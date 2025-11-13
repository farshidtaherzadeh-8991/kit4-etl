# Projet ETL – Kit 4

## Objectif
Ce projet vise à migrer et normaliser six fichiers CSV vers une base de données SQLite (`kit4.db`) à l’aide de scripts ETL modulaires. Chaque fichier source est traité individuellement selon un schéma relationnel défini dans un diagramme UML.

## Structure du projet
extraction/ ├── ETL/ │   ├── jobs/              # Scripts ETL pour chaque entité │   ├── docs/              # Documentation technique pour chaque job │   ├── run_all_etl.py     # Script principal pour exécuter tous les jobs │   └── README.md          # Ce fichier ├── migrations/            # Fichiers CSV sources ├── database/              # Base de données SQLite (exclue du Git)


## 🛠️ Technologies utilisées
- Python 3.x
- SQLite
- Pandas
- Git

##  Instructions d’exécution

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/farshidtaherzadeh-8991/kit4-etl.git
   cd kit4-etl

   2. 	Placer les fichiers CSV dans le dossier migrations/
3. 	Exécuter le script principal :

python ETL/run_all_etl.py
4- La base de données kit4.db sera générée dans database/


Documentation
Chaque script ETL est accompagné d’un fichier Markdown dans ETL/docs/ expliquant :
- Les colonnes extraites
- Les transformations appliquées
- Les clés primaires et étrangères
- Les liens avec le diagramme UML
   Auteur
Farshid Taherzadeh
Projet académique – Grenoble, France
Langues : 🇫🇷 Français 
م
