import csv

try:
    printHeader=True
    with open('names.csv', "r+", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            printHeader=False
        csvfile.close()
    with open('names.csv', 'a', newline='') as csvfile:
        fieldNames=["first_name", "last_name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        if printHeader:
            writer.writeheader()
        writer.writerow({'first_name': 'Baked_new_1', 'last_name': 'Beans_new_1'})
        csvfile.close()
except:
    with open('names.csv', 'a', newline='') as csvfile:
        fieldNames=["first_name", "last_name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked_new_1', 'last_name': 'Beans_new_1'})
        csvfile.close()