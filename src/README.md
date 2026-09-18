# Struttura del codice

Tutto il codice scritto per la tesi vive in questa cartella. I dati restano fuori, in
`data/` (formato BIDS) e `rawdata/` (EDF originali).

```
src/
├── pipelines/     Pipeline di classificazione complete, con validazione Leave-One-Run-Out
├── analysis/      Analisi neurofisiologiche: ERD/ERS e selezione dei canali
├── experiments/   Confronti metodologici precedenti, tenuti come riferimento per la tesi
├── util/          Moduli python riusabili, importati dai notebook
├── docs/          Materiale di riferimento (montaggio elettrodi, esempi MNE)
├── results/       Output testuali delle esecuzioni, in markdown
└── plots/         Grafici generati dai notebook di analysis/
```

## pipelines/

Due task, tre metodi di estrazione delle feature, sei notebook. Le colonne sono i task:

| Metodo | Motor imagery (run 4, 8, 12) | Motor execution (run 5, 9, 13) |
|---|---|---|
| CSP a banda singola | `CSP_motor_imagery.ipynb` | `CSP_motor_execution.ipynb` |
| Filter Bank CSP | `FBCSP_motor_imagery.ipynb` | `FBCSP_motor_execution.ipynb` |
| Riemanniano | `Riemann_motor_imagery.ipynb` | `Riemann_motor_execution.ipynb` |

Le classi sono pugno sinistro vs destro **immaginato** per il motor imagery, entrambi i pugni
vs entrambi i piedi con movimento **reale** per il motor execution.

Tutte e sei condividono la stessa impalcatura: lettura BIDS → filtro passa banda → riferimento
medio → sliding window → estrazione feature → SVM con `GridSearchCV` → Leave-One-Run-Out
sulle tre run → soglia probabilistica. Cambia solo il blocco di feature extraction:

- **CSP** — un CSP sulla banda 8-30 Hz, il baseline classico.
- **FBCSP** — un CSP indipendente per ognuna delle nove sotto-bande da 4 Hz fra 4 e 40 Hz
  (`util/FilterBankCSP.py`), seguito da `SelectKBest` con mutua informazione. Qui il filtro
  passa banda è 4-40 Hz e non 8-30: restringerlo lascerebbe vuote le sotto-bande esterne.
  La `Pipeline` usa una cache su disco perché altrimenti il banco di filtri verrebbe
  ricalcolato a ogni combinazione della griglia, con tempi circa tripli.
- **Riemanniano** — matrice di covarianza di ogni finestra proiettata nello spazio tangente
  (`pyriemann`), poi SVM. È il più veloce dei tre di un ordine di grandezza.

Nell'impalcatura non c'è più la pulizia ICA, che prima veniva ristimata su ogni run. La
rimozione è stata decisa dopo averla misurata: nella banda 8-30 Hz scartava in media 0,5
componenti su 15 ed era quindi inerte, mentre nella banda 4-40 Hz ne scartava 6,5, quasi tutte
classificate come muscolari, e su otto soggetti costava 2,45 punti di balanced accuracy
(6 soggetti su 8 peggioravano, p = 0,148). Il calo resta anche tenendo il solo rilevamento
oculare (−1,19 punti) e non cambia stimando l'ICA su una copia filtrata a 1-40 Hz come vuole
la prassi (+0,02 punti): il dataset non ha canali EOG dedicati, `find_bads_eog` usa Fp1 e Fp2
come surrogati e finisce per rimuovere anche segnale utile. Senza ICA le pipeline sono anche
circa il doppio più veloci.

La cross validation interna alla `GridSearchCV` usa `StratifiedGroupKFold` raggruppando per
trial: le finestre si sovrappongono al 75% e, divise a caso, finirebbero quasi identiche sia
in train sia in validation, gonfiando lo score con cui vengono scelti gli iperparametri.

### Simulazione online

`Online_motor_imagery.ipynb` e `Online_motor_execution.ipynb` non sono un quarto metodo ma una
modalità di valutazione: misurano quanto costa il vincolo di causalità, cioè la differenza fra
quello che la pipeline ottiene potendo leggere l'intera registrazione e quello che otterrebbe
dal vivo, ricevendo i campioni man mano. Le due differenze sono:

