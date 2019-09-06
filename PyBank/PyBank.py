import os
import csv
#import file
print(os.getcwd())
csvpath = os.path.join("..","PyBank","budget_data.csv")
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    profitlosses = []
    date = []
    rev_change = []  
#calculate total number of months
#calculate net total amount of "Profit/Losses"
    for xrow in csvreader:
        profitlosses.append(float(xrow[1]))
        date.append(xrow[0])
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:",len(date))
    print("Total: $",sum(profitlosses))
#Calculate the average of the changes in "Profit/Losses"
#Calculate the greatest increase in profits (date and amount)
#Calculate the greatest decrease in losses (date and amount)
    for i in range(1,len(profitlosses)):
        rev_change.append(profitlosses[i] - profitlosses[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
    print("Avereage Change: $", round(avg_rev_change))
    print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")