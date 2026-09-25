# Predittore neurofisiologico della prestazione BCI, calcolato dalle run di baseline.
#
# L'idea: il motor imagery funziona rompendo la sincronia del ritmo mu sensomotorio. Se a
# riposo quel ritmo non c'e', non c'e' niente da rompere e il soggetto non otterra' controllo.
# Il predittore misura quanto e' marcato il ritmo mu di una persona che sta ferma, e lo fa
# rispetto al fondo spettrale invece che in assoluto, cosi' da non misurare lo spessore del
# cranio o l'impedenza degli elettrodi.
#
# Si calcola sulle run 1 e 2 (baseline), mentre la prestazione si misura sulle run 4, 8 e 12:
# i due insiemi di dati non si toccano, quindi non c'e' circolarita'.

import numpy as np
from scipy.signal import welch
from mne_bids import BIDSPath, read_raw_bids

# Run di baseline del protocollo
BASELINE_EYES_OPEN = "1"    # 61 s a occhi aperti: e' quella giusta per il mu
BASELINE_EYES_CLOSED = "2"  # 61 s a occhi chiusi: utile solo come controllo

# Vicini usati dal laplaciano. Il mu e' focale, l'alfa residuo e' diffuso: sottraendo a un
# elettrodo la media dei quattro che lo circondano si tiene il primo e si cancella il secondo.
LAPLACIAN_NEIGHBOURS = {
    "C3": ["Fc3", "Cp3", "C1", "C5"],
    "C4": ["Fc4", "Cp4", "C2", "C6"],
    "Cz": ["Fcz", "Cpz", "C1", "C2"],
}

MU_BAND = (7.0, 14.0)     # banda in cui si cerca la gobba, larga per accogliere le variazioni
                          # individuali della frequenza del mu
FIT_RANGE = (3.0, 40.0)   # intervallo su cui si stima il fondo spettrale


# Laplaciano di superficie: segnale dell'elettrodo centrale meno la media dei vicini.
#
# Con laplacian=False si restituisce il canale grezzo. Serve come termine di paragone: e' la
# scelta fatta da chi misura il predittore sui canali non filtrati spazialmente, e su quel
# segnale la banda 8-13 Hz contiene, oltre al mu sensomotorio, anche l'alfa occipitale che vi
# arriva per conduzione di volume. Il confronto fra le due versioni dice quanto pesi quella
# contaminazione.
def laplacian_signal(raw, centre, laplacian=True):
    centre_data = raw.get_data(picks=[centre])[0]

    if not laplacian:
        return centre_data

    neighbours = LAPLACIAN_NEIGHBOURS[centre]
    ring_data = raw.get_data(picks=neighbours).mean(axis=0)
    return centre_data - ring_data


# Spettro di potenza con il metodo di Welch: il segnale viene spezzato in segmenti che si
# sovrappongono a meta', di ognuno si calcola lo spettro e si fa la media. Segmenti da 2 s
# danno una risoluzione di 0.5 Hz, sufficiente a distinguere la gobba del mu.
def power_spectrum(signal, sfreq, segment_seconds=2.0):
    nperseg = int(segment_seconds * sfreq)
    freqs, psd = welch(signal, fs=sfreq, nperseg=nperseg, noverlap=nperseg // 2)
    return freqs, psd


# Stima del fondo 1/f. In scala doppiamente logaritmica l'attivita' di fondo dell'EEG e'
# all'incirca una retta, quindi basta una regressione lineare. La banda mu viene esclusa dal
# fit: se la gobba partecipasse alla stima del fondo, alzerebbe il fondo stesso e la misura
# della sua altezza risulterebbe schiacciata.
def fit_background(freqs, psd, mu_band=MU_BAND, fit_range=FIT_RANGE):
    in_fit = (freqs >= fit_range[0]) & (freqs <= fit_range[1])
    in_mu = (freqs >= mu_band[0]) & (freqs <= mu_band[1])
    used = in_fit & ~in_mu

    slope, intercept = np.polyfit(np.log10(freqs[used]), np.log10(psd[used]), 1)
    return float(slope), float(intercept)


# Riporta la retta stimata in scala lineare, per confrontarla con lo spettro o per disegnarla.
def background_curve(freqs, slope, intercept):
    return 10 ** (intercept + slope * np.log10(freqs))


# Il predittore vero e proprio: di quanto la gobba del mu supera il fondo, in decibel.
# Restituisce anche la frequenza a cui si trova il picco (la frequenza mu individuale, che
# varia da persona a persona) e la pendenza del fondo.
def peak_over_background(freqs, psd, mu_band=MU_BAND, fit_range=FIT_RANGE):
    slope, intercept = fit_background(freqs, psd, mu_band, fit_range)

    in_mu = (freqs >= mu_band[0]) & (freqs <= mu_band[1])
    ratio = psd[in_mu] / background_curve(freqs[in_mu], slope, intercept)
    best = int(np.argmax(ratio))

    return {
        "prominence_db": float(10 * np.log10(ratio[best])),
        "peak_hz": float(freqs[in_mu][best]),
        "background_slope": slope,
    }


# Predittore di un soggetto, calcolato su una run di baseline e su piu' elettrodi.
#
# Il valore per emisfero conta: un soggetto puo' avere il mu marcato da un lato e assente
# dall'altro, e per classificare sinistra contro destra serve che ci sia da entrambe le parti.
# Per questo oltre alla media viene restituito anche il minimo fra i canali.
def subject_predictor(subject, root, run=BASELINE_EYES_OPEN, channels=("C3", "C4"),
                      laplacian=True):
    bids_path = BIDSPath(
        subject=subject, task="motion", run=run, datatype="eeg", root=root
    )
    raw = read_raw_bids(bids_path, verbose=False)
    raw.load_data(verbose=False)
    sfreq = raw.info["sfreq"]

    result = {"subject": subject, "sfreq": sfreq}
    prominences = []

    for channel in channels:
        signal = laplacian_signal(raw, channel, laplacian)
        freqs, psd = power_spectrum(signal, sfreq)
        measured = peak_over_background(freqs, psd)

        result[f"{channel}_db"] = measured["prominence_db"]
        result[f"{channel}_hz"] = measured["peak_hz"]
        prominences.append(measured["prominence_db"])

    result["mean_db"] = float(np.mean(prominences))
    result["min_db"] = float(np.min(prominences))
    return result


# Spettro, fondo stimato e misura, per disegnare la figura di un singolo soggetto.
def spectrum_for_plot(subject, root, channel="C3", run=BASELINE_EYES_OPEN, laplacian=True):
    bids_path = BIDSPath(
        subject=subject, task="motion", run=run, datatype="eeg", root=root
    )
    raw = read_raw_bids(bids_path, verbose=False)
    raw.load_data(verbose=False)

    signal = laplacian_signal(raw, channel, laplacian)
    freqs, psd = power_spectrum(signal, raw.info["sfreq"])

    slope, intercept = fit_background(freqs, psd)
    visible = (freqs >= FIT_RANGE[0]) & (freqs <= FIT_RANGE[1])

    return (
        freqs[visible],
        psd[visible],
        background_curve(freqs[visible], slope, intercept),
        peak_over_background(freqs, psd),
    )
