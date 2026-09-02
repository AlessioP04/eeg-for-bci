# Selezione dei canali piu' discriminativi a partire dagli ERD/ERS.
#
# Il modulo nasce dal notebook analysis/canali_discriminativi.ipynb: la logica e' stata
# spostata qui perche' la selezione va ricalcolata dentro ogni fold della Leave-One-Run-Out
# usando SOLO le run di training. Calcolarla una volta sola su tutte le run (come avveniva
# prima) fa entrare nella scelta dei canali informazione proveniente dalla run di test.

import numpy as np
import mne
from mne_bids import BIDSPath, read_raw_bids
from scipy.signal import hilbert
from scipy.ndimage import uniform_filter1d

DEFAULT_BANDS = {"mu": (8, 12), "beta": (13, 30)}

# Contrasti disponibili: mappano il nome dell'evento BIDS sul gruppo ("a" oppure "b")
# di cui viene poi confrontato l'ERD medio post-stimolo.
IMAGERY_REST_ACTIVE   = {"TASK2T0": "a", "TASK2T1": "b", "TASK2T2": "b"}
IMAGERY_LEFT_RIGHT    = {"TASK2T1": "a", "TASK2T2": "b"}
EXECUTION_REST_ACTIVE = {"TASK3T0": "a", "TASK3T1": "b", "TASK3T2": "b"}
EXECUTION_HANDS_FEET  = {"TASK3T1": "a", "TASK3T2": "b"}


# Canali candidati: area sensomotoria (centrali, fronto-centrali, centro-parietali).
def candidate_channels(raw):
    C  = ["C1", "C2", "C3", "C4", "C5", "C6", "Cz"]
    FC = [ch for ch in raw.ch_names if ch.startswith("Fc")]
    CP = [ch for ch in raw.ch_names if ch.startswith("Cp")]
    return C + FC + CP


# Potenza istantanea in banda: filtro + inviluppo di Hilbert al quadrato.
def _band_power(X, sfreq, l_freq, h_freq):
    filt = mne.filter.filter_data(
        X.astype(np.float64), sfreq=sfreq,
        l_freq=l_freq, h_freq=h_freq, verbose=False
    )
    return np.abs(hilbert(filt, axis=-1)) ** 2


# Restituisce i canali ordinati per potere discriminante, calcolati sulle sole run passate.
# Da chiamare con le run di training del fold corrente, mai con l'intero set di run.
def select_discriminative_channels(
    subject,
    runs,
    root,
    class_map=IMAGERY_REST_ACTIVE,
    n_channels=10,
    top_per_band=10,
    bands=DEFAULT_BANDS,
    t_pre=1.0,
    t_post=4.0,
    smooth_ms=200,
):
    epochs_a = []
    epochs_b = []
    ch_names = None
    sfreq = None

    for run in runs:
        bids_path = BIDSPath(
            subject=subject,
            task="motion",
            run=run,
            datatype="eeg",
            root=root,
        )

        raw = read_raw_bids(bids_path, verbose=False)
        raw.load_data(verbose=False)
        raw.filter(l_freq=1, h_freq=40, verbose=False)
        raw.set_eeg_reference('average', projection=False, verbose=False)

        picks = mne.pick_channels(raw.ch_names, candidate_channels(raw))

        if ch_names is None:
            ch_names = [raw.ch_names[p] for p in picks]
            sfreq = int(raw.info['sfreq'])

        n_pre  = int(t_pre  * sfreq)
        n_post = int(t_post * sfreq)

        events, event_id = mne.events_from_annotations(raw, verbose=False)
        code_map = {
            event_id[name]: group
            for name, group in class_map.items()
            if name in event_id
        }

        data = raw.get_data(picks=picks)

        for onset, _, code in events:
            if code not in code_map:
                continue

            start = onset - n_pre
            end   = onset + n_post

            if start < 0 or end > data.shape[1]:
                continue

            epoch = data[:, start:end]
            if code_map[code] == "a":
                epochs_a.append(epoch)
            else:
                epochs_b.append(epoch)

    if not epochs_a or not epochs_b:
        raise ValueError(f"Soggetto {subject}: trial insufficienti nelle run {runs}")

    X_a = np.array(epochs_a)
    X_b = np.array(epochs_b)
    X_all = np.concatenate([X_a, X_b], axis=0)

    n_pre = int(t_pre * sfreq)
    smooth = int(smooth_ms * sfreq / 1000)
    scores_per_band = np.zeros((len(bands), len(ch_names)))

    for b_idx, (l_freq, h_freq) in enumerate(bands.values()):
        power_a   = _band_power(X_a,   sfreq, l_freq, h_freq)
        power_b   = _band_power(X_b,   sfreq, l_freq, h_freq)
        power_all = _band_power(X_all, sfreq, l_freq, h_freq)

        # Baseline comune alle due classi: media pre-stimolo su tutti i trial
        baseline = np.mean(power_all[:, :, :n_pre], axis=(0, 2))[:, np.newaxis]

        erd_a = (uniform_filter1d(np.mean(power_a, axis=0), smooth, axis=-1) - baseline) / baseline * 100
        erd_b = (uniform_filter1d(np.mean(power_b, axis=0), smooth, axis=-1) - baseline) / baseline * 100

        # Potere discriminante = distanza tra gli ERD medi post-stimolo delle due classi
        scores_per_band[b_idx] = np.abs(
            np.mean(erd_b[:, n_pre:], axis=1) - np.mean(erd_a[:, n_pre:], axis=1)
        )

    # Top per banda, poi unione senza duplicati mantenendo l'ordine
    selected = []
    seen = set()
    for b_idx in range(len(bands)):
        top_idx = np.argsort(scores_per_band[b_idx])[::-1][:top_per_band]
        for j in top_idx:
            ch = ch_names[j]
            if ch not in seen and len(selected) < n_channels:
                seen.add(ch)
                selected.append(ch)

    return selected
