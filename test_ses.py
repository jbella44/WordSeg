import os 
import csv
import json 
"""
jsons = json.loads(open("./Sesotho/sesotho-puddle/eval_summary.txt",encoding="utf8").read())
print(type(jsons))
"""
w = ["1","2","3"]
print(w[-2])

cr = csv.reader(open("./Sesotho/utterances.csv",'r'))
stri=""
for rows in cr : 
    stri=""
    for elt in rows :
        stri+=elt
    stri = stri.replace(",","")
    print(stri)
for rows in cr : 
    print(rows)