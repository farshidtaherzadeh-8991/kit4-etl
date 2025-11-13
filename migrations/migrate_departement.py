# migrations/migrate_departement.py

import pandas as pd

# Chargement du fichier des communes
df = pd.read_csv("../collect/communes_geo_api.csv")

# Sélection des codes département uniques
departement_df = df[["Code Département"]].drop_duplicates()

# Renommage de la colonne pour correspondre au modèle UML
departement_df.columns = ["code_departement"]

# Conversion du code en chaîne de caractères pour concaténation
departement_df["nom_departement"] = "Département " + departement_df["code_departement"].astype(str)

# Export du fichier CSV final dans le dossier 'migrations'
departement_df.to_csv("departement.csv", index=False)

