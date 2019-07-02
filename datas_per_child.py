import os 
from sesotho_child import child_to_sessions 
from collections import defaultdict
import csv 
import argparse

def search_child_id(session):
    for child_id in child_to_sessions:
        #print("CHILD : ",child_id)
        #print("SESSIONS: ",child_to_sessions[child_id][0], child_to_sessions[child_id][1])
        #print("SESSION: ",session)
        if session>=child_to_sessions[child_id][0] and session<=child_to_sessions[child_id][1]:
            return(child_id)

split_rows = []
child_golds = defaultdict(list)
cr = csv.reader(open("./Sesotho/utterances.csv",'r'))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
for rows in cr : 
    stri=""
    for elt in rows : 
        stri += elt
    stri = stri.replace(",","")
    stri = stri.split("#")
    split_rows.append(stri) 

for phr in split_rows:
    txt = phr[0]
    if txt!='utterance':
        child_id = search_child_id(phr[-3])
        child_golds[child_id].append(txt)
#print(child_golds.keys())

####associer utt child a utt dans gold & output & json ?
child = rf.child

gold_child = []
for i in range (len(child_golds[child])):
    #child_golds[child][i] = child_golds[child][i].replace(" ","")
    child_golds[child][i] = child_golds[child][i].replace(";"," ")
    if child_golds[child][i] in g[0]:
        gold_child.append(phr)
        
#######regles phono->ortho        
dic_of_rules = defaultdict(str)
rules =csv.reader(open("./Sesotho.tsv",'r'))
for row in rules: 
    newrow = row[0].split('\t')
    dic_of_rules[newrow[1]] = newrow[0]
print(dic_of_rules)
########

print(len(gold_child)) #vide pour l'instant (correspondance à faire)
print(type(child_golds[child]))
print(g[0][0][0])
print(child_golds['882'][0])
