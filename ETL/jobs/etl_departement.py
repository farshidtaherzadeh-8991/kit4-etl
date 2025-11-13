import pandas as pd
import sqlite3

df = pd.read_csv('../../migrations/departement.csv', encoding='utf-8')
df = df.drop_duplicates()
df.columns = [col.strip().lower() for col in df.columns]

conn = sqlite3.connect('../database/kit4.db')
df.to_sql('departement', conn, if_exists='replace', index=False)
conn.close()