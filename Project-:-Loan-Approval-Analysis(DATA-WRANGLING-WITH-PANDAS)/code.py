# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
#bank_mode=banks.mode()
for i in banks[['Gender','Married','Dependents','Self_Employed','LoanAmount','Loan_Amount_Term','Credit_History']]:
    bank_mode= banks[i].mode()
    banks[i] = banks[i].fillna('bank_mode')

#banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# code starts here

# check the avg_loan_amount


avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)
# code ends here


# --------------
# code starts here




loan_approved_se=banks.loc[(banks['Self_Employed']=="Yes") & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
        
loan_approved_nse=banks.loc[(banks['Self_Employed']=="No") & (banks['Loan_Status']=='Y'),['Loan_Status']].count()    
percentage_se = (loan_approved_se * 100 / 614)
percentage_nse = (loan_approved_nse * 100 / 614)

percentage_se=percentage_se[0]
percentage_nse=percentage_nse[0]


      



# --------------
# code starts here


def m_y(x):
    x=x/12
    return x

loan_term=banks['Loan_Amount_Term'].apply(m_y)
print(loan_term)
big_loan_term=0
for i in loan_term:
    if(i>=25):
        big_loan_term+=1

print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby(['Loan_Status'])


loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
print(loan_groupby)
mean_values=loan_groupby.mean()
print(mean_values)
# code ends here


