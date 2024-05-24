# drug_interactions/interactions.py
import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return pd.DataFrame()
    
    try:
        print(f"Loading data from {file_path}")  # Ajout de l'impression pour débogage
        data = pd.read_csv(file_path, on_bad_lines='skip')
        print(f"Data loaded successfully from {file_path}, preview:\n{data.head()}")  # Aperçu des premières lignes
        data[['Drug1', 'Drug2']] = data.iloc[:, 0].str.split(';', expand=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
