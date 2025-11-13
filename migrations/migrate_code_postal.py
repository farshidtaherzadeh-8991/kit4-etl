# migrations/migrate_code_postal.py

import pandas as pd

# Chargement du fichier contenant les codes postaux et noms de communes
df = pd.read_csv("../collect/communes_enrichies.csv")

#  Sélection des colonnes nécessaires pour la classe 'CodePostal'
code_postal_df = df[[
    "Code Postal",          # Code postal
    "Nom de la Commune"     # Nom de la commune
]].drop_duplicates()        # Suppression des doublons

# Renommage des colonnes pour correspondre au modèle UML
code_postal_df.columns = [
    "code_postal",
    "nom_commune"
]

# Export du fichier CSV final dans le dossier 'migrations'
code_postal_df.to_csv("code_postal.csv", index=False)