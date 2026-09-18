# Estrazione di feature riemanniane a banco di filtri, con riallineamento per run.
#
# E' l'approccio piu' solido oggi disponibile per il motor imagery quando i trial sono pochi,
# come in questo dataset. Tre ingredienti:
#
#   1. Covarianze invece di filtri spaziali. La matrice di covarianza di una finestra contiene
#      per costruzione le potenze di tutti i canali e tutte le loro relazioni: e' un descrittore
#      piu' ricco delle poche componenti che il CSP estrae, e non va addestrato.
#
#   2. Banco di filtri. Una covarianza per sotto-banda, cosi' mu e beta non vengono mescolate
#      in un'unica statistica come accade filtrando 8-30 Hz in un colpo solo.
#
#   3. Riallineamento per run. E' il pezzo che conta di piu' qui. Fra una run e l'altra cambiano
#      impedenze, sonnolenza, livello generale di potenza: le covarianze di run diverse vivono
#      in zone diverse della varieta', e un classificatore addestrato su due run trova la terza
#      spostata. Riportando il baricentro di ogni run all'identita' quello spostamento sparisce.
#      Il baricentro si calcola SENZA etichette, quindi puo' essere stimato anche sulla run di
#      test: e' adattamento di dominio non supervisionato, non leakage. In un sistema reale
#      corrisponde a far registrare all'utente un minuto di segnale prima di iniziare.
#
# Dopo il riallineamento tutte le covarianze sono centrate sull'identita', quindi la proiezione
# nello spazio tangente si fa in quel punto ed e' coerente fra run diverse.

import numpy as np
from mne.filter import filter_data
from pyriemann.estimation import Covariances
from pyriemann.utils.mean import mean_riemann
from pyriemann.utils.base import invsqrtm
from pyriemann.utils.tangentspace import tangent_space

# Sotto-bande: mu, beta bassa, beta alta. Poche e larghe, perche' ogni banda aggiunge
# n_canali * (n_canali + 1) / 2 feature e i trial disponibili sono pochi.
DEFAULT_BANDS = [(8, 13), (13, 20), (20, 30)]


# Covarianze di un insieme di finestre in una singola banda.
# windows shape: (n_windows, n_channels, n_times)
def band_covariances(windows, sfreq, band, estimator='oas'):
    l_freq, h_freq = band
    filtered = filter_data(
        windows.astype(np.float64), sfreq=sfreq,
        l_freq=l_freq, h_freq=h_freq, verbose=False
    )
    return Covariances(estimator=estimator).fit_transform(filtered)


# Covarianze di una run, una matrice per banda.
# Restituisce una lista lunga quanto bands, ciascuna (n_windows, n_channels, n_channels).
def run_covariances(windows, sfreq, bands=None, estimator='oas'):
    bands = DEFAULT_BANDS if bands is None else bands
    return [band_covariances(windows, sfreq, b, estimator) for b in bands]


# Baricentro riemanniano di un insieme di covarianze: il punto della varieta' rispetto al
# quale la nuvola e' centrata. Non usa le etichette.
def reference_mean(covs):
    return mean_riemann(covs)


# Riporta le covarianze attorno all'i dentita' rispetto al riferimento dato.
def recenter(covs, reference):
    W = invsqrtm(reference)
    return np.einsum('ij,njk,kl->nil', W, covs, W)


# Dalle covarianze gia' riallineate al vettore di feature nello spazio tangente, calcolato
# nel punto identita' e concatenato sulle bande.
def to_tangent(covs_per_band):
    features = []
    for covs in covs_per_band:
        identity = np.eye(covs.shape[-1])
        features.append(tangent_space(covs, identity))
    return np.concatenate(features, axis=1)


# Numero di feature prodotte, utile per controllare il rapporto con i campioni disponibili.
def n_features(n_channels, n_bands):
    return n_bands * n_channels * (n_channels + 1) // 2
