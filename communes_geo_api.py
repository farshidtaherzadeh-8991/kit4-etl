import requests
import pandas as pd

# --- 1. Requête à l'API des communes ---
url = "https://geo.api.gouv.fr/communes"
params = {
    "fields": "nom,code,siren,codeDepartement,codeRegion,codeEpci,codesPostaux,centre,population",
    "format": "json",
    "geometry": "centre"
}

response = requests.get(url, params=params)
communes_data = response.json()

# --- 2. Extraction des données(limite à 60 communes) ---
communes_list = []

for commune in communes_data[:60]:
    nom = commune.get("nom", "")
    code = commune.get("code", "")
    siren = commune.get("siren", "")
    code_dep = commune.get("codeDepartement", "")
    code_reg = commune.get("codeRegion", "")
    code_epci = commune.get("codeEpci", "")
    codes_postaux = ",".join(commune.get("codesPostaux", []))
    population = commune.get("population", "")
    
    # Coordonnées géographiques
    coords = commune.get("centre", {}).get("coordinates", [None, None])
    lon, lat = coords if len(coords) == 2 else (None, None)

    communes_list.append({
        "Nom": nom,
        "Code Commune": code,
        "SIREN": siren,
        "Code Département": code_dep,
        "Code Région": code_reg,
        "Code EPCI": code_epci,
        "Codes Postaux": codes_postaux,
        "Latitude": lat,
        "Longitude": lon,
        "Population": population
    })

# --- 3. Sauvegarde dans un fichier CSV ---
df = pd.DataFrame(communes_list)
df.to_csv("communes_geo_api.csv", index=False, encoding="utf-8-sig")

print(" Fichier 'communes_geo_api.csv' enregistré avec succès !")