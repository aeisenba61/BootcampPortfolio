# Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset

# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period

# * The greatest increase in revenue (date and amount) over the entire period

# * The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```

import os
import csv
import pandas as pd
import glob

cols = ["Date", "Revenue"]

names = pd.DataFrame()
for i in glob.glob('*.csv', recursive=True):
    #print(i)
    df = pd.read_csv(i, header = None, skiprows=[0],names = cols)
print(df)

df['DateIndex'] = df['Date']
df2 = df.set_index('DateIndex')
total_revenue = df2['Revenue'].sum()
max_change = df2['Revenue'].max()
max_date = df2['Revenue'].argmax()
min_change = df2['Revenue'].min()
min_date = df2['Revenue'].argmin()
unique_months = df2['Date'].unique()
total_months = len(unique_months)
AvgRevChange = total_revenue / total_months
AvgRevChangeTest = df2['Revenue'].mean()


print("Total Months: " + str(format(total_months, '0,')) + '\n'
	+ "Total Revenue: $" + str(format(total_revenue,'0,')) + '\n'
	+ "Average Revenue Change: $" + str(format(AvgRevChange,'0,')) + '\n'
	+ "Greatest Increase in Revenue: $" + str(format(max_change,'0,')) + ' on ' + str(max_date) + '\n'
	+ "Greatest Decrease in Revenue: " + str('${:,.2f}'.format(min_change)) + ' on ' + str(min_date)
    )