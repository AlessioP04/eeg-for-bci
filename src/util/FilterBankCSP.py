from sklearn.base import BaseEstimator, TransformerMixin
from mne.decoding import CSP
from mne.filter import filter_data
import numpy as np

# Banco di filtri del FBCSP: sotto-bande da 4 Hz che coprono theta, mu e beta.
DEFAULT_BANDS = [
    (4, 8), (8, 12), (12, 16), (16, 20), (20, 24),
    (24, 28), (28, 32), (32, 36), (36, 40)
]


# Generalizzazione di DualBandCSP a un numero qualsiasi di sotto-bande: un CSP indipendente
# per ciascuna, con le feature poi concatenate. La selezione delle piu' informative non e'
# fatta qui ma a valle nella Pipeline, con SelectKBest e mutua informazione.
#
# Il segnale in ingresso deve essere filtrato su una banda larga (tipicamente 4-40 Hz):
# se arriva gia' ristretto a 8-30 Hz le sotto-bande esterne restano vuote.
class FilterBankCSP(BaseEstimator, TransformerMixin):
    def __init__(self, n_components=4, reg='ledoit_wolf', log=True, sfreq=160, bands=None):
        self.n_components = n_components
        self.reg = reg
        self.log = log
        self.sfreq = sfreq
        self.bands = bands

    def _bands(self):
        return DEFAULT_BANDS if self.bands is None else self.bands

    # X shape: (n_windows, n_channels, n_times)
    def _bandpass(self, X, l_freq, h_freq):
        return filter_data(
            X.astype(np.float64),
            sfreq=self.sfreq,
            l_freq=l_freq,
            h_freq=h_freq,
            verbose=False
        )

    def fit(self, X, y):
        self.csp_ = []

        for l_freq, h_freq in self._bands():
            csp = CSP(n_components=self.n_components, reg=self.reg, log=self.log)
            csp.fit(self._bandpass(X, l_freq, h_freq), y)
            self.csp_.append(csp)

        return self

    def transform(self, X):
        features = [
            csp.transform(self._bandpass(X, l_freq, h_freq))
            for csp, (l_freq, h_freq) in zip(self.csp_, self._bands())
        ]

        return np.concatenate(features, axis=1)
