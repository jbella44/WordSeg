from collections import defaultdict
import os 

####AF----child_name à rentrer en ligne de commande

child = 'wil'
###AF----rootd à rentrer en ligne de commande
rootd="./English/wsexp.zi_/wsexp/Providence"

"""DESCRIBE phono2ortho.py :
  generate the dictionary phono2ortho 
    key = phonological word
    value = orthographic word

  files used : ortholines and gold
  ortholines = file containing the orthographic input 
  gold = file containing the phonological input

 METHODS : 
 --read_files(rootd): 
    return a dictionary with all the files 
    to treat. 
    Example : for "eth01":
    key = '01', value = ['eth01-gold.txt','eth01-ortholines.txt']
 --return_dic():
    return the dictionary phono2ortho  
 --create_phono_to_ortho(phono2ortho,g,o):
    filling of the dic phono2ortho in function of the words
    contained in the files g(the orthographic file) and o(the phonological file) 
"""

def read_files(rootd):
    path_dic = defaultdict(list)
    for f in os.listdir(rootd):
        f_path = rootd +'/'+f
        if os.path.isfile(f_path):
            f_split = f.split("-")
            name = f_split[0][0:3]
            f_id = f_split[0][3:]
            if name ==child and len(f_split)==2 and (f_split[1]=='gold.txt' or f_split[1]=='ortholines.txt'): 
                path_dic[f_id].append(f)
    return path_dic

def create_phono_to_ortho(phono2ortho,g,o):
    for gsent,osent in zip(g,o):
        gsent = gsent.strip('\n').split(" ")
        osent = osent.strip('\n').split(" ")
        for gw,ow in zip(gsent,osent):
            if gw not in phono2ortho:
                phono2ortho[gw]=ow

def clean_dic(phono2ortho):
    newdic = defaultdict(type(phono2ortho))
    for key in phono2ortho:
        if type(phono2ortho[key])!=str:
            print(key,phono2ortho[key])
    return phono2ortho

def return_dic(rootd):
    path_dic = read_files(rootd)
    print(path_dic)
    phono2ortho = defaultdict(list) #0:phono,1:ortho
    for elt in path_dic:
        gfic = open(rootd+'/'+path_dic[elt][0],encoding="utf8")
        ofic = open(rootd+'/'+path_dic[elt][1],encoding="utf8")
        g = gfic.readlines()
        o = ofic.readlines()
        create_phono_to_ortho(phono2ortho,g,o)
        gfic.close()
        ofic.close()
        phono2ortho = clean_dic(phono2ortho)
    return phono2ortho

phono2ortho = return_dic(rootd)
print(phono2ortho)


def return_rootd():
    return(rootd)