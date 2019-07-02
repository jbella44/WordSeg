import read_folder as rf
from read_folder import language
from read_folder import child
from collections import defaultdict
import json


#child = rf.return_child_name()
global rootd 
if language=="English":
    rootd = "./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp/results_do_concat_prov"
else : 
    rootd = "./"+language

rf.read_dirs(rootd)
j,g,o = rf.return_child_datas()
print(len(j[0]),len(g[0]),len(o[0]))

""" Input : the dict "over" included in the json file in treatment
   Fill a dictionary(word2oseg_occ) which store every word and its associated
   segmentations, and the utterances of this segmentation.
   key = the gold word 
   value = list of lists : [
                    [[x1..xi,xi+1,xk],occ],
                    ...
                    [[x1...xj,xj+1,xk],occ]
                           ]
    example :{ bathroom : 
                [[["bath","room"],11],
                 [["bat","hroom"],2] 
                ]
"""

global word2oseg
word2oseg = defaultdict(list)
global word2oseg_occ
word2oseg_occ = defaultdict(list)


def store_word_oseg(dic_of_oseg,output,word2oseg,word2oseg_occ):
    for wordg in dic_of_oseg:
        find_oseg(wordg,dic_of_oseg[wordg],output,word2oseg,word2oseg_occ)


def find_oseg(wordg,oseg_occ,output,word2oseg,word2oseg_occ):
    before_cut = wordg[0]
    for i in range(1,len(wordg)): #long de la decoupe min. 2 : m1m2..mn --> m1m1... mn
        before_cut += wordg[i]
        for sent in output:
            sent = sent.rstrip('\n').split(" ")
            seg = analyze_sent(sent,before_cut,wordg)
            if seg!=None :
                if seg not in word2oseg[wordg]:
                    word2oseg[wordg].append(seg)
                    word2oseg_occ[wordg].append([seg,1])
                else :
                    for elt in word2oseg_occ[wordg]:
                        if elt[0]==seg:
                            elt[1]+=1

def analyze_sent(sent,bc,w):
    seg_form = [bc]
    if bc in sent : 
        idx_bc = sent.index(bc)
        while len(bc) < len(w)-1 and idx_bc < len(sent)-1 :
            bc += sent[idx_bc+1]
            idx_bc+=1
            seg_form.append(sent[idx_bc])
            if w==bc : 
                return seg_form
            elif w.startswith(bc) == False : 
                return None


global list_dic_per_algo
list_dic_per_algo = list()

def return_child_dics():
    for i in range(0,8):
        word2oseg = defaultdict(list)
        word2oseg_occ = defaultdict(list)
        for k in range(0,len(j[i])):
            print(len(o[i][k]))
            store_word_oseg(j[i][k]["over"],o[i][k],word2oseg,word2oseg_occ)
            print("file of algo ",i," number",k, "processed")
        list_dic_per_algo.append(word2oseg_occ)
    return list_dic_per_algo

listdics = return_child_dics()
if language=="English":
    path_name = "./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp/"+child+'_datas.json'
if language=='Sesotho':
    path_name = "./Sesotho/sesotho_datas.json"
with open(path_name,'w') as file:
    json.dump(listdics,file)
    
