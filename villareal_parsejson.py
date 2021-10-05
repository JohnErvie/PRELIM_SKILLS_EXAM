import json
import csv

with open('covid_cases.json','r') as f:
    #print(f)
    covid = json.load(f)

with open('test.csv', 'w') as f:
    for key in covid.keys():
        f.write("%s,%s\n"%(key,covid[key]))