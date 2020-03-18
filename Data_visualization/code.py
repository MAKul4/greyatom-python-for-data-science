# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar', figsize=(10,5))


#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)



# --------------
#Code starts here

graduate = data[ data['Education'] == 'Graduate' ]
not_graduate = data[ data['Education'] == 'Not Graduate' ]

graduate.plot(x='Education', y='LoanAmount', kind='density', label='Graduate')
not_graduate.plot(x='Education', y='LoanAmount', kind='density', label='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(10,5))

data.plot.scatter('ApplicantIncome', 'LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter('CoapplicantIncome', 'LoanAmount', ax=ax_2)
ax_1.set_title('Coapplicant Incom')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

data.plot.scatter('ApplicantIncome', 'LoanAmount', ax=ax_3)
ax_1.set_title('Total Income')


