# Job ETL – Epci

## Source
- Fichier : `migrations/epci.csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Suppression des doublons
- Normalisation des noms de colonnes
- Chargement dans la base SQLite (`kit4.db`)

## Table cible
- Nom : `epci`
- Colonnes : code_epci, nom_epci