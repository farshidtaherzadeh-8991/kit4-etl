# Job ETL – Commune

## Source
- Fichier : `migrations/commune.csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Nettoyage des doublons
- Harmonisation des noms de colonnes
- Chargement dans une base SQLite (`kit4.db`)

## Table cible
- Nom : `commune`
- Colonnes : code_commune, nom_commune, population, gps, code_departement, code_region, code_epci