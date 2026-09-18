# Primitive per simulare il funzionamento online (live) di una pipeline BCI.
#
# Le pipeline offline possono permettersi di guardare l'intera registrazione: filtrano con un
# filtro a fase zero, che compensa il ritardo usando anche i campioni futuri. Dal vivo questo
# non e' possibile, perche' i campioni futuri semplicemente non esistono ancora. Questo modulo
# fornisce i pezzi per rieseguire una run rispettando la causalita': filtro con stato
# persistente, buffer circolare e soglia probabilistica calibrata sui soli dati di training.

import numpy as np
import mne
from scipy.signal import butter, sosfilt, group_delay


# Filtro passa banda causale (Butterworth IIR) con stato persistente fra un blocco e il
# successivo. Filtrare un array intero in una sola chiamata o filtrarlo a blocchi portandosi
# dietro lo stato da' esattamente lo stesso risultato: e' questo che rende confrontabili la
# versione "offline causale" e quella riprodotta campione per campione.
class CausalBandpass:
    def __init__(self, l_freq, h_freq, sfreq, order=4):
        self.sos = butter(order, [l_freq, h_freq], btype='band', fs=sfreq, output='sos')
        self.sfreq = sfreq
        self.zi = None

    # Lo stato parte da zero: e' il transitorio che un sistema reale subisce all'accensione.
    def reset(self, n_channels):
        self.zi = np.zeros((self.sos.shape[0], n_channels, 2))

    # block shape: (n_channels, n_samples)
    def __call__(self, block):
        if self.zi is None or self.zi.shape[1] != block.shape[0]:
            self.reset(block.shape[0])

        out, self.zi = sosfilt(self.sos, block, axis=-1, zi=self.zi)
        return out

    # Ritardo di gruppo in secondi alla frequenza indicata: e' la quota di latenza
    # introdotta dal filtro, che il filtro a fase zero invece annulla barando sul futuro.
    def group_delay_s(self, freq):
        from scipy.signal import sos2tf
        b, a = sos2tf(self.sos)
        w, gd = group_delay((b, a), fs=self.sfreq)
        return float(np.interp(freq, w, gd) / self.sfreq)


# Buffer circolare: accumula i campioni in arrivo e tiene sempre gli ultimi window_samples.
# Alimentandolo a blocchi di step_samples campioni, ogni push corrisponde a una finestra
# della sliding window offline, cosi' le due valutazioni restano allineate indice per indice.
class RingBuffer:
    def __init__(self, n_channels, window_samples):
        self.buffer = np.zeros((n_channels, window_samples))
        self.window_samples = window_samples
        self.received = 0

    def push(self, block):
        n = block.shape[1]

        if n >= self.window_samples:
            self.buffer = block[:, -self.window_samples:].copy()
        else:
            self.buffer = np.concatenate([self.buffer[:, n:], block], axis=1)

        self.received += n

    @property
    def ready(self):
        return self.received >= self.window_samples

    def window(self):
        return self.buffer.copy()


# Riferimento medio: si calcola sui canali dello stesso istante, quindi e' gia' causale.
def average_reference(block):
    return block - block.mean(axis=0, keepdims=True)


# Soglia probabilistica calibrata sui dati di training. Offline la soglia poteva scendere
# guardando quanti campioni di test venivano accettati; dal vivo il test non esiste ancora,
# quindi il valore va fissato qui e poi congelato.
def calibrate_threshold(probs, start=0.90, minimum=0.50, min_accepted_ratio=0.70, step=0.05):
    max_probs = np.max(probs, axis=1)
    threshold = start

    while np.mean(max_probs >= threshold) < min_accepted_ratio and threshold > minimum:
        threshold -= step

    return threshold


# Ricostruisce un oggetto Raw a partire da dati gia' pre-processati, per poter riusare
# create_sliding_windows e create_window_labels senza duplicarne la logica.
def as_raw(data, info):
    return mne.io.RawArray(data, info.copy(), verbose=False)
