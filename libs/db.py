import sqlite3
import os
import pandas as pd

DATABASE_LOC = 'database.db'
SQL_FILE = 'patients.sql'

def setup():
  print("Setting up database...", end="")

  os.remove(DATABASE_LOC)
  conn = sqlite3.connect(DATABASE_LOC)

  data_files = ['PATIENTS', 'BLOOD_TESTS', 'DIAGNOSES', 'INPATIENT_SPELLS']
  schemas = {}

  for table in data_files:
    df = pd.read_csv(f'data/{table}.csv')
    schemas[table] = df
    df.to_sql(table, conn, if_exists='replace', index=False)

  conn.close()

  print("Done.")

def get_db_connection():
    conn = sqlite3.connect(DATABASE_LOC)
    conn.row_factory = sqlite3.Row
    return conn