import json 
import os
from collections import defaultdict
import argparse
import csv 

parser = argparse.ArgumentParser()
parser.add_argument("child", help = "name/id")
parser.add_argument("language", help="English/Sesotho/Japanese/Indonesian")
args = parser.parse_args()

global language 
language = args.language
global child
child = args.child

global j_child_data_en
global g_child_data_en
global o_child_data_en
global j_child_data
global g_child_data
global o_child_data

#stockage des outputs,gold et json pour l'anglais (8 algos)
o_child_data_en=[[],[],[],[],[],[],[],[]]
g_child_data_en=[[],[],[],[],[],[],[],[]]
j_child_data_en=[[],[],[],[],[],[],[],[]]

#stockage des outputs,gold et json pour les 3 autres langues (12 algos) 
o_child_data=[[],[],[],[],[],[],[],[],[],[],[],[]]
g_child_data=[[],[],[],[],[],[],[],[],[],[],[],[]]
j_child_data=[[],[],[],[],[],[],[],[],[],[],[],[]]


def read_dirs(rootd):
    count=0
    b_o,b_g = False,False
    for subdir in os.listdir(rootd) :
        subdir_split = subdir.split("-")
        print(subdir_split)
        #if 'or' add
        if (len(subdir_split)>1 and subdir_split[0]==child) or (len(subdir_split)>1 and subdir_split[0]==language.lower()): 
            chemin = rootd+'/'+subdir
            #print(chemin)
            if os.path.isdir(chemin)==True:
                o_path = chemin+'/'+"output.txt"
                g_path = chemin+'/'+"gold.txt"
                print("goldpath********* = ",g_path)
                if language=='English':
                    json_path =  chemin+'/'+"eval_summary.json"
                if language=='Sesotho':
                    json_path = chemin+"/eval_summary.txt"
                if os.path.isfile(o_path) == True:
                    output = open(o_path,encoding="utf8")
                    b_o = True
                    outputs = output.readlines()
                if b_o==True and os.path.isfile(g_path):
                    gold =open(g_path,encoding="utf8")
                    b_g = True
                    golds = gold.readlines()
                    print(len(golds))
                if b_o == True and b_g == True and os.path.isfile(json_path):
                    count+=1
                    jsons = json.loads(open(json_path,encoding="utf8").read())
                    store_datas_per_algorithms(subdir,outputs,golds,jsons)



def associate_number_to_algorithms_en(subdir):
    split_subdir_name = subdir.split("-")
    algorithm = split_subdir_name[-1]
    if algorithm=='tpabs':
        return 0
    elif algorithm=='tprel':
        return 1
    elif algorithm=='puddle':
        return 2
    elif algorithm=='dibs':
        return 3
    elif algorithm=='ag':
        return 4
    elif algorithm=='00':
        return 5
    elif algorithm=='05':
        return 6
    else :
        return 7

def associate_number_to_algorithms(subdir):
    split_subdir_name = subdir.split("-")
    algorithm = split_subdir_name[-1]
    if algorithm=='puddle':
        return 0
    elif algorithm=='mir':
        return 1
    elif algorithm=='mia':
        return 2
    elif algorithm=='ftpr':
        return 3
    elif algorithm=='ftpa':
        return 4
    elif algorithm=='dibs':
        return 5
    elif algorithm=='btpr':
        return 6
    elif algorithm=='btpa':
        return 7
    elif algorithm=='base6':
        return 8
    elif algorithm=='base1':
        return 9
    elif algorithm=='base0':
        return 10
    else : #ag
        return 11

def store_datas_per_algorithms(subdir,o,g,j):
    if language=="English":
        idx_algo = associate_number_to_algorithms_en(subdir)
        o_child_data_en[idx_algo].append(o)
        g_child_data_en[idx_algo].append(g)
        j_child_data_en[idx_algo].append(j)
    if language=="Sesotho":
        #print("##########################")
        idx_algo = associate_number_to_algorithms(subdir)
        o_child_data[idx_algo].append(o)
        g_child_data[idx_algo].append(g)
        j_child_data[idx_algo].append(j)

def return_child_datas():
    if language=='English':
        return j_child_data_en,g_child_data_en,o_child_data_en
    if language=='Sesotho':
        return j_child_data,g_child_data,o_child_data
def return_child_name():
    return child

rootd = "./"+rf.language
read_dirs(rootd)
j,g,o = return_child_datas() 
for i in range(len(g)):
    for k in range (len(g[i][0])):
        g[i][0][k] = g[i][0][k].strip('\n')
        o[i][0][k] = o[i][0][k].strip('\n')
#contient les jsons,output,golds (pas séparé par enfant pour le sesotho)