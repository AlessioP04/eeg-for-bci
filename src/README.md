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

| Notebook | Run | Classi |
|---|---|---|
| `CSP_motor_imagery.ipynb` | 4, 8, 12 | pugno sinistro vs destro **immaginato** |
| `CSP_motor_execution.ipynb` | 5, 9, 13 | entrambi i pugni vs entrambi i piedi, movimento **reale** |

Entrambe seguono la stessa sequenza: lettura BIDS → filtro 8-30 Hz → riferimento medio →
ICA → sliding window → CSP → SVM con `GridSearchCV` → Leave-One-Run-Out sulle tre run.

Le predizioni con probabilità massima sotto soglia vengono scartate anziché emesse: è una
scelta di progetto, in un sistema BCI è preferibile non emettere un comando piuttosto che
emetterne uno sbagliato. Per questo i risultati vanno letti come **accuratezza relativa a
una certa percentuale di campioni scartati**, mai come accuratezza assoluta: entrambe le
pipeline stampano le due grandezze insieme.

I parametri stanno tutti nel blocco `Configurazione` in cima alla cella. In particolare
`CHANNEL_MODE` sceglie come vengono selezionati i canali:

- `"auto"` — ricalcolati dentro ogni fold della LORO sulle sole run di training, tramite
  `util.channel_selection`. È il default per il motor imagery.
- `"fixed"` — la lista in `FIXED_CHANNELS`, comoda per le prove veloci e per riprodurre i
  risultati già documentati in `results/`. È il default per il motor execution.

## analysis/

- `erd_ers_lr.ipynb` — ERD/ERS in banda mu e beta, sinistra vs destra, salvati in `plots/erd_ers/`
- `erd_ers_ra.ipynb` — stessa analisi per il contrasto riposo vs attivazione
- `canali_discriminativi.ipynb` — stampa i canali selezionati fold per fold, per ispezionare
  cosa sceglie `util.channel_selection` prima di lanciare una pipeline

## util/

- `preprocessing.py` — sliding window sul segnale raw e relativa etichettatura
- `channel_selection.py` — canali più discriminativi a partire dagli ERD/ERS, calcolati su un
  sottoinsieme di run scelto dal chiamante
- `DualBandCSP.py` — trasformatore che concatena due CSP, uno in banda mu e uno in banda beta
- `modifica_tsv.py` — script una tantum sui `*_channels.tsv`, da eseguire dopo aver scaricato
  il dataset (vedi il README nella root)

## Come si lanciano i notebook

Ogni notebook si apre con lo stesso preambolo, che risale l'albero delle cartelle fino alla
root del progetto e aggiunge `src/` al path di import. Non ci sono percorsi relativi da
aggiustare: il notebook funziona indipendentemente dalla cartella da cui parte il kernel, e
`DATA`, `PLOTS` e `PROJECT_ROOT` sono già disponibili.

## Note sul dataset

I soggetti **088, 092 e 100** sono campionati a 128 Hz invece che a 160 Hz: vanno esclusi o
ricampionati quando si estende l'analisi a tutti e 109 i soggetti. Il **089** ha annotazioni
irregolari ed è escluso per convenzione nella letteratura su questo dataset.
