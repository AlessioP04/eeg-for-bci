Solite caratteristiche, pipeline classica
============================================================
Fold riusciti:          327/327
Stadio 1 da solo:       68.18%   (riposo vs attivo)
Stadio 2 da solo:       38.13%   (quattro movimenti, stadio 1 supposto perfetto)
Prodotto dei due:       25.99%   (stima grossolana di quanto costa la serie)
Catena completa:        36.46%   con 26.3% di campioni scartati
Deviazione standard:    12.85%
Caso su cinque classi:  20.00%

Matrice di confusione media (righe = vero, colonne = predetto):
                riposo   pugno sx   pugno dx  due pugni  due piedi
     riposo      156.4        9.2        9.1        8.8        9.1
   pugno sx       11.7        6.2        2.9        4.4        2.9
   pugno dx       11.6        3.1        6.6        3.9        3.0
  due pugni       10.3        4.1        3.8        8.2        2.2
  due piedi       13.2        3.1        2.9        2.4        7.3

============================================================
Paziente 001
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 304 accettati / 118 scartati (28.0%)
  Stadio 1 riposo/attivo: 65.51% | score interno 69.37% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 68.45% | score interno 44.58% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 53.26%
  Tempo: 14.0s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 296 accettati / 126 scartati (29.9%)
  Stadio 1 riposo/attivo: 65.81% | score interno 70.83% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 57.74% | score interno 55.28% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 49.13%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 296 accettati / 126 scartati (29.9%)
  Stadio 1 riposo/attivo: 69.95% | score interno 62.53% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 64.29% | score interno 55.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 55.71%
  Tempo: 0.4s

  Paziente 001: 52.70% con 29.2% di scarti | Tempo: 31.1s

============================================================
Paziente 002
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 63.15% | score interno 68.23% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 62.50% | score interno 35.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.19%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 69.51% | score interno 65.67% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 47.64% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 46.58%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 64.22% | score interno 68.22% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 45.83% | score interno 46.25% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.31%
  Tempo: 0.4s

  Paziente 002: 43.02% con 28.0% di scarti | Tempo: 15.6s

============================================================
Paziente 003
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 305 accettati / 117 scartati (27.7%)
  Stadio 1 riposo/attivo: 58.78% | score interno 59.60% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.71% | score interno 19.44% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.09%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 333 accettati / 89 scartati (21.1%)
  Stadio 1 riposo/attivo: 54.02% | score interno 58.15% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 15.42% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 20.18%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 297 accettati / 125 scartati (29.6%)
  Stadio 1 riposo/attivo: 59.58% | score interno 55.97% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 24.40% | score interno 21.53% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 24.49%
  Tempo: 0.4s

  Paziente 003: 25.25% con 26.1% di scarti | Tempo: 15.8s

============================================================
Paziente 004
============================================================
  Run test: 12 + 14 | Threshold: 0.85 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 295 accettati / 121 scartati (29.1%)
  Stadio 1 riposo/attivo: 82.38% | score interno 90.84% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 51.79% | score interno 50.97% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 57.30%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 87.90% | score interno 86.26% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 63.69% | score interno 38.19% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 68.59%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 312 accettati / 104 scartati (25.0%)
  Stadio 1 riposo/attivo: 85.57% | score interno 85.21% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 60.71% | score interno 36.94% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 61.47%
  Tempo: 0.4s

  Paziente 004: 62.45% con 26.8% di scarti | Tempo: 15.6s

============================================================
Paziente 005
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 326 accettati / 90 scartati (21.6%)
  Stadio 1 riposo/attivo: 63.20% | score interno 66.68% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.36% | score interno 20.69% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.27%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 64.41% | score interno 66.33% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.98% | score interno 17.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.03%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 67.69% | score interno 66.78% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 18.75% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 32.55%
  Tempo: 0.4s

  Paziente 005: 28.95% con 22.9% di scarti | Tempo: 15.4s

============================================================
Paziente 006
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 53.83% | score interno 46.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.83% | score interno 19.58% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 18.16%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 50.48% | score interno 55.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 15.00% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.13%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 48.73% | score interno 50.73% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 23.81% | score interno 18.75% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 18.46%
  Tempo: 0.4s

  Paziente 006: 19.58% con 26.4% di scarti | Tempo: 15.4s

============================================================
Paziente 007
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 302 accettati / 120 scartati (28.4%)
  Stadio 1 riposo/attivo: 62.15% | score interno 74.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 75.60% | score interno 74.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 52.76%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 310 accettati / 112 scartati (26.5%)
  Stadio 1 riposo/attivo: 70.15% | score interno 72.07% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 85.12% | score interno 71.81% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 67.65%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 299 accettati / 123 scartati (29.1%)
  Stadio 1 riposo/attivo: 74.70% | score interno 65.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 77.98% | score interno 73.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 68.87%
  Tempo: 0.4s

  Paziente 007: 63.09% con 28.0% di scarti | Tempo: 16.4s

============================================================
Paziente 008
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 72.80% | score interno 64.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 55.36% | score interno 39.58% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 50.68%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 62.51% | score interno 70.07% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.67% | score interno 43.47% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 31.05%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 66.91% | score interno 67.54% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.98% | score interno 43.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.47%
  Tempo: 0.4s

  Paziente 008: 42.40% con 28.2% di scarti | Tempo: 15.5s

============================================================
Paziente 009
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 56.41% | score interno 59.31% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 19.44% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.98%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 50.06% | score interno 60.12% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 23.21% | score interno 19.58% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 17.84%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 59.21% | score interno 52.59% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 10.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.78%
  Tempo: 0.4s

  Paziente 009: 22.20% con 25.2% di scarti | Tempo: 15.4s

============================================================
Paziente 010
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 62.31% | score interno 60.96% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.69% | score interno 34.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.74%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 62.02% | score interno 62.14% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 40.48% | score interno 38.75% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 34.39%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 62.99% | score interno 64.23% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 46.43% | score interno 33.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 38.57%
  Tempo: 0.4s

  Paziente 010: 34.90% con 25.8% di scarti | Tempo: 15.9s

============================================================
Paziente 011
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 66.79% | score interno 60.98% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 26.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.21%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 64.33% | score interno 58.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 29.72% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.52%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 59.92% | score interno 63.01% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 28.06% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 27.61%
  Tempo: 0.5s

  Paziente 011: 30.11% con 25.1% di scarti | Tempo: 18.3s

============================================================
Paziente 012
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 78.49% | score interno 75.12% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 33.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 49.55%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 77.27% | score interno 74.17% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 50.00% | score interno 33.75% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 49.01%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 72.70% | score interno 75.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.26% | score interno 35.83% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 40.67%
  Tempo: 0.5s

  Paziente 012: 46.41% con 27.0% di scarti | Tempo: 18.1s

============================================================
Paziente 013
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 311 accettati / 105 scartati (25.2%)
  Stadio 1 riposo/attivo: 71.00% | score interno 71.13% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 54.76% | score interno 31.11% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 51.09%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 318 accettati / 98 scartati (23.6%)
  Stadio 1 riposo/attivo: 70.34% | score interno 72.03% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 33.75% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 41.13%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 72.78% | score interno 72.35% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 26.94% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 46.16%
  Tempo: 0.5s

  Paziente 013: 46.13% con 24.2% di scarti | Tempo: 18.6s

============================================================
Paziente 014
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 65.68% | score interno 61.34% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 25.56% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 29.06%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 65.32% | score interno 63.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 24.40% | score interno 24.72% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 21.17%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 61.63% | score interno 61.75% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 19.03% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.81%
  Tempo: 0.6s

  Paziente 014: 26.68% con 28.0% di scarti | Tempo: 19.8s

