import pandas as pd
import requests
import time

# توکن دسترسی که از قبل گرفتی
access_token = "ee7c2c6e-82f7-4555-bc2c-6e82f78555ca"

# خواندن لیست SIREN از فایل CSV
df = pd.read_csv("communes_geo_api.csv")
siren_list = df["SIREN"].dropna().unique()[:50]  # محدود به 50 شرکت

# آماده‌سازی لیست خروجی
results = []

# حلقه روی SIRENها
for siren in siren_list:
    url = f"https://api.insee.fr/api-sirene/3.11/siren/{siren}"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(url, headers=headers)
    
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
        print(f"⚠️ Erreur {response.status_code} pour SIREN {siren}")
    
    time.sleep(1)  # برای جلوگیری از بلاک شدن توسط API

# ذخیره در فایل CSV
pd.DataFrame(results).to_csv("insee_entreprises.csv", index=False, encoding="utf-8-sig")
print("✅ Fichier 'insee_entreprises.csv' enregistré avec succès !")