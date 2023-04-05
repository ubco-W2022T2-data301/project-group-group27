def myfunction1():
    df12 =(pd.read_excel(io=r'../data/raw/default of credit card clients.xls')
    .drop("Unnamed: 0",axis=1)
    .iloc[1:]
    .rename(columns={"X1": "LIMIT_BAL","X2":"SEX","X3":'EDUCATION',"X4":"MARRIAGE","X5":"AGE","X6":"PAY_0",
       "X7":"PAY_2", "X8":"PAY_3","X9":"PAY_4", "X10":"PAY_5", "X11":"PAY_6","X12":"BILL_AMT1","X13": "BILL_AMT2",
       "X14":"BILL_AMT3","X15":"BILL_AMT4","X16":"BILL_AMT5","X17":"BILL_AMT6", "X18":"PAY_AMT1",
       "X19":"PAY_AMT2","X20":"PAY_AMT3", "X21":"PAY_AMT4","X22":"PAY_AMT5", "X23":"PAY_AMT6",
       "Y":"default payment next month"})
    .replace({'SEX':[1,2]},{'SEX':['male','female']})
    .replace({'default payment next month':[1,0]},{'default payment next month':['yes','no']})
    .replace({'MARRIAGE':[0,1,2,3]},{'MARRIAGE':['unknown','married','single','others']})
    .replace({'EDUCATION':[0,1,2,3,4,5,6]},{'EDUCATION':['unknown','graduate school','university','high school','others','unknown','unknown']}))
    df13= (df12.drop(columns = ['SEX', 'EDUCATION','MARRIAGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6','default payment next month'])
       .sort_values("AGE", ascending=True)
       .assign(percentage=lambda x: (x['AGE']/x['LIMIT_BAL'])))
    return df13
def myfunction2():
    df14= (df12.drop(columns = ['SEX', 'LIMIT_BAL','EDUCATION','MARRIAGE','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6','default payment next month'])
       .sort_values("AGE", ascending=True)
       .assign(percentage1=lambda x:(x['PAY_0']/x['AGE']))
       .assign(percentage2=lambda x:(x['PAY_2']/x['AGE']))
       .assign(percentage3=lambda x:(x['PAY_3']/x['AGE']))
       .assign(percentage4=lambda x:(x['PAY_4']/x['AGE']))
       .assign(percentage5=lambda x:(x['PAY_5']/x['AGE']))
       .assign(percentage6=lambda x:(x['PAY_6']/x['AGE'])))
    return df14
def myfunction3():
    df14= (df12.drop(columns = ['SEX','AGE','LIMIT_BAL','EDUCATION','MARRIAGE','default payment next month'])
       .assign(Topay1=lambda x:(x['PAY_0']*x['BILL_AMT1']))
       .assign(Topay2=lambda x:(x['PAY_2']*x['BILL_AMT2']))
       .assign(Topay3=lambda x:(x['PAY_3']*x['BILL_AMT3']))
       .assign(Topay4=lambda x:(x['PAY_4']*x['BILL_AMT4']))
       .assign(Topay5=lambda x:(x['PAY_5']*x['BILL_AMT5']))
       .assign(Topay6=lambda x:(x['PAY_6']*x['BILL_AMT6'])))
    return df14