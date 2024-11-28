import pandas as pd

def dropMissingData(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['name'])
    return df

