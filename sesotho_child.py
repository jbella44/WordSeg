import csv 
from collections import defaultdict

global child_to_sessions
child_to_sessions = defaultdict(list)
child_id = ""
cr = csv.reader(open("./Sesotho/sessionssesotho.csv","r"))
pass_line=0
for rows in cr:
    pass_line+=1
    if pass_line>1:
        row = rows[0].split("#")
        child = row[-2]
        child_to_sessions[child].append(row[0])
for child in child_to_sessions:
    l_tmp = sorted(child_to_sessions[child])
    child_to_sessions[child]= [l_tmp[0],l_tmp[-1]]
