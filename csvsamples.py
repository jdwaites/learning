import csv
with open('test.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)