============================================================
Paziente 015
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 82.31% | score interno 84.61% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 58.93% | score interno 53.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 66.18%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.85 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 85.50% | score interno 83.20% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 54.76% | score interno 47.92% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 61.98%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 84.38% | score interno 82.47% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 51.19% | score interno 47.08% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 57.88%
  Tempo: 0.4s

  Paziente 015: 62.01% con 26.3% di scarti | Tempo: 18.7s

============================================================
Paziente 016
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 76.19% | score interno 63.19% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 15.97% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 38.51%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 65.51% | score interno 75.37% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.83% | score interno 21.25% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.92%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 75.39% | score interno 66.73% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 25.83% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.84%
  Tempo: 0.4s

  Paziente 016: 34.09% con 28.7% di scarti | Tempo: 17.8s

============================================================
Paziente 017
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 78.97% | score interno 72.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.19% | score interno 27.92% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 36.61%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 77.58% | score interno 73.90% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.14% | score interno 31.25% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 34.20%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 69.33% | score interno 79.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 20.83% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 27.62%
  Tempo: 0.5s

  Paziente 017: 32.81% con 25.8% di scarti | Tempo: 17.8s

============================================================
Paziente 018
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 320 accettati / 96 scartati (23.1%)
  Stadio 1 riposo/attivo: 67.52% | score interno 64.84% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.00% | score interno 14.03% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 26.06%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 65.23% | score interno 65.80% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 19.64% | score interno 15.28% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.08%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 69.82% | score interno 67.49% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 13.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.70%
  Tempo: 0.4s

  Paziente 018: 24.61% con 25.2% di scarti | Tempo: 17.5s

============================================================
Paziente 019
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 70.21% | score interno 63.34% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.33% | score interno 26.67% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.17%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 56.94% | score interno 67.82% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 35.71% | score interno 25.14% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 25.96%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 68.98% | score interno 64.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 24.31% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 37.31%
  Tempo: 0.4s

  Paziente 019: 31.48% con 28.2% di scarti | Tempo: 18.2s

============================================================
Paziente 020
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 69.91% | score interno 73.32% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.19% | score interno 20.83% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 32.45%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 67.83% | score interno 72.14% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 21.81% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 32.77%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 75.27% | score interno 70.63% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.14% | score interno 20.56% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 40.74%
  Tempo: 0.5s

  Paziente 020: 35.32% con 26.7% di scarti | Tempo: 17.7s

============================================================
Paziente 021
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 324 accettati / 98 scartati (23.2%)
  Stadio 1 riposo/attivo: 64.53% | score interno 57.20% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 37.50% | score interno 21.39% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.33%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 329 accettati / 93 scartati (22.0%)
  Stadio 1 riposo/attivo: 57.59% | score interno 64.96% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.38% | score interno 21.25% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.15%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 306 accettati / 116 scartati (27.5%)
  Stadio 1 riposo/attivo: 60.56% | score interno 63.48% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 22.02% | score interno 17.78% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.59%
  Tempo: 0.5s

  Paziente 021: 26.69% con 24.2% di scarti | Tempo: 19.2s

============================================================
Paziente 022
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 299 accettati / 123 scartati (29.1%)
  Stadio 1 riposo/attivo: 75.79% | score interno 81.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 21.43% | score interno 29.58% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.27%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 299 accettati / 123 scartati (29.1%)
  Stadio 1 riposo/attivo: 80.35% | score interno 78.83% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 24.40% | score interno 30.28% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 38.29%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 314 accettati / 108 scartati (25.6%)
  Stadio 1 riposo/attivo: 84.49% | score interno 75.72% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.14% | score interno 22.08% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 40.03%
  Tempo: 0.5s

  Paziente 022: 35.20% con 28.0% di scarti | Tempo: 18.2s

============================================================
Paziente 023
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 65.60% | score interno 71.06% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.10% | score interno 31.94% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 40.03%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 72.92% | score interno 69.00% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 33.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 35.77%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 72.08% | score interno 69.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.02% | score interno 27.22% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.27%
  Tempo: 0.5s

  Paziente 023: 40.36% con 25.9% di scarti | Tempo: 17.6s

============================================================
Paziente 024
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 70.52% | score interno 80.00% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 35.56% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 35.05%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 318 accettati / 98 scartati (23.6%)
  Stadio 1 riposo/attivo: 76.70% | score interno 78.35% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 37.50% | score interno 29.03% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 41.88%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 296 accettati / 120 scartati (28.8%)
  Stadio 1 riposo/attivo: 80.99% | score interno 71.49% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 31.11% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 41.07%
  Tempo: 0.5s

  Paziente 024: 39.33% con 26.2% di scarti | Tempo: 18.1s

============================================================
Paziente 025
============================================================
  Run test: 12 + 14 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 85.48% | score interno 84.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 43.45% | score interno 45.14% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 53.67%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 81.13% | score interno 83.32% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.98% | score interno 35.69% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 54.26%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 84.98% | score interno 83.53% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.38% | score interno 41.67% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 55.67%
  Tempo: 0.5s

  Paziente 025: 54.53% con 27.2% di scarti | Tempo: 19.2s

============================================================
Paziente 026
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 295 accettati / 121 scartati (29.1%)
  Stadio 1 riposo/attivo: 63.53% | score interno 66.40% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 31.25% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 30.60%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 62.52% | score interno 60.85% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 27.78% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.22%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 67.63% | score interno 62.20% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.71% | score interno 35.56% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 35.71%
  Tempo: 0.4s

  Paziente 026: 31.84% con 28.1% di scarti | Tempo: 17.9s

============================================================
Paziente 027
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 295 accettati / 121 scartati (29.1%)
  Stadio 1 riposo/attivo: 58.83% | score interno 64.26% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 16.67% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 23.78%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 331 accettati / 85 scartati (20.4%)
  Stadio 1 riposo/attivo: 64.52% | score interno 61.71% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 19.64% | score interno 26.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.16%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 60.90% | score interno 66.61% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 15.83% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.40%
  Tempo: 0.4s

  Paziente 027: 24.45% con 24.3% di scarti | Tempo: 17.6s

============================================================
Paziente 028
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 311 accettati / 105 scartati (25.2%)
  Stadio 1 riposo/attivo: 69.50% | score interno 73.95% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.83% | score interno 22.50% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 21.17%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 71.99% | score interno 67.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 20.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.53%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 73.02% | score interno 66.42% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 10.83% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.80%
  Tempo: 0.4s

  Paziente 028: 26.17% con 25.6% di scarti | Tempo: 17.8s

============================================================
Paziente 029
============================================================
  Run test: 12 + 14 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 295 accettati / 119 scartati (28.7%)
  Stadio 1 riposo/attivo: 80.10% | score interno 78.32% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 76.19% | score interno 68.06% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 79.24%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 297 accettati / 117 scartati (28.3%)
  Stadio 1 riposo/attivo: 76.17% | score interno 79.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 70.83% | score interno 72.22% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 65.92%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 312 accettati / 102 scartati (24.6%)
  Stadio 1 riposo/attivo: 81.07% | score interno 78.11% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 75.00% | score interno 63.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 75.41%
  Tempo: 0.5s

  Paziente 029: 73.52% con 27.2% di scarti | Tempo: 17.5s

