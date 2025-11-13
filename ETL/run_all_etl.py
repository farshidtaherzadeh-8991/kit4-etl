import subprocess
import os

job_folder = "jobs"
job_files = [
    "etl_commune.py",
    "etl_departement.py",
    "etl_region.py",
    "etl_epci.py",
    "etl_entreprise.py",
    "etl_code_postal.py"
]

print("Démarrage de l'exécution des jobs ETL...\n")

for job in job_files:
    job_path = os.path.join(job_folder, job)
    print(f" Exécution de {job}...")
    result = subprocess.run(["python", job_path], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{job} terminé avec succès.\n")
    else:
        print(f" Erreur dans {job}:\n{result.stderr}\n")

print("Tous les jobs ETL ont été traités.")