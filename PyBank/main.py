# Import Mods
import os
import csv

#set path for file
csvpath = os.path.join("Resources" , "PyBank_budget_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # ignore first row - header
    csvheader = next(csvfile)
    # print(f"header:{header}")

    # set counters to 0
    Total_Profit = 0.00
    Total_Months = 0
    Avg_Change = 0

    # store values in empty list for the variables
    Months = []
    Profit = []
    Avg_Change = []
  
    for row in csvreader:
        # total amount of "Profit/Losses"
        Total_Profit = (Total_Profit + float(row[1]))
        # total number of months
        Total_Months = int(Total_Months+1)
        # find the increase in profits in the amount list
        Profit.append(float(row[1]))
        # find the increase in profits in the months list
        Months.append(str(row[0]))

    # going through the profits in order to get the monthly change 
    for i in range(len(Profit)-1):
        
        # getting the difference (decrease) between the two numbers and add to monthly profit change list
        Avg_Change.append(Profit[i+1]-Profit[i])

increase_value = max(Avg_Change)
decrease_value = min(Avg_Change)

# finding max and min in the months using  the month list and index from max and min

increase_month = Avg_Change.index(max(Avg_Change)) + 1
decrease_month = Avg_Change.index(min(Avg_Change)) + 1 


#display results
print("Financial Analysis")
print("...........................")
print(f"Total months: {Total_Months}")
print(f"Total profit: ${Total_Profit}")
print(f"Average change: ${round(sum(Avg_Change)/len(Avg_Change),2)}")
print(f"Greatest Increase in Profits: {Months[increase_month]} ${increase_value}")
print(f"Greatest Decrease in Profits: {Months[decrease_month]} ${decrease_value}")

# Output results to a file
output_file = os.path.join("analysis", "analysis_results.txt")

with open (output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("...........................")
    file.write("\n")
    file.write(f"Total months: {Total_Months}")
    file.write("\n")
    file.write(f"Total profit: ${Total_Profit}")
    file.write("\n")
    file.write(f"Average change: ${round(sum(Avg_Change)/len(Avg_Change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Months[increase_month]} ${increase_value}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Months[decrease_month]} ${decrease_value}")