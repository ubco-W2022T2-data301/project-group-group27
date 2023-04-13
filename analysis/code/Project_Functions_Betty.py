import pandas as pd
import numpy as np

def method_chaining(data_methodchaining):
    dataframe = (
        data_methodchaining.rename(columns=data_methodchaining.iloc[0])
        .iloc[1:].reset_index()
        .apply(pd.to_numeric)   
    )
    
    dataframe1 = (
        dataframe.dropna(axis = 0).drop(columns = 'index')
        .apply(lambda x: ~x['EDUCATION'].isin([0, 5, 6]))
        .apply(lambda x: ~x['MARRIAGE'].isin([0]))
    )
    
    return dataframe1

