import pandas as pd
import numpy as np

def load_and_process(path_to_csv_file):
    
    # Method Chain 1 (Load data, drop unused column, drop index row, and rename column name)
    
    df=(
    pd.read_excel(io=path_to_csv_file)
    .drop(['Unnamed: 0','X1','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21','X22','X23','Y'],axis=1)
    .rename({'X2':'Sex','X3':'Education','X4':'Marriage','X5':'Age','X6':'PAY_0','X7':'PAY_2','X8':'PAY_3','X9':'PAY_4','X10':'PAY_5','X11':'PAY_6',},axis='columns')
    .iloc[1:]
    .rename({'PAY_0':'Repayment_Status_September,2005','PAY_2':'Repayment_Status_August,2005','PAY_3':'Repayment_Status_July,2005','PAY_4':'Repayment_Status_June,2005','PAY_5':'Repayment_Status_May,2005','PAY_6':'Repayment_Status_April,2005'},axis='columns')
    )
    
    # Method Chain 2 (Drop unusual values, drop NaNs, change the data frame's type to numeric, and reset the index)
    
    df2=(
    df
    .assign(Marriage=lambda x: np.where(x.Marriage==0,np.nan,x.Marriage))
    .loc[lambda x: x['Education']!=0]
    .loc[lambda x: x['Education']!=5]
    .loc[lambda x: x['Education']!=6] 
    .dropna(axis=0)
    .apply(pd.to_numeric)
    .reset_index(drop=True)
    )
    
    # Method Chain 3 (Create a new column, reorder all the columns, and replace numeric values in some columns with more representative names)
    
    df3=(
     df2
     .assign(Average_Repayment_Status=(lambda x: df2[['Repayment_Status_April,2005','Repayment_Status_May,2005','Repayment_Status_June,2005','Repayment_Status_July,2005','Repayment_Status_August,2005','Repayment_Status_September,2005']].mean(axis=1)))
     .reindex(columns=['Sex', 'Education', 'Marriage', 'Age','Repayment_Status_April,2005','Repayment_Status_May,2005','Repayment_Status_June,2005','Repayment_Status_July,2005','Repayment_Status_August,2005','Repayment_Status_September,2005','Average_Repayment_Status'])
     .assign(Sex=lambda x: np.where(x.Sex==1,'male','female'))
     .replace({'Marriage':[1,2,3],'Education':[1,2,3,4]},{'Marriage':['married','single','others'],'Education':['graduate school','university','high school','others']}) 
    )
    return df3
    