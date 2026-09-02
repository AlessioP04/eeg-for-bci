Informazioni: 
7 giugno 2026
Prima run completa: gridsearch più approfondito e discriminazione dei canali tramite opportuno script.
Finestra 2/0.5s. Threshold probabilistico dinamico da 90% in giù. Finestra etichettata se active>80%.
============================================================
Paziente 001
============================================================
Canali selezionati (10): ['C3', 'Fc3', 'Fc4', 'C5', 'Fc1', 'Fc2', 'C4', 'Cp3', 'Fc5', 'Cp6']

  Run test: 4 | Threshold: 0.60
  Campioni: 84 tot / 62 acc / 22 ↓ (26.2%)
  Accuracy: 79.05% | Best params: C=0.1, components=4
  Tempo: 26.3s

  Run test: 8 | Threshold: 0.80
  Campioni: 84 tot / 64 acc / 20 ↓ (23.8%)
  Accuracy: 68.75% | Best params: C=0.1, components=6
  Tempo: 13.3s

  Run test: 12 | Threshold: 0.70
  Campioni: 84 tot / 61 acc / 23 ↓ (27.4%)
  Accuracy: 77.15% | Best params: C=100, components=4
  Tempo: 13.4s
  
┌──────────────────────────────────────────────────────────┐
│ Paziente 001:  74.98% | Tempo totale:   53.0s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 002
============================================================
Canali selezionati (10): ['C5', 'C6', 'Cp1', 'Cp3', 'Fc5', 'Cp6', 'C4', 'C3', 'C1', 'Cp4']

  Run test: 4 | Threshold: 0.85
  Campioni: 84 tot / 63 acc / 21 ↓ (25.0%)
  Accuracy: 87.35% | Best params: C=10, components=4
  Tempo: 18.0s

  Run test: 8 | Threshold: 0.75
  Campioni: 84 tot / 64 acc / 20 ↓ (23.8%)
  Accuracy: 96.80% | Best params: C=10, components=6
  Tempo: 17.6s

  Run test: 12 | Threshold: 0.90
  Campioni: 84 tot / 59 acc / 25 ↓ (29.8%)
  Accuracy: 79.63% | Best params: C=1, components=8
  Tempo: 18.0s

┌──────────────────────────────────────────────────────────┐
│ Paziente 002:  87.93% | Tempo totale:   53.7s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 003
============================================================
Canali selezionati (10): ['Cp3', 'Fcz', 'Fc2', 'Fc6', 'Fc4', 'Cp1', 'Fc1', 'Cp2', 'C5', 'Cz']

  Run test: 4 | Threshold: 0.50
  Campioni: 84 tot / 84 acc / 0 ↓ (0.0%)
  Accuracy: 54.76% | Best params: C=0.1, components=6
  Tempo: 13.8s

  Run test: 8 | Threshold: 0.55
  Campioni: 84 tot / 67 acc / 17 ↓ (20.2%)
  Accuracy: 37.66% | Best params: C=100, components=6
  Tempo: 13.3s

  Run test: 12 | Threshold: 0.60
  Campioni: 84 tot / 61 acc / 23 ↓ (27.4%)
  Accuracy: 52.71% | Best params: C=1, components=2
  Tempo: 13.2s

┌──────────────────────────────────────────────────────────┐
│ Paziente 003:  48.38% | Tempo totale:   40.4s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 004
============================================================
Canali selezionati (10): ['Fc6', 'Fc4', 'Cp3', 'Cp1', 'Cp2', 'Cpz', 'C3', 'Cp6', 'C1', 'Fc3']

  Run test: 4 | Threshold: 0.65
  Campioni: 84 tot / 65 acc / 19 ↓ (22.6%)
  Accuracy: 57.14% | Best params: C=100, components=4
  Tempo: 13.3s

  Run test: 8 | Threshold: 0.65
  Campioni: 84 tot / 66 acc / 18 ↓ (21.4%)
  Accuracy: 57.74% | Best params: C=100, components=8
  Tempo: 13.3s

  Run test: 12 | Threshold: 0.70
  Campioni: 84 tot / 59 acc / 25 ↓ (29.8%)
  Accuracy: 72.64% | Best params: C=100, components=4
  Tempo: 13.8s

┌──────────────────────────────────────────────────────────┐
│ Paziente 004:  62.51% | Tempo totale:   40.4s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 005
============================================================
Canali selezionati (10): ['Fcz', 'C2', 'C4', 'Fc1', 'Fc2', 'Cp4', 'Cp2', 'Fc5', 'C6', 'Cz']

  Run test: 4 | Threshold: 0.65
  Campioni: 84 tot / 61 acc / 23 ↓ (27.4%)
  Accuracy: 80.11% | Best params: C=10, components=4
  Tempo: 18.5s

  Run test: 8 | Threshold: 0.70
  Campioni: 84 tot / 65 acc / 19 ↓ (22.6%)
  Accuracy: 57.05% | Best params: C=10, components=6
  Tempo: 18.2s

  Run test: 12 | Threshold: 0.60
  Campioni: 84 tot / 65 acc / 19 ↓ (22.6%)
  Accuracy: 54.87% | Best params: C=10, components=2
  Tempo: 17.9s

