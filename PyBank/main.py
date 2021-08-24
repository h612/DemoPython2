import os
import csv
pybank = os.path.join("Resources", "budget_data.csv")
#pybank = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBank\Resources\budget_data.csv'
# Open and read csv
with open(pybank) as csv_file:
    csvreader  = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csvreader )
    print(pybank_header)
    
