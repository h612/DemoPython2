import os
import csv
pybank = os.path.join("Resources", "election_data.csv")


dict1={}#DICTIONARY OF KEY VALUES {NAME: VOTES}
tv=0# TOTAL VOTES

with open(pybank,"r") as csv_file:
    csvreader  = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csvreader )
    
    for r in csvreader:
        try:
            dict1[r[2]]#try to access the value from key
        except KeyError:
            dict1[r[2]]=1#new person
            tv+=1
        else:
            dict1[r[2]]=dict1[r[2]]+1#INCREMENT VOTES
            tv+=1

election_file = os.path.join("analysis", "reportPoll.txt")

with open(election_file, "w") as outfile:
    outfile.write("""Election Results\n-------------------------\nTotal Votes: {}\n-------------------------""".format(tv))
    i=0

    for wn, v in reversed(sorted(dict1.items(), key=lambda x: x[1])):
        outfile.write("""\n{}: {}% ({})""".format(wn,round(v/tv*100,2),v))
        
        if i==1:
            winner=wn
            
    outfile.write("""\n-------------------------\nWinner: {}\n-------------------------""".format(winner))