┌──────────────────────────────────────────────────────────┐
│ Paziente 005:  64.01% | Tempo totale:   54.6s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 006
============================================================
Canali selezionati (10): ['Cp4', 'Cp6', 'C4', 'Cp2', 'Fc5', 'C5', 'Fc4', 'Fc2', 'C2', 'Fcz']

  Run test: 4 | Threshold: 0.65
  Campioni: 84 tot / 62 acc / 22 ↓ (26.2%)
  Accuracy: 44.27% | Best params: C=100, components=8
  Tempo: 15.9s

  Run test: 8 | Threshold: 0.75
  Campioni: 84 tot / 62 acc / 22 ↓ (26.2%)
  Accuracy: 50.00% | Best params: C=10, components=4
  Tempo: 16.7s

  Run test: 12 | Threshold: 0.60
  Campioni: 84 tot / 67 acc / 17 ↓ (20.2%)
  Accuracy: 60.70% | Best params: C=10, components=8
  Tempo: 17.8s

┌──────────────────────────────────────────────────────────┐
│ Paziente 006:  51.66% | Tempo totale:   50.5s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 007
============================================================
Canali selezionati (10): ['Cp5', 'Cp3', 'Fcz', 'Fc2', 'Fc4', 'Cp1', 'Cz', 'C1', 'Fc1', 'C4']

  Run test: 4 | Threshold: 0.75
  Campioni: 84 tot / 62 acc / 22 ↓ (26.2%)
  Accuracy: 96.15% | Best params: C=1, components=2
  Tempo: 14.4s

  Run test: 8 | Threshold: 0.90
  Campioni: 84 tot / 61 acc / 23 ↓ (27.4%)
  Accuracy: 100.00% | Best params: C=100, components=2
  Tempo: 13.7s

  Run test: 12 | Threshold: 0.90
  Campioni: 84 tot / 73 acc / 11 ↓ (13.1%)
  Accuracy: 100.00% | Best params: C=10, components=2
  Tempo: 14.8s

┌──────────────────────────────────────────────────────────┐
│ Paziente 007:  98.72% | Tempo totale:   42.9s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 008
============================================================
Canali selezionati (10): ['Fc4', 'Fc2', 'Fcz', 'Fc1', 'C2', 'Fc6', 'Fc3', 'Cz', 'C1', 'C6']

  Run test: 4 | Threshold: 0.65
  Campioni: 84 tot / 60 acc / 24 ↓ (28.6%)
  Accuracy: 42.55% | Best params: C=1, components=8
  Tempo: 14.8s

  Run test: 8 | Threshold: 0.60
  Campioni: 84 tot / 63 acc / 21 ↓ (25.0%)
  Accuracy: 63.64% | Best params: C=10, components=4
  Tempo: 14.2s

  Run test: 12 | Threshold: 0.70
  Campioni: 84 tot / 59 acc / 25 ↓ (29.8%)
  Accuracy: 41.95% | Best params: C=1, components=4
  Tempo: 14.3s

┌──────────────────────────────────────────────────────────┐
│ Paziente 008:  49.38% | Tempo totale:   43.3s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 009
============================================================
Canali selezionati (10): ['Fcz', 'Fc1', 'Cp5', 'Fc3', 'Fc2', 'Cz', 'Fc5', 'C1', 'C6', 'C3']

  Run test: 4 | Threshold: 0.85
  Campioni: 84 tot / 63 acc / 21 ↓ (25.0%)
  Accuracy: 55.17% | Best params: C=0.1, components=8
  Tempo: 21.4s

  Run test: 8 | Threshold: 0.75
  Campioni: 84 tot / 60 acc / 24 ↓ (28.6%)
  Accuracy: 67.51% | Best params: C=0.1, components=2
  Tempo: 20.1s

  Run test: 12 | Threshold: 0.60
  Campioni: 84 tot / 59 acc / 25 ↓ (29.8%)
  Accuracy: 64.57% | Best params: C=0.1, components=8
  Tempo: 20.3s

┌──────────────────────────────────────────────────────────┐
│ Paziente 009:  62.42% | Tempo totale:   61.8s │
└──────────────────────────────────────────────────────────┘

============================================================
Paziente 010
============================================================
Canali selezionati (10): ['Fc1', 'C4', 'C1', 'Cp1', 'C3', 'Cp4', 'Cpz', 'Cp3', 'Cp2', 'C6']

  Run test: 4 | Threshold: 0.65
  Campioni: 84 tot / 66 acc / 18 ↓ (21.4%)
  Accuracy: 50.00% | Best params: C=10, components=6
  Tempo: 14.7s

  Run test: 8 | Threshold: 0.75
  Campioni: 84 tot / 64 acc / 20 ↓ (23.8%)
  Accuracy: 60.85% | Best params: C=0.1, components=4
  Tempo: 13.5s

  Run test: 12 | Threshold: 0.70
  Campioni: 84 tot / 60 acc / 24 ↓ (28.6%)
  Accuracy: 53.33% | Best params: C=1, components=2
  Tempo: 13.6s

┌──────────────────────────────────────────────────────────┐
│ Paziente 010:  54.73% | Tempo totale:   41.8s │
└──────────────────────────────────────────────────────────┘
 

============================================================
RISULTATI FINALI
============================================================
Accuracy media:      65.47%
Deviazione standard: 17.57%
Min/Max:             37.66% / 100.00%

Matrice di confusione media:
[[89 36]
 [55 70]]

Timing:
  Tempo totale: 8.0 minuti
  Tempo medio/paziente: 48.2s
  Paziente 001: 53.0s
  Paziente 002: 53.7s
  Paziente 003: 40.4s
  Paziente 004: 40.4s
  Paziente 005: 54.6s
  Paziente 006: 50.5s
  Paziente 007: 42.9s
  Paziente 008: 43.3s
  Paziente 009: 61.8s
  Paziente 010: 41.8s







f