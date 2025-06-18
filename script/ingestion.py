from google.cloud import bigquery
import pandas as pd
import os

# Authentification
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Retail project/Crediantials/retail_keys.json" # Your key path 
client = bigquery.Client()

# Nom du dataset
dataset_id = "new_retail"  # your dataset name
project_id = client.project

def load_csv_to_bq(csv_path, table_name):
    df = pd.read_csv(csv_path)
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"✅ Table {table_name} chargée ({len(df)} lignes)")

# upload the files
load_csv_to_bq("C:/Retail project/data/dataproducts.csv", "products")
load_csv_to_bq("C:/Retail project/data/datacustomers.csv", "customers")
load_csv_to_bq("C:/Retail project/data/datasales.csv", "sales")