============================================================
Paziente 030
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 316 accettati / 98 scartati (23.7%)
  Stadio 1 riposo/attivo: 73.30% | score interno 67.10% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 22.02% | score interno 26.53% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 28.12%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 312 accettati / 102 scartati (24.6%)
  Stadio 1 riposo/attivo: 72.12% | score interno 70.35% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 18.33% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 33.10%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 303 accettati / 111 scartati (26.8%)
  Stadio 1 riposo/attivo: 70.02% | score interno 67.26% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.33% | score interno 15.69% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 33.99%
  Tempo: 0.5s

  Paziente 030: 31.74% con 25.0% di scarti | Tempo: 18.0s

============================================================
Paziente 031
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 65.54% | score interno 67.43% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.31% | score interno 32.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.22%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 62.95% | score interno 70.59% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 40.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 40.23%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 316 accettati / 100 scartati (24.0%)
  Stadio 1 riposo/attivo: 68.83% | score interno 62.52% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 53.57% | score interno 40.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 46.54%
  Tempo: 0.4s

  Paziente 031: 39.33% con 25.5% di scarti | Tempo: 18.0s

============================================================
Paziente 032
============================================================
  Run test: 12 + 14 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 301 accettati / 121 scartati (28.7%)
  Stadio 1 riposo/attivo: 80.73% | score interno 87.38% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.31% | score interno 53.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 39.19%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.85 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 300 accettati / 122 scartati (28.9%)
  Stadio 1 riposo/attivo: 91.01% | score interno 84.42% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.98% | score interno 31.53% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 58.38%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.85 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 306 accettati / 116 scartati (27.5%)
  Stadio 1 riposo/attivo: 85.77% | score interno 87.16% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 39.88% | score interno 38.75% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 53.18%
  Tempo: 0.5s

  Paziente 032: 50.25% con 28.4% di scarti | Tempo: 18.3s

============================================================
Paziente 033
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 73.23% | score interno 82.96% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 44.05% | score interno 30.56% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 39.60%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 80.04% | score interno 76.25% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 37.50% | score interno 25.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 40.83%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 84.21% | score interno 76.20% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.07% | score interno 32.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.81%
  Tempo: 0.5s

  Paziente 033: 42.08% con 26.4% di scarti | Tempo: 17.4s

============================================================
Paziente 034
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 306 accettati / 108 scartati (26.1%)
  Stadio 1 riposo/attivo: 66.19% | score interno 71.97% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 63.69% | score interno 48.47% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 42.17%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 301 accettati / 113 scartati (27.3%)
  Stadio 1 riposo/attivo: 70.19% | score interno 69.44% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 55.36% | score interno 58.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 43.09%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 302 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 72.57% | score interno 67.18% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 58.93% | score interno 43.89% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.69%
  Tempo: 0.5s

  Paziente 034: 43.65% con 26.9% di scarti | Tempo: 19.3s

============================================================
Paziente 035
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 299 accettati / 123 scartati (29.1%)
  Stadio 1 riposo/attivo: 77.96% | score interno 79.11% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 58.93% | score interno 58.06% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 58.06%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 308 accettati / 114 scartati (27.0%)
  Stadio 1 riposo/attivo: 78.75% | score interno 79.25% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 50.00% | score interno 63.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 48.04%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 323 accettati / 99 scartati (23.5%)
  Stadio 1 riposo/attivo: 73.02% | score interno 78.46% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 57.14% | score interno 61.53% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 47.25%
  Tempo: 0.5s

  Paziente 035: 51.12% con 26.5% di scarti | Tempo: 17.9s

============================================================
Paziente 036
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 79.31% | score interno 77.98% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 22.36% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 37.32%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 78.00% | score interno 76.52% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 26.67% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 37.47%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 82.30% | score interno 79.40% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 25.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 41.81%
  Tempo: 0.4s

  Paziente 036: 38.87% con 28.0% di scarti | Tempo: 17.5s

============================================================
Paziente 037
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 299 accettati / 115 scartati (27.8%)
  Stadio 1 riposo/attivo: 65.99% | score interno 71.01% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 18.06% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.99%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 301 accettati / 113 scartati (27.3%)
  Stadio 1 riposo/attivo: 77.04% | score interno 61.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 18.47% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 33.43%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 322 accettati / 93 scartati (22.4%)
  Stadio 1 riposo/attivo: 63.07% | score interno 72.55% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 18.75% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.97%
  Tempo: 0.4s

  Paziente 037: 27.13% con 25.8% di scarti | Tempo: 17.2s

============================================================
Paziente 038
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 47.14% | score interno 51.42% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 18.45% | score interno 18.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 16.03%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 49.54% | score interno 49.16% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 20.83% | score interno 14.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 19.01%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 316 accettati / 100 scartati (24.0%)
  Stadio 1 riposo/attivo: 52.13% | score interno 48.65% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 17.86% | score interno 14.03% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 19.71%
  Tempo: 0.4s

  Paziente 038: 18.25% con 26.6% di scarti | Tempo: 17.8s

============================================================
Paziente 039
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 324 accettati / 92 scartati (22.1%)
  Stadio 1 riposo/attivo: 49.11% | score interno 54.65% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.00% | score interno 20.69% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 20.39%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 312 accettati / 104 scartati (25.0%)
  Stadio 1 riposo/attivo: 57.55% | score interno 45.93% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 23.21% | score interno 19.17% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 20.83%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 311 accettati / 105 scartati (25.2%)
  Stadio 1 riposo/attivo: 50.95% | score interno 52.54% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 22.02% | score interno 18.75% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 18.74%
  Tempo: 0.4s

  Paziente 039: 19.98% con 24.1% di scarti | Tempo: 17.7s

============================================================
Paziente 040
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 311 accettati / 105 scartati (25.2%)
  Stadio 1 riposo/attivo: 54.81% | score interno 64.39% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 32.14% | score interno 19.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.86%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 333 accettati / 83 scartati (20.0%)
  Stadio 1 riposo/attivo: 61.31% | score interno 59.58% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 20.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 24.99%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 65.34% | score interno 57.32% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.36% | score interno 24.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.09%
  Tempo: 0.5s

  Paziente 040: 25.98% con 24.3% di scarti | Tempo: 17.8s

============================================================
Paziente 041
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 494 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 70.24% | score interno 65.28% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 40.48% | score interno 28.75% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 39.93%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 495 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 306 accettati / 109 scartati (26.3%)
  Stadio 1 riposo/attivo: 61.16% | score interno 67.75% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.67% | score interno 35.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.75%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 495 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 320 accettati / 95 scartati (22.9%)
  Stadio 1 riposo/attivo: 69.34% | score interno 63.11% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.07% | score interno 26.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.05%
  Tempo: 0.4s

  Paziente 041: 36.91% con 25.7% di scarti | Tempo: 17.7s

============================================================
Paziente 042
============================================================
  Run test: 12 + 14 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 78.50% | score interno 75.44% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 83.93% | score interno 70.83% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 78.11%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 80.70% | score interno 77.11% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 84.52% | score interno 75.97% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 78.74%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 75.00% | score interno 80.14% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 71.43% | score interno 83.89% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 69.78%
  Tempo: 0.5s

  Paziente 042: 75.54% con 28.3% di scarti | Tempo: 18.2s

============================================================
Paziente 043
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 78.73% | score interno 81.78% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 53.57% | score interno 47.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 53.56%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 83.32% | score interno 77.42% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 60.12% | score interno 38.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 60.27%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 80.96% | score interno 77.71% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 38.69% | score interno 54.58% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.41%
  Tempo: 0.5s

  Paziente 043: 53.08% con 26.8% di scarti | Tempo: 17.6s

============================================================
Paziente 044
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 66.29% | score interno 62.33% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.10% | score interno 27.92% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.28%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 59.92% | score interno 65.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 44.05% | score interno 23.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 34.58%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 65.90% | score interno 61.85% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.24% | score interno 27.36% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 35.36%
  Tempo: 0.5s

  Paziente 044: 35.41% con 27.2% di scarti | Tempo: 17.6s

