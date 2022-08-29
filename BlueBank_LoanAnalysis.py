# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:51:29 2022
A visualization of this project can be found at https://public.tableau.com/app/profile/rodney.buerkley/viz/BlueBankLoanAnalysis_16589269396020/BlueBankLoan
@author: Rodney Buerkley
"""

#Importing libraries and files
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('loan_data_json.json') as json_file:
    Data = json.load(json_file)
    
loandata = pd.DataFrame(Data)

#exploring the data
loandata['purpose'].unique()

loandata.describe()

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

income = np.exp(loandata['log.annual.inc'])
loandata['annual_income'] = income

#analyzing FICO score
# - 300 - 400: Very Poor
# - 401 - 600: Poor
# - 601 - 660: Fair
# - 661 - 780: Good
# - 781 - 850: Excellent

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

# new column for interest rate
# rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'Low'

# number of loans by fico category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

# count of purposes in data
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.5)
plt.show()

#Writing to a CSV
loandata.to_csv('loan_cleaned.csv', index = True)



