# migrations/migrate_epci.py

import pandas as pd

# Chargement des deux fichiers sources
df_communes = pd.read_csv("../collect/communes_geo_api.csv")
df_entreprises = pd.read_csv("../collect/entreprises_proches.csv", encoding="ISO-8859-1")


# Extraction des EPCI depuis les communes
epci_from_communes = df_communes[["Code EPCI"]].drop_duplicates()
epci_from_communes.columns = ["code_epci"]

# Extraction des EPCI depuis les entreprises
epci_from_entreprises = df_entreprises[["epci"]].drop_duplicates()
epci_from_entreprises.columns = ["code_epci"]

# Fusion des deux sources
epci_all = pd.concat([epci_from_communes, epci_from_entreprises]).drop_duplicates()

# Ajout du nom_epci si disponible (depuis communes_geo_api)
epci_nom_map = df_communes[["Code EPCI", "Nom"]].drop_duplicates()
epci_nom_map.columns = ["code_epci", "nom_epci"]

# Jointure pour récupérer les noms
epci_final = epci_all.merge(epci_nom_map, on="code_epci", how="left")

# Export du fichier CSV final
epci_final.to_csv("epci.csv", index=False)