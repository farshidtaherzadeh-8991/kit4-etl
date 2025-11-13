# Job ETL – region

## Source
- Fichier : `migrations/[nom].csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Nettoyage des doublons
- Harmonisation des noms de colonnes
- Chargement dans la base SQLite (`kit4.db`)

## Table cible
- Nom : `region`
- Colonnes : code_region,nom_region