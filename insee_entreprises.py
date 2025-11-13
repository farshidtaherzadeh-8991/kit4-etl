import pandas as pd
import requests
import time



df = pd.read_csv("entreprises_proches.csv", encoding="ISO-8859-1")
siren_list = df["siren"].dropna().unique()[:20]  

results = []

for siren in siren_list:
    url = f"https://api.insee.fr/api-sirene/3.11/siren/{siren}"
    params = {"q" : "Test"}
    headers ={"X-INSEE-Api-Key-Integration": "ee7c2c6e-82f7-4555-bc2c-6e82f78555ca"}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get("uniteLegale", {})
        results.append({
            "SIREN": siren,
            "Nom": data.get("denominationUniteLegale", ""),
            "Activité": data.get("activitePrincipaleUniteLegale", ""),
            "Catégorie juridique": data.get("categorieJuridiqueUniteLegale", ""),
            "Date création": data.get("dateCreationUniteLegale", "")
        })
    else:
        print(f"Erreur {response.status_code} pour SIREN {siren}")
    
    time.sleep(3) 


pd.DataFrame(results).to_csv("insee_entreprises.csv", index=False, encoding="utf-8-sig")
print(" Fichier 'insee_entreprises.csv' enregistré avec succès !")