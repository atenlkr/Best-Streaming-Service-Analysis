import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # For this dataset, no cleaning needed. Placeholder for real-world cleaning.
    return df