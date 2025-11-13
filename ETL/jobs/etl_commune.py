import pandas as pd
import sqlite3

# Extraction
df = pd.read_csv('../../migrations/commune.csv', encoding='utf-8')

# Transformation
df = df.drop_duplicates()
df.columns = [col.strip().lower() for col in df.columns]

# Load
conn = sqlite3.connect('../database/kit4.db')
df.to_sql('commune', conn, if_exists='replace', index=False)
conn.close()