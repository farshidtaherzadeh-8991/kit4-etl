# Job ETL – Code Postal

## Source
- Fichier : `migrations/code_postal.csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Suppression des doublons
- Normalisation des noms de colonnes
- Chargement dans la base SQLite (`kit4.db`)

## Table cible
- Nom : `code_postal`
- Colonnes : code_postal, nom_commune, code_commune