1. **Filtro causale.** `raw.filter()` usa `phase='zero'`, che secondo la documentazione di MNE
   compensa il ritardo *rendendo il filtro non causale*: guarda i campioni futuri. La versione
   online usa un Butterworth IIR in avanti soltanto, con lo stato portato da un blocco al
   successivo.
2. **Soglia congelata.** Offline scende finché non accetta il 70% del test set, il che richiede
   di conoscerlo in anticipo. Online lo stesso criterio si applica alle probabilità ottenute in
   cross validation sul training, e il valore risultante non si tocca più.

La run di test viene poi riprodotta a blocchi di mezzo secondo attraverso un buffer circolare.
Il notebook stampa una verifica di correttezza: lo stesso pre-processing calcolato in un colpo
solo deve dare le identiche probabilità del replay a blocchi, e la differenza attesa è zero.

Le predizioni con probabilità massima sotto soglia vengono scartate anziché emesse: è una
scelta di progetto, in un sistema BCI è preferibile non emettere un comando piuttosto che
emetterne uno sbagliato. Per questo i risultati vanno letti come **accuratezza relativa a
una certa percentuale di campioni scartati**, mai come accuratezza assoluta: entrambe le
pipeline stampano le due grandezze insieme.

I parametri stanno tutti nel blocco `Configurazione` in cima alla cella. In particolare
`CHANNEL_MODE` sceglie come vengono selezionati i canali:

- `"auto"` — ricalcolati dentro ogni fold della LORO sulle sole run di training, tramite
  `util.channel_selection`. Vanno calcolati per forza dentro il fold: una selezione unica su
  tutte e tre le run guarderebbe anche la run di test e falserebbe la validazione.
- `"fixed"` — la lista in `FIXED_CHANNELS`, cioè i canali sensomotori scelti anatomicamente.

Il default è `"fixed"` ovunque tranne che in `CSP_motor_imagery.ipynb`. In un confronto su tre
soggetti con la pipeline riemanniana i canali fissi hanno reso più della selezione automatica
(69,2% contro 64,9% con il contrasto riposo/attivazione e 68,1% con quello sinistra/destra),
ma con deviazioni standard fra i 13 e i 20 punti: su tre soggetti la differenza non è
conclusiva e andrebbe rimisurata su tutti e 109.

## analysis/

- `erd_ers_lr.ipynb` — ERD/ERS in banda mu e beta, sinistra vs destra, salvati in `plots/erd_ers/`
- `erd_ers_ra.ipynb` — stessa analisi per il contrasto riposo vs attivazione
- `canali_discriminativi.ipynb` — stampa i canali selezionati fold per fold, per ispezionare
  cosa sceglie `util.channel_selection` prima di lanciare una pipeline

## util/

- `preprocessing.py` — sliding window sul segnale raw e relativa etichettatura
- `channel_selection.py` — canali più discriminativi a partire dagli ERD/ERS, calcolati su un
  sottoinsieme di run scelto dal chiamante
- `online_simulation.py` — primitive per il funzionamento dal vivo: filtro causale con stato,
  buffer circolare, calibrazione della soglia
- `FilterBankCSP.py` — un CSP per ogni sotto-banda del banco di filtri, con le feature concatenate
- `DualBandCSP.py` — versione a due sole bande, mu e beta, precedente al `FilterBankCSP`
- `modifica_tsv.py` — script una tantum sui `*_channels.tsv`, da eseguire dopo aver scaricato
  il dataset (vedi il README nella root)

## Dipendenze

`mne`, `mne-bids`, `scikit-learn`, `numpy`, `scipy`, `pandas`, `matplotlib`, più `pyriemann`
per le due pipeline riemanniane.

## Come si lanciano i notebook

Ogni notebook si apre con lo stesso preambolo, che risale l'albero delle cartelle fino alla
root del progetto e aggiunge `src/` al path di import. Non ci sono percorsi relativi da
aggiustare: il notebook funziona indipendentemente dalla cartella da cui parte il kernel, e
`DATA`, `PLOTS` e `PROJECT_ROOT` sono già disponibili.

## Note sul dataset

I soggetti **088, 092 e 100** sono campionati a 128 Hz invece che a 160 Hz: vanno esclusi o
ricampionati quando si estende l'analisi a tutti e 109 i soggetti. Il **089** ha annotazioni
irregolari ed è escluso per convenzione nella letteratura su questo dataset.