============================================================
Paziente 045
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 77.79% | score interno 83.54% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 46.43% | score interno 30.56% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 46.59%
  Tempo: 0.6s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 85.00% | score interno 78.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 43.45% | score interno 34.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 54.97%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 79.81% | score interno 81.79% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.07% | score interno 34.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 42.92%
  Tempo: 0.4s

  Paziente 045: 48.16% con 27.1% di scarti | Tempo: 17.3s

============================================================
Paziente 046
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 314 accettati / 108 scartati (25.6%)
  Stadio 1 riposo/attivo: 69.65% | score interno 69.98% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 30.28% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 32.32%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 296 accettati / 126 scartati (29.9%)
  Stadio 1 riposo/attivo: 62.24% | score interno 74.30% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.31% | score interno 22.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 34.26%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 319 accettati / 103 scartati (24.4%)
  Stadio 1 riposo/attivo: 73.80% | score interno 69.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.07% | score interno 32.22% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 39.76%
  Tempo: 0.4s

  Paziente 046: 35.44% con 26.6% di scarti | Tempo: 17.6s

============================================================
Paziente 047
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 56.76% | score interno 53.96% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.00% | score interno 22.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 21.16%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 56.42% | score interno 54.18% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 22.62% | score interno 14.44% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 20.59%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 321 accettati / 95 scartati (22.8%)
  Stadio 1 riposo/attivo: 53.63% | score interno 56.50% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 23.81% | score interno 20.83% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 21.05%
  Tempo: 0.5s

  Paziente 047: 20.93% con 26.4% di scarti | Tempo: 17.9s

============================================================
Paziente 048
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 73.79% | score interno 77.93% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.62% | score interno 42.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.63%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 78.39% | score interno 76.62% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 41.67% | score interno 43.19% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 46.99%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 80.01% | score interno 78.80% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 49.40% | score interno 35.28% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 49.61%
  Tempo: 0.5s

  Paziente 048: 47.41% con 26.9% di scarti | Tempo: 17.7s

============================================================
Paziente 049
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 71.24% | score interno 74.44% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.02% | score interno 46.53% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 41.29%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 71.54% | score interno 71.52% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.83% | score interno 38.06% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 41.54%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 326 accettati / 90 scartati (21.6%)
  Stadio 1 riposo/attivo: 72.62% | score interno 73.71% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 46.43% | score interno 40.42% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 47.38%
  Tempo: 0.4s

  Paziente 049: 43.40% con 26.4% di scarti | Tempo: 17.6s

============================================================
Paziente 050
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 87.17% | score interno 77.72% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 31.11% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 41.02%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 73.41% | score interno 84.57% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 24.72% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 33.69%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 82.22% | score interno 78.66% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 23.21% | score interno 29.86% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 32.76%
  Tempo: 0.5s

  Paziente 050: 35.82% con 28.0% di scarti | Tempo: 17.4s

============================================================
Paziente 051
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 77.00% | score interno 72.33% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.71% | score interno 15.97% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 40.34%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 77.49% | score interno 71.85% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.00% | score interno 18.47% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 32.90%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 77.20% | score interno 73.38% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 19.05% | score interno 20.14% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 32.32%
  Tempo: 0.5s

  Paziente 051: 35.19% con 26.4% di scarti | Tempo: 18.0s

============================================================
Paziente 052
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 71.21% | score interno 69.03% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 41.07% | score interno 43.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 35.61%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 65.04% | score interno 73.23% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 41.53% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 25.08%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 74.91% | score interno 69.46% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 53.57% | score interno 25.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 50.18%
  Tempo: 0.4s

  Paziente 052: 36.95% con 26.0% di scarti | Tempo: 17.5s

============================================================
Paziente 053
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 316 accettati / 100 scartati (24.0%)
  Stadio 1 riposo/attivo: 64.40% | score interno 65.02% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 26.94% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.22%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 69.00% | score interno 58.96% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 25.69% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 30.81%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 62.90% | score interno 65.43% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.93% | score interno 34.03% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.87%
  Tempo: 0.4s

  Paziente 053: 29.97% con 24.9% di scarti | Tempo: 18.1s

============================================================
Paziente 054
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 72.07% | score interno 78.77% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 49.40% | score interno 43.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 49.70%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 73.71% | score interno 75.99% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 55.95% | score interno 37.64% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 53.30%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 81.68% | score interno 71.77% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 51.19% | score interno 45.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 54.75%
  Tempo: 0.5s

  Paziente 054: 52.58% con 27.2% di scarti | Tempo: 17.8s

============================================================
Paziente 055
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 79.00% | score interno 79.52% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.98% | score interno 39.86% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 49.68%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 80.71% | score interno 81.52% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.86% | score interno 30.56% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 40.01%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 74.83% | score interno 81.11% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 40.48% | score interno 39.03% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 38.48%
  Tempo: 0.5s

  Paziente 055: 42.72% con 28.3% di scarti | Tempo: 17.6s

============================================================
Paziente 056
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 70.09% | score interno 76.67% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 53.57% | score interno 43.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 47.18%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 302 accettati / 114 scartati (27.4%)
  Stadio 1 riposo/attivo: 78.07% | score interno 76.64% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 55.95% | score interno 42.50% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 57.54%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 79.36% | score interno 73.50% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.26% | score interno 41.11% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 44.22%
  Tempo: 0.4s

  Paziente 056: 49.65% con 26.4% di scarti | Tempo: 17.8s

============================================================
Paziente 057
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 298 accettati / 124 scartati (29.4%)
  Stadio 1 riposo/attivo: 62.43% | score interno 60.17% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 17.86% | score interno 30.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 19.72%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 316 accettati / 106 scartati (25.1%)
  Stadio 1 riposo/attivo: 58.79% | score interno 63.13% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 28.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 21.11%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 321 accettati / 101 scartati (23.9%)
  Stadio 1 riposo/attivo: 58.30% | score interno 58.16% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 33.33% | score interno 14.58% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.22%
  Tempo: 0.4s

  Paziente 057: 22.35% con 26.1% di scarti | Tempo: 18.0s

============================================================
Paziente 058
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 75.60% | score interno 71.12% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 42.26% | score interno 35.97% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 43.32%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 74.51% | score interno 74.68% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.31% | score interno 31.67% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 35.70%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 306 accettati / 110 scartati (26.4%)
  Stadio 1 riposo/attivo: 73.73% | score interno 70.74% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 38.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.94%
  Tempo: 0.5s

  Paziente 058: 37.65% con 27.9% di scarti | Tempo: 17.7s

============================================================
Paziente 059
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 63.62% | score interno 66.38% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 24.72% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.88%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 70.03% | score interno 64.22% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 30.00% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 34.64%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 63.12% | score interno 61.53% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 36.31% | score interno 14.44% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.71%
  Tempo: 0.5s

  Paziente 059: 30.74% con 28.0% di scarti | Tempo: 18.2s

============================================================
Paziente 060
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 68.20% | score interno 70.09% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 51.79% | score interno 45.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 46.77%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 62.43% | score interno 73.51% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.26% | score interno 46.94% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 35.84%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 71.76% | score interno 68.09% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 44.64% | score interno 41.81% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 41.66%
  Tempo: 0.5s

  Paziente 060: 41.43% con 26.4% di scarti | Tempo: 17.6s

