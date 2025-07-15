import pandas as pd
import zipfile
import os

def load_data(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall("data/")
    # Load the JSON file into a DataFrame
    df = pd.read_json("D:\shaha\Documents\python progams\AaveCreditScoring\user-wallet-transactions.json\user-wallet-transactions.json")
    return df

def clean_data(df):
    # Handle missing values
    df.dropna(inplace=True)
    # Convert timestamps to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
