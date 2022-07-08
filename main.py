f = open('data.csv').read()
rows =f.split('\n')
country = []
for i in rows:
    country.append(i.split(',')[3])
print(country)

import csv 
f = open('data.csv')
r = csv.reader(f)
for row in r:
    print(row[3])