============================================================
Paziente 061
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 325 accettati / 97 scartati (23.0%)
  Stadio 1 riposo/attivo: 65.39% | score interno 53.98% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 31.25% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.16%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 59.17% | score interno 60.29% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 35.12% | score interno 27.50% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 25.37%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 328 accettati / 94 scartati (22.3%)
  Stadio 1 riposo/attivo: 53.93% | score interno 66.10% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 26.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 26.77%
  Tempo: 0.5s

  Paziente 061: 26.10% con 23.9% di scarti | Tempo: 17.9s

============================================================
Paziente 062
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 71.53% | score interno 68.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 67.86% | score interno 77.08% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 62.13%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 75.20% | score interno 67.66% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 81.55% | score interno 62.08% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 73.01%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 68.10% | score interno 72.02% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 77.98% | score interno 68.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 61.36%
  Tempo: 0.5s

  Paziente 062: 65.50% con 26.9% di scarti | Tempo: 18.0s

============================================================
Paziente 063
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 318 accettati / 98 scartati (23.6%)
  Stadio 1 riposo/attivo: 69.42% | score interno 72.56% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 23.21% | score interno 22.22% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 27.58%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 71.62% | score interno 70.01% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 22.02% | score interno 20.69% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 26.12%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 73.19% | score interno 68.80% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.38% | score interno 21.25% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 27.90%
  Tempo: 0.4s

  Paziente 063: 27.20% con 26.8% di scarti | Tempo: 17.2s

============================================================
Paziente 064
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 495 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 299 accettati / 115 scartati (27.8%)
  Stadio 1 riposo/attivo: 66.80% | score interno 68.90% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 19.17% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.90%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 494 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 296 accettati / 119 scartati (28.7%)
  Stadio 1 riposo/attivo: 73.06% | score interno 70.75% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 25.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.05%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 74.61% | score interno 68.61% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.00% | score interno 18.06% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.13%
  Tempo: 0.5s

  Paziente 064: 30.70% con 27.7% di scarti | Tempo: 17.6s

============================================================
Paziente 065
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 296 accettati / 126 scartati (29.9%)
  Stadio 1 riposo/attivo: 75.31% | score interno 67.23% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.83% | score interno 28.75% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 49.17%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 309 accettati / 113 scartati (26.8%)
  Stadio 1 riposo/attivo: 72.74% | score interno 69.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.86% | score interno 25.14% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 48.18%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 67.48% | score interno 70.82% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.10% | score interno 36.39% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 32.03%
  Tempo: 0.5s

  Paziente 065: 43.13% con 27.6% di scarti | Tempo: 17.8s

============================================================
Paziente 066
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 305 accettati / 117 scartati (27.7%)
  Stadio 1 riposo/attivo: 59.57% | score interno 61.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.98% | score interno 17.36% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 25.89%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 305 accettati / 117 scartati (27.7%)
  Stadio 1 riposo/attivo: 63.03% | score interno 61.92% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 22.22% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 32.38%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 316 accettati / 106 scartati (25.1%)
  Stadio 1 riposo/attivo: 64.41% | score interno 59.83% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 19.05% | score interno 18.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 24.71%
  Tempo: 0.5s

  Paziente 066: 27.66% con 26.9% di scarti | Tempo: 17.4s

============================================================
Paziente 067
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 60.29% | score interno 59.78% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 21.25% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 29.17%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 61.12% | score interno 57.47% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 17.36% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.88%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 58.50% | score interno 58.51% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 20.83% | score interno 23.19% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.33%
  Tempo: 0.4s

  Paziente 067: 24.79% con 26.0% di scarti | Tempo: 17.1s

============================================================
Paziente 068
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 80.29% | score interno 77.70% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.98% | score interno 36.11% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.42%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 80.29% | score interno 78.28% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.24% | score interno 29.72% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 52.76%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 305 accettati / 111 scartati (26.7%)
  Stadio 1 riposo/attivo: 76.08% | score interno 79.74% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.26% | score interno 30.69% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 48.72%
  Tempo: 0.4s

  Paziente 068: 45.97% con 27.5% di scarti | Tempo: 17.3s

============================================================
Paziente 069
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 81.78% | score interno 84.73% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 26.39% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 39.10%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 85.17% | score interno 83.68% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 28.33% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 40.68%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 88.10% | score interno 81.66% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 25.14% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 41.35%
  Tempo: 0.4s

  Paziente 069: 40.38% con 26.3% di scarti | Tempo: 17.2s

============================================================
Paziente 070
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 60.63% | score interno 61.27% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 54.76% | score interno 45.97% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 41.40%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 66.14% | score interno 64.58% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 57.14% | score interno 44.86% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 48.65%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 65.72% | score interno 61.81% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 51.19% | score interno 47.92% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.47%
  Tempo: 0.4s

  Paziente 070: 42.51% con 24.9% di scarti | Tempo: 17.3s

============================================================
Paziente 071
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 316 accettati / 106 scartati (25.1%)
  Stadio 1 riposo/attivo: 57.00% | score interno 66.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 50.00% | score interno 44.03% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.09%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 318 accettati / 104 scartati (24.6%)
  Stadio 1 riposo/attivo: 62.92% | score interno 62.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.24% | score interno 41.94% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 45.49%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 303 accettati / 119 scartati (28.2%)
  Stadio 1 riposo/attivo: 63.14% | score interno 66.57% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 45.24% | score interno 38.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 38.88%
  Tempo: 0.5s

  Paziente 071: 39.15% con 26.0% di scarti | Tempo: 18.2s

============================================================
Paziente 072
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 305 accettati / 110 scartati (26.5%)
  Stadio 1 riposo/attivo: 68.87% | score interno 70.79% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 68.45% | score interno 62.36% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 50.19%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 315 accettati / 99 scartati (23.9%)
  Stadio 1 riposo/attivo: 70.50% | score interno 69.06% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 62.50% | score interno 71.81% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 57.30%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 299 accettati / 115 scartati (27.8%)
  Stadio 1 riposo/attivo: 73.14% | score interno 68.02% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 76.19% | score interno 54.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 62.10%
  Tempo: 0.5s

  Paziente 072: 56.53% con 26.1% di scarti | Tempo: 17.9s

============================================================
Paziente 073
============================================================
  Run test: 12 + 14 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 309 accettati / 105 scartati (25.4%)
  Stadio 1 riposo/attivo: 79.28% | score interno 82.34% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 44.64% | score interno 43.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 56.49%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.85 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 303 accettati / 111 scartati (26.8%)
  Stadio 1 riposo/attivo: 85.09% | score interno 83.66% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 42.86% | score interno 45.14% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 54.61%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 295 accettati / 119 scartati (28.7%)
  Stadio 1 riposo/attivo: 82.83% | score interno 80.06% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.38% | score interno 28.06% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 52.90%
  Tempo: 0.5s

  Paziente 073: 54.67% con 27.0% di scarti | Tempo: 17.5s

============================================================
Paziente 074
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 316 accettati / 98 scartati (23.7%)
  Stadio 1 riposo/attivo: 59.84% | score interno 58.72% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 22.92% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 23.44%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 305 accettati / 109 scartati (26.3%)
  Stadio 1 riposo/attivo: 62.58% | score interno 53.57% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 15.48% | score interno 25.56% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 20.82%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 303 accettati / 112 scartati (27.0%)
  Stadio 1 riposo/attivo: 60.33% | score interno 54.23% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 35.12% | score interno 16.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.85%
  Tempo: 0.4s

  Paziente 074: 24.71% con 25.7% di scarti | Tempo: 17.6s

