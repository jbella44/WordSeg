from collections import defaultdict
import word2phon as wp
import json 
from read_folder import return_child_name
import phono2ortho as po

def clean_phono2ortho(p2o):
    dic=defaultdict(type(p2o))
    for key in p2o:
        if type(p2o[key])==str:
            dic[key]=p2o[key]
    print("################          AFTER CLEANING   ############")
    for key in dic:
        if type(key)!=str:
            print(key,dic[key])
    return(dic)

tmp_path = po.return_rootd()
p2o = po.return_dic(tmp_path)
phono2ortho = clean_phono2ortho(p2o)

#child = return_child_name()
child = 'wil'
json_path = "./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp/"+child+"_datas.json"
word2oseg_phono = json.loads(open(json_path,encoding="utf8").read())
word2phone_phono = wp.read_tags_and_golds("./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp/results_do_concat_prov")

phonorules = {'aa': ['a','o'],
'ae':['a'],
'ah':['u','o','ou'],
'ao':['aw','oo','a'],
'aw': ['ow','ou'],
'ax':['a','e','u','i','o','l'],
'ay':['i','y','igh'],
'eh':['e','ea','ai'],
'el':['le'],
'em':['em','m'],
'en':['en'],
'er':['er','ear','u','re','ir','or','orr'],
'ey':['a','ay','ai','ea'],
'ih':['i','ee','a'],
'iy':['ea','ee','ey','y','e'],
'ow':['o','oa'],
'oy':['oy'],
'uh':['u','oo','ou'],
'uw':['oo','u','ew','ui'],
'b':['b','bb'],
'ch':['ch','tch'],
'd':['d','dd','ed','t'],
'dh':['th'],
'f':['f','ff'],
'g':['g','gg'],
'hh':['h','hh'],
'jh':['g','j','gg','jj'],
'k':['c','ck','k','cc','kk','ke','x'],
'l':['l','ll','le','e'],
'm':['m','mm','me'],
'n':['n','nn','ne'],
'ng':['ng'],
'p':['p','pp'],
'r':['r','rr'],
's':['s','ss','ce','c','e'],
'sh':['sh'],
't':['t','tt','ed','te','d'],
'th':['th'],
'v':['v','vv'],
'w':['w','ww','wh'],
'y':['y','yy','u'],
'z':['z','s'],
'zh':['s','ss'],
'pau':['']
}

def idk():
    word2phone_ortho = defaultdict(list)
    for entry in word2phone_phono: #entry  = "hhelow"
        if entry in phono2ortho:#CH
            phons= word2phone_phono[entry] #phons = ["hh","e","l","ow"]
            ortho_word = phono2ortho[entry] #ortho_word = "hello"
            tmp_list = []
            if ortho_word!= []:
                for phon in phons : 
                    tmp_list.append(phonorules[phon])
                word2phone_ortho[ortho_word] = tmp_list
        print("entry for computer",word2phone_ortho["computer"])
    return word2phone_ortho

def remove_empty_char(dico):
    dic = defaultdict(type(dico))
    for cle in dico :
        newval = []
        for elt in dico[cle]:
            newlist = []
            for char in elt : 
                if char!='':
                    newlist.append(char)
            newval.append(newlist)
        dic[cle]=newval
    return dic

#dico_test = {"honey":[["h"],["u","o"],["n","n"],["ee","ea","ey"]]}

def cleaning_transcripts(dico):
    newdic = defaultdict(list)
    l = []
    for cle in dico :
        if cle=='computer':
            print("COMPUTER IS:",dico[cle])
        word=""
        list_words=[]
        treat = dico[cle]
        i=0
        elt=treat[i]
        while len(elt)==1 and i<len(treat)-1:
            add = '-'+elt[0]
            word+=add
            i+=1
            elt=treat[i]
        list_words.append(word)
        while i<len(treat):
            tmpw = list_words
            newlist=[]
            for w in tmpw:
                for opt in elt :
                    if opt!='': 
                        neword =w+'-'+opt
                        newlist.append(neword)
            i+=1
            if i<len(treat):
                elt=treat[i]
            list_words = newlist
        if cle=='computer':
            print("LOOK AT HERE ",cle,list_words)
        good_transcript = search_transcript(cle,list_words)
        if good_transcript != None :
            good_transcript = good_transcript[1:].split('-')
            newdic[cle]= good_transcript
        """
        else : 
            newdic[cle]=[]
        """
    return newdic

