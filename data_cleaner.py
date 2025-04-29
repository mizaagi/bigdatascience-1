import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    df['Deaths/100 Recovered'] = df['Deaths/100 Recovered'].astype(str).str.replace('inf', '0').astype(float)
    return df