============================================================
Paziente 075
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 54.92% | score interno 68.56% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 39.29% | score interno 20.83% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 29.63%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 321 accettati / 95 scartati (22.8%)
  Stadio 1 riposo/attivo: 62.93% | score interno 58.00% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.98% | score interno 38.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.84%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 312 accettati / 104 scartati (25.0%)
  Stadio 1 riposo/attivo: 65.21% | score interno 58.05% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 31.11% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.15%
  Tempo: 0.4s

  Paziente 075: 28.21% con 24.5% di scarti | Tempo: 18.1s

============================================================
Paziente 076
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 308 accettati / 106 scartati (25.6%)
  Stadio 1 riposo/attivo: 60.14% | score interno 57.70% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.24% | score interno 25.97% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 22.41%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 308 accettati / 106 scartati (25.6%)
  Stadio 1 riposo/attivo: 60.94% | score interno 55.68% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 11.31% | score interno 14.31% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 19.04%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 307 accettati / 107 scartati (25.8%)
  Stadio 1 riposo/attivo: 58.01% | score interno 56.87% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 20.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 20.81%
  Tempo: 0.4s

  Paziente 076: 20.75% con 25.7% di scarti | Tempo: 18.0s

============================================================
Paziente 077
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 323 accettati / 93 scartati (22.4%)
  Stadio 1 riposo/attivo: 61.99% | score interno 55.67% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 23.81% | score interno 20.00% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.55%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 299 accettati / 117 scartati (28.1%)
  Stadio 1 riposo/attivo: 56.13% | score interno 62.57% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 22.62% | score interno 15.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 21.17%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 64.72% | score interno 60.58% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.74% | score interno 15.42% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 28.33%
  Tempo: 0.4s

  Paziente 077: 24.68% con 25.0% di scarti | Tempo: 18.2s

============================================================
Paziente 078
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 310 accettati / 106 scartati (25.5%)
  Stadio 1 riposo/attivo: 55.55% | score interno 52.65% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 18.45% | score interno 14.44% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 18.73%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 56.90% | score interno 52.78% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 22.02% | score interno 26.11% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 20.83%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 316 accettati / 100 scartati (24.0%)
  Stadio 1 riposo/attivo: 51.77% | score interno 58.89% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.17% | score interno 12.22% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 23.33%
  Tempo: 0.4s

  Paziente 078: 20.96% con 25.5% di scarti | Tempo: 17.8s

============================================================
Paziente 079
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 309 accettati / 113 scartati (26.8%)
  Stadio 1 riposo/attivo: 55.34% | score interno 55.42% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 32.14% | score interno 25.42% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.88%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 296 accettati / 126 scartati (29.9%)
  Stadio 1 riposo/attivo: 56.02% | score interno 58.75% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 29.76% | score interno 26.67% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.04%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 314 accettati / 108 scartati (25.6%)
  Stadio 1 riposo/attivo: 56.69% | score interno 54.78% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 30.95% | score interno 27.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.01%
  Tempo: 0.5s

  Paziente 079: 28.64% con 27.4% di scarti | Tempo: 17.8s

============================================================
Paziente 080
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 296 accettati / 120 scartati (28.8%)
  Stadio 1 riposo/attivo: 76.08% | score interno 71.97% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.10% | score interno 22.78% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 35.07%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 296 accettati / 120 scartati (28.8%)
  Stadio 1 riposo/attivo: 71.96% | score interno 70.38% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.36% | score interno 28.75% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 34.06%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 66.72% | score interno 74.53% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 25.56% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 26.07%
  Tempo: 0.4s

  Paziente 080: 31.73% con 28.8% di scarti | Tempo: 17.8s

============================================================
Paziente 081
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 321 accettati / 95 scartati (22.8%)
  Stadio 1 riposo/attivo: 72.40% | score interno 72.03% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 23.61% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 39.50%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 70.12% | score interno 77.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 19.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.54%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 77.91% | score interno 68.95% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 38.69% | score interno 27.50% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 43.05%
  Tempo: 0.5s

  Paziente 081: 39.70% con 25.1% di scarti | Tempo: 18.6s

============================================================
Paziente 082
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 59.50% | score interno 64.29% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 39.29% | score interno 30.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 30.56%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 63.83% | score interno 65.19% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.33% | score interno 29.86% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 33.97%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 319 accettati / 97 scartati (23.3%)
  Stadio 1 riposo/attivo: 69.39% | score interno 62.17% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 39.29% | score interno 29.17% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 34.74%
  Tempo: 0.5s

  Paziente 082: 33.09% con 26.0% di scarti | Tempo: 17.8s

============================================================
Paziente 083
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 308 accettati / 114 scartati (27.0%)
  Stadio 1 riposo/attivo: 66.10% | score interno 73.18% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.98% | score interno 32.92% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 27.81%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 318 accettati / 104 scartati (24.6%)
  Stadio 1 riposo/attivo: 67.59% | score interno 67.70% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 37.50% | score interno 25.14% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 36.89%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 302 accettati / 120 scartati (28.4%)
  Stadio 1 riposo/attivo: 72.72% | score interno 64.59% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 25.69% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.67%
  Tempo: 0.4s

  Paziente 083: 34.12% con 26.7% di scarti | Tempo: 17.8s

============================================================
Paziente 084
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 70.42% | score interno 69.01% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 32.14% | score interno 29.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.25%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 321 accettati / 95 scartati (22.8%)
  Stadio 1 riposo/attivo: 65.94% | score interno 68.30% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.93% | score interno 28.47% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.27%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 311 accettati / 105 scartati (25.2%)
  Stadio 1 riposo/attivo: 66.61% | score interno 66.25% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.38% | score interno 30.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 26.46%
  Tempo: 0.4s

  Paziente 084: 30.66% con 24.2% di scarti | Tempo: 17.5s

============================================================
Paziente 085
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 75.97% | score interno 66.74% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 64.88% | score interno 53.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 62.42%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 74.68% | score interno 71.81% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 67.26% | score interno 48.06% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 60.68%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 296 accettati / 120 scartati (28.8%)
  Stadio 1 riposo/attivo: 64.53% | score interno 75.61% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 55.95% | score interno 61.11% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 43.96%
  Tempo: 0.5s

  Paziente 085: 55.69% con 26.8% di scarti | Tempo: 17.7s

============================================================
Paziente 086
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 301 accettati / 121 scartati (28.7%)
  Stadio 1 riposo/attivo: 73.61% | score interno 78.57% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 58.93% | score interno 32.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 52.48%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 299 accettati / 123 scartati (29.1%)
  Stadio 1 riposo/attivo: 80.84% | score interno 76.29% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 44.64% | score interno 49.72% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 42.45%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 80.75% | score interno 77.15% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 46.43% | score interno 53.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 51.49%
  Tempo: 0.5s

  Paziente 086: 48.81% con 28.0% di scarti | Tempo: 17.8s

============================================================
Paziente 087
============================================================
  Run test: 12 + 14 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 327 accettati / 89 scartati (21.4%)
  Stadio 1 riposo/attivo: 47.62% | score interno 58.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 31.55% | score interno 19.17% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 20.04%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 50.84% | score interno 52.90% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 24.40% | score interno 27.92% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.15%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 49.04% | score interno 47.98% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 24.40% | score interno 22.50% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.93%
  Tempo: 0.4s

  Paziente 087: 22.04% con 26.8% di scarti | Tempo: 17.5s

============================================================
Paziente 088
============================================================
  Run test: 12 + 14 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 272 accettati / 94 scartati (25.7%)
  Stadio 1 riposo/attivo: 59.39% | score interno 46.53% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 26.04% | score interno 17.40% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.02%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.45 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 278 accettati / 88 scartati (24.0%)
  Stadio 1 riposo/attivo: 54.37% | score interno 59.36% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.43% | score interno 17.55% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 24.80%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 283 accettati / 83 scartati (22.7%)
  Stadio 1 riposo/attivo: 58.04% | score interno 57.34% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 25.69% | score interno 15.16% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.99%
  Tempo: 0.5s

  Paziente 088: 23.94% con 24.1% di scarti | Tempo: 14.4s

