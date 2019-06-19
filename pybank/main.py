import os
import csv

#initialize variables 
months=0
total_PL=0
min_change = 0
max_change = 0
past_month=0
monthly_change=0
total_monthly_change=0
avg_monthly_change=0
total_PL=0
data=[]

# Read budget.csv file
budget_file = 'budget_data.csv'
with open(budget_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
    #total months 
        months += 1 
    #total P&L value 
        total_PL = total_PL+int(row[1])
    #variables to calculate monthly changes and min/max- made data[] a list above so this will be dynamic 
    #this tells which column is months 
        month=str(row[0])
    #this tells which column is PL numbers 
        PL=float(row[1])
    #this, because it's in the for loop, adds every line to the "data" list I made above
        data.append([month,PL])
    # this is setting up variables for the previous and next months so I can manipulate - entry is where I'll start but then I want current month and next month to be their own variables
    for row in range(len(data)-1):
        entry=data[row]
        current_month = entry[1]
        next_entry=data[row+1]
        next_month = next_entry[1]
        #loop through and add all monthly changes to get total monthly change that I'll divide by total months to get avg 
        monthly_change=next_month-current_month
        total_monthly_change = total_monthly_change + monthly_change
        if min_change > monthly_change:
            Date1=entry[0]
            min_change = monthly_change
            
        if max_change < monthly_change:
            Date2=entry[0]
            max_change = monthly_change
            
    #have to divide by months-1 because there are only 85 "change" values while there are 86 months.  The first month change value isn't starting from 0, but we don't know where it started so I'm ommitting and checking against the excel
    avg_monthly_change = total_monthly_change / (months-1)

    print("\nFinancial Analysis")
    print("----------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_PL}")
    print(f"Average: ${avg_monthly_change}")
    print(f"Greatest increase in profit on {Date2} is ${max_change}")
    print(f"Greatest decrease in profit on {Date1} is ${min_change}\n")