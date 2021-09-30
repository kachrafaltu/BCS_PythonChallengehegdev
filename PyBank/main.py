# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

prev_period_profit = 0
prev_period = ""
previous_year = ""
cur_month_change = 0
max_profit_increase = 0
max_profit_decrease = 0
total_profit_change = 0
avg_profit_change=0
total_months = 0
period = []
profit = []
profit_change = []
max_profit_incr_period =""
max_profit_desc_period = ""

#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
#        print(row)
        period.append(row[0])
        profit.append(int(row[1]))
#    print(period," -- ", profit)
#    print(period.__len__())
    total_months = period.__len__()

    for i in range(total_months) :
        if i > 0:
#            print("Current Change for " ,period[i], profit[i]-profit[i-1])
            profit_change.append(profit[i]-profit[i-1])
            if max_profit_increase < (profit[i]-profit[i-1]):
                max_profit_increase = (profit[i]-profit[i-1])
                max_profit_incr_period = period[i]
            if max_profit_decrease > (profit[i]-profit[i-1]):
                max_profit_decrease = (profit[i]-profit[i-1])
                max_profit_decr_period = period[i]

#    print("Done")

    with open("./Analysis/output.txt", 'w') as outfile:

        print("Total Months :" , total_months)
        outfile.write(f"Total Months : {total_months}\n")
        print("Average Change of Profit :" ,sum(profit_change)/len(profit_change))
        outfile.write(f"Average Change of Profit : {sum(profit_change)/len(profit_change)}\n")
        print("Greatest increase in Profits :" , max_profit_incr_period, "  (", max(profit_change), ")")
        outfile.write(f"Greatest increase in Profits : {max_profit_incr_period}  ( { max(profit_change)})\n")
    #    print("Greatest increase period : ", max_profit_incr_period)
        print("Greatest decrease in Profit :" , max_profit_decr_period , "  (", min(profit_change) , ")")
        outfile.write(f"Greatest decrease in Profit : {max_profit_decr_period } ({min(profit_change)})\n")
    #    print("Greatest decrease period : ", max_profit_decr_period)
    #    print(" Average Change of Profit :" mean(profit_change))
        print(f"Total Profit/Loss over entire dataset : {sum(profit)}")
        outfile.write(f"Total Profit/Loss over entire dataset : {sum(profit)}\n")


