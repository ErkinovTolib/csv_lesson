f = open('data.csv').read()
rows =f.split('\n')
country = []
for i in rows:
    country.append(i.split(',')[3])
print(country)



