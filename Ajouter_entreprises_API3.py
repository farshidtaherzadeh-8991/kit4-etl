import pandas as pd
import requests
import time

communes = pd.read_csv("communes_enrichies.csv")


all_entreprises = []

for index, row in communes.iterrows():
    nom_commune = row["Nom de la Commune"]
    lat = row["Latitude"]
    lon = row["Longitude"]

    print(f" Recherche des entreprises autour de {nom_commune}")

    url = "https://geo.api.gouv.fr/communes"
    params = {
        "latitude": lat,
        "longitude": lon,
        "radius": 0.5, 
        "per_page": 50
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if "results" in data:
            for ent in data["results"]:
                all_entreprises.append({
                    "Commune": nom_commune,
                    "Nom entreprise": ent.get("nom_entreprise", ""),
                    "SIREN": ent.get("siren", ""),
                    "Activité principale": ent.get("activite_principale", ""),
                    "Section": ent.get("section_activite_principale", ""),
                    "Adresse": ent.get("siege", {}).get("adresse", ""),
                    "Code postal": ent.get("siege", {}).get("code_postal", "")
                })

        else:
            print(f" Aucun résultat pour {nom_commune}")

    except Exception as e:
        print(f"Erreur pour {nom_commune}: {e}")

    time.sleep(1)  

df_final = pd.DataFrame(all_entreprises)
df_final.to_csv("entreprises_par_commune_api.csv", index=False, encoding="utf-8-sig")

print(" Fichier 'entreprises_par_commune_api.csv' enregistré avec succès !")

