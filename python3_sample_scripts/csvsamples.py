"""
import csv
with open('test.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)

"""

import csv
with open('test.csv','rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print (row)