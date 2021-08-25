import os
import csv
pybank = os.path.join("Resources", "budget_data.csv")

with open(pybank) as csv_file:
    csvreader  = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csvreader )
    total=0
    total_pl=0
    changes=[]
    for i,r in enumerate(csvreader):
        print(i)
        if i==0:
            print("First Data")
            previous_r=float(r[1])
            delta=0
            total=1
            changes.append(0)
        else:
            total+=1
            val=float(r[1])# current month
            total_pl+=val
            consecutiveChange=val-previous_r
            delta+=consecutiveChange#net profit loss
            changes.append(consecutiveChange)
            previous_r=val
            
    print("---",delta)     
    print("Total Number of Months: ",total)
    print("Net total Profit/Losses: ",total_pl)
    averageChanges=round(delta/(total-1),2)
    print("Average of the Changes in Profit/Losses: ",averageChanges )    
    print("Greatest Increase:",max(changes))
    print("Greatest Decrease: ",min(changes))

    budget_file = os.path.join("analysis", "report.txt")
    with open(budget_file, "w") as outfile:

        outfile.write("Financial Analysis\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Months:  {total}\n")
        outfile.write(f"Total:  ${total_pl}\n")
        outfile.write(f"Average Change:  ${averageChanges}\n")
        outfile.write(f"Greatest Increase in Profits:  {max(changes)} \n")
        outfile.write(f"Greatest Decrease in Losses:  {min(changes)} ")