============================================================
Paziente 089
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 81.00% | score interno 78.92% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 30.14% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 41.98%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.75 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 79.60% | score interno 78.37% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 48.81% | score interno 30.97% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 51.47%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 315 accettati / 101 scartati (24.3%)
  Stadio 1 riposo/attivo: 76.18% | score interno 79.08% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.12% | score interno 35.83% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.90%
  Tempo: 0.5s

  Paziente 089: 43.45% con 25.4% di scarti | Tempo: 18.1s

============================================================
Paziente 090
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 69.59% | score interno 65.49% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 33.33% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.91%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 292 accettati / 124 scartati (29.8%)
  Stadio 1 riposo/attivo: 64.91% | score interno 69.16% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 20.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.18%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 314 accettati / 102 scartati (24.5%)
  Stadio 1 riposo/attivo: 70.52% | score interno 65.10% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 24.03% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 27.75%
  Tempo: 0.5s

  Paziente 090: 30.95% con 26.0% di scarti | Tempo: 17.2s

============================================================
Paziente 091
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 60.64% | score interno 65.05% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.71% | score interno 27.64% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 32.34%
  Tempo: 0.6s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 69.52% | score interno 64.63% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.19% | score interno 28.75% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 28.40%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 67.74% | score interno 63.42% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 35.71% | score interno 24.17% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 31.27%
  Tempo: 0.5s

  Paziente 091: 30.67% con 26.1% di scarti | Tempo: 19.6s

============================================================
Paziente 092
============================================================
  Run test: 12 + 14 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 266 accettati / 100 scartati (27.3%)
  Stadio 1 riposo/attivo: 61.42% | score interno 64.35% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 31.94% | score interno 23.07% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.99%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 267 accettati / 99 scartati (27.0%)
  Stadio 1 riposo/attivo: 60.66% | score interno 55.15% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 32.99% | score interno 23.28% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.85%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 156 finestre di riposo / 576 di movimento
  Campioni: 366 tot / 271 accettati / 95 scartati (26.0%)
  Stadio 1 riposo/attivo: 53.34% | score interno 65.54% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 34.72% | score interno 23.07% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 21.59%
  Tempo: 0.6s

  Paziente 092: 26.15% con 26.8% di scarti | Tempo: 17.3s

============================================================
Paziente 093
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 324 accettati / 92 scartati (22.1%)
  Stadio 1 riposo/attivo: 57.83% | score interno 57.59% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 52.38% | score interno 46.39% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.25%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 296 accettati / 120 scartati (28.8%)
  Stadio 1 riposo/attivo: 54.83% | score interno 60.09% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 47.02% | score interno 52.78% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.71%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 58.63% | score interno 62.47% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 55.95% | score interno 42.36% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 35.98%
  Tempo: 0.5s

  Paziente 093: 35.31% con 26.4% di scarti | Tempo: 20.3s

============================================================
Paziente 094
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 61.04% | score interno 66.00% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 61.31% | score interno 59.86% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 50.02%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 293 accettati / 123 scartati (29.6%)
  Stadio 1 riposo/attivo: 69.00% | score interno 62.71% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 68.45% | score interno 48.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 54.46%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 309 accettati / 107 scartati (25.7%)
  Stadio 1 riposo/attivo: 63.92% | score interno 62.98% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 70.83% | score interno 53.19% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 46.96%
  Tempo: 0.5s

  Paziente 094: 50.48% con 26.4% di scarti | Tempo: 17.7s

============================================================
Paziente 095
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 65.60% | score interno 48.72% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 36.31% | score interno 28.61% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 33.00%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 328 accettati / 94 scartati (22.3%)
  Stadio 1 riposo/attivo: 66.01% | score interno 57.06% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 40.48% | score interno 30.69% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 36.74%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 319 accettati / 103 scartati (24.4%)
  Stadio 1 riposo/attivo: 55.62% | score interno 63.86% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 33.93% | score interno 31.67% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 25.64%
  Tempo: 0.5s

  Paziente 095: 31.79% con 24.3% di scarti | Tempo: 17.9s

============================================================
Paziente 096
============================================================
  Run test: 12 + 14 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 342 accettati / 80 scartati (19.0%)
  Stadio 1 riposo/attivo: 55.93% | score interno 60.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.83% | score interno 26.67% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 22.08%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 326 accettati / 96 scartati (22.7%)
  Stadio 1 riposo/attivo: 58.87% | score interno 54.65% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 23.21% | score interno 22.08% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 21.93%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 317 accettati / 105 scartati (24.9%)
  Stadio 1 riposo/attivo: 60.08% | score interno 59.58% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 21.43% | score interno 21.94% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 19.83%
  Tempo: 0.5s

  Paziente 096: 21.28% con 22.2% di scarti | Tempo: 17.9s

============================================================
Paziente 097
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 66.60% | score interno 57.61% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 30.95% | score interno 30.42% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 29.77%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 61.65% | score interno 62.17% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 20.83% | score interno 25.00% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 24.12%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 322 accettati / 94 scartati (22.6%)
  Stadio 1 riposo/attivo: 60.64% | score interno 59.95% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 20.83% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 30.70%
  Tempo: 0.4s

  Paziente 097: 28.20% con 24.1% di scarti | Tempo: 17.5s

============================================================
Paziente 098
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 331 accettati / 85 scartati (20.4%)
  Stadio 1 riposo/attivo: 69.20% | score interno 67.74% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 19.64% | score interno 35.00% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 23.08%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 303 accettati / 113 scartati (27.2%)
  Stadio 1 riposo/attivo: 68.46% | score interno 67.16% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 23.21% | score interno 25.83% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 27.24%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 74.81% | score interno 64.11% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 36.90% | score interno 21.39% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 36.08%
  Tempo: 0.5s

  Paziente 098: 28.80% con 25.6% di scarti | Tempo: 18.0s

============================================================
Paziente 099
============================================================
  Run test: 12 + 14 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 337 accettati / 79 scartati (19.0%)
  Stadio 1 riposo/attivo: 49.55% | score interno 53.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.19% | score interno 19.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 19.50%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 308 accettati / 108 scartati (26.0%)
  Stadio 1 riposo/attivo: 52.80% | score interno 58.21% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 20.83% | score interno 22.64% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 22.45%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 300 accettati / 116 scartati (27.9%)
  Stadio 1 riposo/attivo: 59.00% | score interno 44.11% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.95% | score interno 20.28% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 28.04%
  Tempo: 0.4s

  Paziente 099: 23.33% con 24.3% di scarti | Tempo: 18.1s

============================================================
Paziente 100
============================================================
  Run test: 12 + 14 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 484 finestre di riposo / 352 di movimento
  Campioni: 418 tot / 301 accettati / 117 scartati (28.0%)
  Stadio 1 riposo/attivo: 62.63% | score interno 67.08% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 42.19% | score interno 36.46% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 32.32%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 484 finestre di riposo / 352 di movimento
  Campioni: 418 tot / 297 accettati / 121 scartati (28.9%)
  Stadio 1 riposo/attivo: 65.88% | score interno 67.17% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 35.31% | score interno 49.06% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 33.23%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 484 finestre di riposo / 352 di movimento
  Campioni: 418 tot / 294 accettati / 124 scartati (29.7%)
  Stadio 1 riposo/attivo: 64.00% | score interno 68.14% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 48.54% | score interno 31.46% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 40.59%
  Tempo: 0.5s

  Paziente 100: 35.38% con 28.9% di scarti | Tempo: 14.0s

