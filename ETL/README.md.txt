# ETL – Extraction, Transformation, Load

Ce dossier contient les scripts et la documentation liés au processus ETL du projet. Chaque job est défini dans `jobs/` et documenté dans `docs/`.

## Objectifs
- Extraire les données des fichiers migrés
- Transformer les données selon le modèle relationnel
- Charger les données dans une base SQLite

## Structure
- `jobs/` : scripts Python pour chaque étape ETL
- `docs/` : schémas, explications, comparaisons ETL vs ELT

## Jobs ETL réalisés
- `etl_commune.py` : structuration et chargement des données des communes


# Projet ETL – Kit 4

## Objectif
Migration et normalisation de 6 fichiers CSV vers une base SQLite (`kit4.db`) via des jobs ETL modulaires.

## Structure
- `jobs/` : scripts ETL individuels
- `docs/` : documentation technique
- `database/kit4.db` : base finale
- `migrations/` : fichiers sources

## Exécution
```bash
python run_all_etl.py