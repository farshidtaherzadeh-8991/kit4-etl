# migrations/migrate_commune.py

import pandas as pd

# Chargement du fichier source contenant les données géographiques des communes
df = pd.read_csv("../collect/communes_geo_api.csv")

# Sélection des colonnes utiles pour la classe 'Commune' selon le diagramme UML
commune_df = df[[
    "Nom",                # Nom de la commune
    "Code Commune",       # Code INSEE de la commune
    "Code Département",   # Code du département
    "Code Région",        # Code de la région
    "Latitude",           # Coordonnée géographique (latitude)
    "Longitude",          # Coordonnée géographique (longitude)
    "Population"          # Population de la commune
]].drop_duplicates()      # Suppression des doublons éventuels

# Renommage des colonnes pour correspondre aux noms du modèle UML
commune_df.columns = [
    "nom_commune",
    "code_commune",
    "code_departement",
    "code_region",
    "latitude",
    "longitude",
    "population"
]

# Export du fichier CSV final dans le dossier 'migrations'
commune_df.to_csv("commune.csv", index=False)