============================================================
Paziente 101
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 313 accettati / 109 scartati (25.8%)
  Stadio 1 riposo/attivo: 63.74% | score interno 56.80% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 16.94% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 28.98%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 310 accettati / 112 scartati (26.5%)
  Stadio 1 riposo/attivo: 66.21% | score interno 56.82% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 24.40% | score interno 23.06% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 27.08%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 306 accettati / 116 scartati (27.5%)
  Stadio 1 riposo/attivo: 64.12% | score interno 60.56% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 19.03% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.12%
  Tempo: 0.5s

  Paziente 101: 29.06% con 26.6% di scarti | Tempo: 17.9s

============================================================
Paziente 102
============================================================
  Run test: 12 + 14 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 492 finestre di riposo / 336 di movimento
  Campioni: 415 tot / 305 accettati / 110 scartati (26.5%)
  Stadio 1 riposo/attivo: 82.57% | score interno 87.26% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 43.45% | score interno 44.58% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 50.59%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.80 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 290 accettati / 124 scartati (30.0%)
  Stadio 1 riposo/attivo: 88.42% | score interno 82.04% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 46.43% | score interno 38.33% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 59.47%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 493 finestre di riposo / 336 di movimento
  Campioni: 414 tot / 296 accettati / 118 scartati (28.5%)
  Stadio 1 riposo/attivo: 79.42% | score interno 84.71% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 52.98% | score interno 40.28% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 55.95%
  Tempo: 0.5s

  Paziente 102: 55.34% con 28.3% di scarti | Tempo: 17.8s

============================================================
Paziente 103
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 302 accettati / 120 scartati (28.4%)
  Stadio 1 riposo/attivo: 67.08% | score interno 68.48% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.36% | score interno 27.92% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.49%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 309 accettati / 113 scartati (26.8%)
  Stadio 1 riposo/attivo: 69.07% | score interno 65.39% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 23.33% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 32.81%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 316 accettati / 106 scartati (25.1%)
  Stadio 1 riposo/attivo: 66.49% | score interno 64.52% | {'clf__shrinkage': 0.2}
  Stadio 2 quattro mosse: 36.31% | score interno 26.39% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 28.66%
  Tempo: 0.4s

  Paziente 103: 29.99% con 26.8% di scarti | Tempo: 17.8s

============================================================
Paziente 104
============================================================
  Run test: 12 + 14 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 479 finestre di riposo / 324 di movimento
  Campioni: 416 tot / 294 accettati / 122 scartati (29.3%)
  Stadio 1 riposo/attivo: 77.80% | score interno 78.26% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 25.60% | score interno 29.58% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 29.18%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 387 tot / 273 accettati / 114 scartati (29.5%)
  Stadio 1 riposo/attivo: 74.29% | score interno 78.26% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 27.48% | score interno 27.78% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 33.72%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 479 finestre di riposo / 324 di movimento
  Campioni: 416 tot / 297 accettati / 119 scartati (28.6%)
  Stadio 1 riposo/attivo: 76.32% | score interno 76.72% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 26.79% | score interno 24.17% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 29.27%
  Tempo: 0.4s

  Paziente 104: 30.73% con 29.1% di scarti | Tempo: 17.6s

============================================================
Paziente 105
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 58.22% | score interno 67.37% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 26.79% | score interno 25.14% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 23.61%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.70 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 298 accettati / 118 scartati (28.4%)
  Stadio 1 riposo/attivo: 63.97% | score interno 66.13% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 34.52% | score interno 39.03% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 30.15%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 318 accettati / 98 scartati (23.6%)
  Stadio 1 riposo/attivo: 69.51% | score interno 60.65% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 30.36% | score interno 23.47% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.49%
  Tempo: 0.5s

  Paziente 105: 28.42% con 26.8% di scarti | Tempo: 18.2s

============================================================
Paziente 106
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 320 accettati / 102 scartati (24.2%)
  Stadio 1 riposo/attivo: 81.15% | score interno 75.33% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 28.57% | score interno 28.75% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 37.13%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 81.72% | score interno 75.88% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 43.45% | score interno 23.61% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 45.60%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.65 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 71.34% | score interno 81.74% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 22.02% | score interno 34.44% | {'clf__shrinkage': 0.5}
  Catena completa sugli accettati: 31.95%
  Tempo: 0.5s

  Paziente 106: 38.23% con 25.6% di scarti | Tempo: 17.9s

============================================================
Paziente 107
============================================================
  Run test: 12 + 14 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 311 accettati / 111 scartati (26.3%)
  Stadio 1 riposo/attivo: 54.62% | score interno 48.27% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 29.76% | score interno 19.58% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 20.27%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 309 accettati / 113 scartati (26.8%)
  Stadio 1 riposo/attivo: 52.25% | score interno 52.95% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 22.02% | score interno 28.47% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 17.05%
  Tempo: 0.4s

  Run test: 4 + 6 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 508 finestre di riposo / 336 di movimento
  Campioni: 422 tot / 325 accettati / 97 scartati (23.0%)
  Stadio 1 riposo/attivo: 53.74% | score interno 47.95% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 22.02% | score interno 18.47% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 17.52%
  Tempo: 0.5s

  Paziente 107: 18.28% con 25.4% di scarti | Tempo: 18.0s

============================================================
Paziente 108
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 313 accettati / 103 scartati (24.8%)
  Stadio 1 riposo/attivo: 55.41% | score interno 52.84% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 44.05% | score interno 36.94% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 29.87%
  Tempo: 0.5s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 317 accettati / 99 scartati (23.8%)
  Stadio 1 riposo/attivo: 57.74% | score interno 48.16% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 45.24% | score interno 27.50% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 31.34%
  Tempo: 0.6s

  Run test: 4 + 6 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 301 accettati / 115 scartati (27.6%)
  Stadio 1 riposo/attivo: 49.54% | score interno 57.44% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 49.40% | score interno 25.56% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 27.84%
  Tempo: 0.5s

  Paziente 108: 29.69% con 25.4% di scarti | Tempo: 18.2s

============================================================
Paziente 109
============================================================
  Run test: 12 + 14 | Threshold: 0.60 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 304 accettati / 112 scartati (26.9%)
  Stadio 1 riposo/attivo: 55.04% | score interno 59.23% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 23.21% | score interno 18.47% | {'clf__shrinkage': 0.2}
  Catena completa sugli accettati: 21.32%
  Tempo: 0.4s

  Run test: 8 + 10 | Threshold: 0.55 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 307 accettati / 109 scartati (26.2%)
  Stadio 1 riposo/attivo: 57.24% | score interno 56.29% | {'clf__shrinkage': 'auto'}
  Stadio 2 quattro mosse: 22.62% | score interno 18.47% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 21.65%
  Tempo: 0.5s

  Run test: 4 + 6 | Threshold: 0.50 | Decisione: cascata | Riallineamento: per_run
  Training: 496 finestre di riposo / 336 di movimento
  Campioni: 416 tot / 332 accettati / 84 scartati (20.2%)
  Stadio 1 riposo/attivo: 60.53% | score interno 55.36% | {'clf__shrinkage': 0.5}
  Stadio 2 quattro mosse: 14.29% | score interno 18.19% | {'clf__shrinkage': 'auto'}
  Catena completa sugli accettati: 20.13%
  Tempo: 0.4s

  Paziente 109: 21.03% con 24.4% di scarti | Tempo: 18.2s

