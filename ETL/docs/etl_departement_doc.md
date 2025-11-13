# Job ETL – departement

## Source
- Fichier : `migrations/department.csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Nettoyage des doublons
- Harmonisation des noms de colonnes
- Chargement dans la base SQLite (`kit4.db`)

## Table cible
- Nom : `departement`
- Colonnes : code_departement,nom_departement