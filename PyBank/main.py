import os 
import csv

# Store and set path for the file
#file = 'E:\Data Analyst Bootcamp\MONU-VIRT-DATA-PT-05-2022-U-LOL\02-Homework\03-Python\Instructions\PyBank\Resources'
#csvpath = os.path.join(file)

csvpath = os.path.join('budget_data.csv')

# open and read csv file
with open(csvpath, newline='') as csvfile:
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Read the csv header
    header = next(csv_reader)

    # create empty list to storecvs value
    month_count = []
    revenue = []
    revchange= []

    for row in csv_reader:
        month_count.append(row[0])
        revenue.append(int(row[1]))
    
    # run through the revenue list to find the change in revenue from month
    for i in range(len(revenue)-1):
        revchange.append(revenue[i+1] - revenue[i])

    # revchange = [revenue[i+1] - revenue[i] for i in range(len(revenue)-1)]

    # evaluate max and min of revenue change
max_revchange = max(revchange)
min_revchange = min(revchange)
    
    # identify the index of max and min revchange
month_increase = revchange.index(max_revchange)+1
month_decrease = revchange.index(min_revchange)+1


# print the result on separate text
output = os.path.join('output.txt')
with open(output, 'w') as result:
     result.write("Financial Analysis\n")
     result.write("------------------------\n")
     result.write(f"Total Months: {len(month_count)}\n")
     result.write(f"Total: ${sum(revenue)}\n")
     result.write(f"Average Change: {round(sum(revchange)/len(revchange),2)}\n")
     result.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(max_revchange))})\n")
     result.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(min_revchange))})\n")

#prints file to terminal
with open(output, 'r') as readfile:
    print(readfile.read())