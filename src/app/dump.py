import pandas as pd  
import sqlite3
import os
print("Directorio actual:", os.getcwd())


con = sqlite3.connect("./data.db")
cur = con.cursor()

df = pd.read_excel('../data/data.xlsx', engine='openpyxl')

df.to_sql('instituciones', con, if_exists='replace', index=False)
