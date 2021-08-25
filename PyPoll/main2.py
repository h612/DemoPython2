import os
import csv
from collections import Counter
pybank = os.path.join("Resources", "election_data.csv")

with open(pybank) as csv_file:
    csvreader  = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csvreader )
    total=0
    total_pl=0
    changes=[]
    list_of_candidates=[]
    unique_list_of_candidates=[]
    for i,r in enumerate(csvreader):
        
        total+=1
        new_row = [' '.join([r[1], r[2]])]
        list_of_candidates.append(new_row[0])
        
        c=Counter(list_of_candidates)
        
    print(unique_list_of_candidates)     
    print(c)
    print("The total number of votes cast: ",total)
    print("A complete list of candidates who received votes: ",unique_list_of_candidates)
    
    print("Greatest Increase:")
    print("Greatest Decrease: ")

##    budget_file = os.path.join("analysis", "report.txt")
##    with open(budget_file, "w") as outfile:
##
##        outfile.write("Financial Analysis\n")
##        outfile.write("----------------------------\n")
##        outfile.write(f"Total Months:  {total}\n")
##        outfile.write(f"Total:  ${total_pl}\n")
##        outfile.write(f"Average Change:  ${averageChanges}\n")
##        outfile.write(f"Greatest Increase in Profits:  {max(changes)} \n")
##        outfile.write(f"Greatest Decrease in Losses:  {min(changes)} ")
##
