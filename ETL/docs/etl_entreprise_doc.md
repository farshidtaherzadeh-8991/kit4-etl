# Job ETL – Entreprise

## Source
- Fichier : `migrations/entreprise.csv`

## Étapes
- Extraction via `pandas.read_csv()`
- Suppression des doublons
- Normalisation des noms de colonnes
- Chargement dans la base SQLite (`kit4.db`)

## Table cible
- Nom : `entreprise`
- Colonnes : siren, nom_entreprise, adresse, ville, code_postal, code_epci
