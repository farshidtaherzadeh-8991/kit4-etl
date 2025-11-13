# migrations/migrate_region.py

import pandas as pd

# Chargement du fichier des communes
df = pd.read_csv("../collect/communes_geo_api.csv")

# Sélection des codes région uniques
region_df = df[["Code Région"]].drop_duplicates()

# Renommage de la colonne pour correspondre au modèle UML
region_df.columns = ["code_region"]

# Création d'un nom générique pour chaque région
region_df["nom_region"] = "Région " + region_df["code_region"].astype(str)

# Export du fichier CSV final
region_df.to_csv("region.csv", index=False)