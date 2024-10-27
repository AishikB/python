import csv

with open('expense.csv', "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)