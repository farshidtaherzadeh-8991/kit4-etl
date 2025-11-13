# migrations/migrate_entreprise.py

import pandas as pd

# Chargement du fichier des entreprises avec encodage compatible
df = pd.read_csv("../collect/entreprises_proches.csv", encoding="ISO-8859-1")

# Sélection des colonnes nécessaires pour la classe 'Entreprise'
entreprise_df = df[[
    "siren",         # Identifiant unique
    "nom",           # Nom de l'entreprise
    "adresse",       # Adresse complète
    "ville",         # Ville (FK vers commune)
    "code_postal",   # Code postal (FK)
    "epci"           # Code EPCI (FK)
]].drop_duplicates()

# Renommage des colonnes pour correspondre au modèle UML
entreprise_df.columns = [
    "siren",
    "nom_entreprise",
    "adresse",
    "ville",
    "code_postal",
    "code_epci"
]

# Export du fichier CSV final
entreprise_df.to_csv("entreprise.csv", index=False)