#def help_transcript(cle,list_words):

def search_transcript(cle,list_words):
    iter=0
    while iter<len(list_words):
        w = list_words[iter].split('-')
        nw = ""
        for elt in w:
            nw+=elt 
        if nw==cle.lower() : 
            return(list_words[iter])
        elif nw==cle[:-1] and cle[-1]=='e':
            modif = list_words[iter]+'-e'
            return(modif)
        iter+=1
        #orth= [phonorules[cle] for cle in phon] #orth = ["h","e","ll","o"]
        
        #word2phone_ortho[]
#dic = idk()

def return_word2phon_ortho():
    return(cleaning_transcripts(idk))

word2phon_ortho = cleaning_transcripts(idk())

#word2phon_ortho = cleaning_transcripts(idk())
#print(word2phon_ortho)
#print(phono2ortho["seyaxng"])
#print(word2phone_phono["seyaxng"])
#print("ICI",word2phon_ortho["honey"])
for elt in word2phon_ortho:
    if word2phon_ortho[elt]==[]:
        #print(elt)
        for x in phono2ortho:
            if phono2ortho[x]==elt:
                print(elt,x,word2phone_phono[x])
print(len(word2phone_phono))
print(len(word2phon_ortho))
count=0
for cle in word2phon_ortho:
    if word2phon_ortho[cle]!=[]:
        count+=1
print(count)

#pb: la premiere partie est recuperee mais mauvaise indiciation ensuite ? ew : 'coloring': [[['co','coloring'],2]]
def built_word2oseg_ortho():
    word2oseg_ortho = [] #list of dict of oseg (1 per algorithm)
    word2oseg_ortho_dict = defaultdict(list)
    for algorithm in word2oseg_phono:
        for word in algorithm:
            #print("word type",type(word)," word=",word)
            if word in phono2ortho:
                if phono2ortho[word] in word2phon_ortho and len(word2phon_ortho[phono2ortho[word]])==len(word2phone_phono[word]):
                    for oseg in algorithm[word]:
                        osegg = oseg[0]
                        oseg_ortho=[]
                        chain,orthochain = "",""
                        idx_phon,idx_in_oseg=0,0
                        while idx_in_oseg<len(osegg):
                            while chain != osegg[idx_in_oseg] and idx_phon<len(word2phone_phono[word]):
                                chain+=word2phone_phono[word][idx_phon]
                                orthochain+=word2phon_ortho[phono2ortho[word]][idx_phon]
                                idx_phon+=1
                            idx_in_oseg+=1
                            #CH idx_phon=0
                            oseg_ortho.append(orthochain)
                            orthochain,chain="",""
                        osego = [oseg_ortho,oseg[1]]
                        word2oseg_ortho_dict[phono2ortho[word]].append(osego)
                        idx_phon=0
        word2oseg_ortho.append(word2oseg_ortho_dict)
        word2oseg_ortho_dict = defaultdict(list)    
    return(word2oseg_ortho)
#print("###################################################################################")
#print("WORD 2 OSEG ORTHOGRAPHIC DICTIONNARY")
#print(built_word2oseg_ortho())
#print("WORD 2 PHONE PHONOLOGICAL DICTIONARY")
#print(word2phone_phono)
#print("#################################################################################")
#print("WORD 2 PHONE ORTHOGRAPHIC DICTIONARY")
#print(word2phon_ortho)
#print("###################################################################")



#------------------------------------------------ IGNORER LA CASSE
#---------Description des tâches à effectuer : 
 #1)FAIT. créer un dico clé = hhelow value = hello
 #2) créer un dico clé = hello value = ['h','e'','ll','o']
 #3)FAIT. créer un dico clé= hhelow value = ['hh','e','l','ow] --> recuperable dans les fic "tags"
 #4) pour chaque oseg ex ['hhe','low']:
#       créer la chaine ortho correspondante : ortho[0]=2[0] if 3[0] != 4[0] then ortho[0]+=2[1]
#   si decoupage_en_morphemes_gold est dans la liste des chaines ortho :
#   analyse (compte,classement)
#5) recuperer les datas des autres enfants(child_datas.json) 3 manquants