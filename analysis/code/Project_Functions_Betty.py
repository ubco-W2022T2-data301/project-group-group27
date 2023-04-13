import pandas as pd
import numpy as np

def method_chaining(file):
    df = (
        pd.read_excel(io = file)
        .rename(columns=df.iloc[0])
        .iloc[1:].reset_index()
        .apply(pd.to_numeric)   
    )
    
    df1 = (
        df..dropna(axis = 0).drop(columns = 'index')
        .apply(lambda x: ~data['EDUCATION'].isin([0, 5, 6]))
        .apply(lambda x: ~data['MARRIAGE'].isin([0]))
    )
    
    return df1

