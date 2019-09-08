import os
import csv

#opening the file
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #define variables
    total_revenue = 0
    total_months = 0
    prev_revenue = 0
    change_revenue = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999999]


    # Read each row of data after the header
    for row in csvreader:

        #Get the total months
        total_months += 1

        #Get the total revenue
        total_revenue += int(row[1])

        #Get the average of the changes
        change_revenue = (int(row[1]) - prev_revenue)/total_months
        # avg_change = change_revenue/85
        
        #Get the greatest increase
        if (change_revenue > greatest_increase[1]):
            greatest_increase[1] = change_revenue
            greatest_increase[0] = row[0]

        #Get the greatest decrease
        if (change_revenue < greatest_decrease[1]):
            greatest_decrease[1] = change_revenue
            greatest_decrease[0] = row[0]


print(f"Total Months: {total_months}")
print(f"Total: {total_revenue}")
print(f"Average Change: {change_revenue}")
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
 

