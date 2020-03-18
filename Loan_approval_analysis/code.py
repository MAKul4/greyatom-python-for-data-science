# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include="object")
print(categorical_var)

numerical_var = bank.select_dtypes(include = "number")
print(numerical_var)






# code ends here


# --------------
# code starts here
banks  = bank.drop('Loan_ID', axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)
banks = banks.fillna("")
print(banks)

#code ends here


# --------------
# code starts here

# check the avg_loan_amount
avg_loan_amount = pd.pivot_table(banks, values = "LoanAmount", index = ["Gender", "Married", "Self_Employed"])

# code ends here


# --------------
# code starts here
loan_approved_se = banks[(banks.Self_Employed == "Yes") & (banks.Loan_Status == 'Y')]
loan_approved_nse = banks[(banks.Self_Employed == "No") & (banks.Loan_Status == 'Y')]

percentage_se = len(loan_approved_se.values)  / 614 * 100
percentage_nse = len(loan_approved_nse.values) / 614 * 100



# code ends here


# --------------
# code starts here



loan_term = banks['Loan_Amount_Term'].apply( lambda  x : x/12)

big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()

print(mean_values)




# code ends here


