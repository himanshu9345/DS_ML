import pandas as pd

loan_data=pd.read_csv(".\\LoanStats3b\\LoanStats3b.csv",low_memory=False,skiprows=1)
dataset = loan_data.iloc[:,2:111]
print (loan_data)