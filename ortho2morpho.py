import os 
from collections import defaultdict
from read_folder import return_child_name
import all_correspondences as ac

global child
#child = return_child_name()
rootd = "./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp"
child = 'wil'

#word2phon_ortho = ac.return_word2phon_ortho()
word2oseg_ortho = ac.built_word2oseg_ortho()
#print(word2oseg_ortho)
print("**************",type(child))
def read_cha_files(child):
    cha_files = []
    #vart=0
    for subdir in os.listdir(rootd):
        if subdir==child+'_mor': #and vart==0
            subdir_path = rootd+'/'+subdir
            for f in os.listdir(subdir_path):
                #if vart<2:
                f_path = subdir_path + '/' +f
                extension = f.split(".")[1]
                if os.path.isfile(f_path) and extension=="txtin":
                    cha_file = open(f_path,encoding="utf8")
                    cha_f = cha_file.readlines()
                    #print(cha_f)
                    cha_f = cha_f[6:-1]
                    cha_files.append(cha_f)
    #                    vart+=1

    return(cha_files)


"""
def built_word_to_morpho(cha_files):
    word2morpho = defaultdict(list)
    for cf in cha_files:
        idx_txt,idx_gra = 0,3
        while idx_gra<=len(cf):
            print(cf[idx_txt:idx_gra])  
            treat_sentence(word2morpho,cf[idx_txt:idx_gra])
            idx_txt+=3
            idx_gra+=3
   """     
def built_word_to_morpho(cha_files):
    word2morpho= defaultdict(list)
    sent_datas = []
    txt,mor,gra=0,0,0
    for cf in cha_files:
        sent_datas.append(("txt",cf[0]))
        txt,mor,gra=0,0,0#add
        for sent in cf[1:] : 
            line_data = sent.split(":")[0]
            if line_data == "%mor":
                sent_datas.append(("mor",sent))
                mor = 1
            elif line_data=="%gra":
                sent_datas.append(("gra",sent))
                gra = 1
            elif line_data!="*TXT" and line_data!="%mor" and line_data!="%gra":
                if mor==1 and gra==0: #and add
                    sent_datas.append(("mor",sent))
                    #mor=0 
                elif gra==1:
                    sent_datas.append(("gra",sent))
                    #gra=0
                else:
                    print("error occured:",line_data)
            elif line_data=="*TXT":
                txt,mor,gra = store_sentence(sent_datas) #str
                word2morpho = treat_sentence(word2morpho,txt,mor,gra)
                sent_datas=[("txt",sent)]
                gra=0
            else : 
                print("a case has been forgotten",print(line_data))
    return(word2morpho)

def store_sentence(sent_datas): #contient les lignes TXT,MOR et GRA pour une ligne à traiter
    txt,mor,gra=[],[],[] 
    for data in sent_datas:
        print(type(data))
        if data[0]=="txt":
            txt.append(data[1])
        elif data[0]=="mor":
            mor.append(data[1])
        else : 
            gra.append(data[1])
    print("*******IN STORE SENTENCES*****",txt,mor,gra)
    txt,mor,gra = datas_fusion(txt,mor,gra)
    #print(txt)
    print("in treat sentence:",txt,mor,gra)
    return(txt,mor,gra) #str

def datas_fusion(txt,mor,gra):
    new_txt = txt[0].strip('\n')
    new_mor = mor[0].strip('\n')
    new_gra = gra[0].strip('\n')
    for i in range(len(txt)):
        if i>0:
            new_txt = new_txt+" "+txt[i][1:]
    new_txt = new_txt[5:].strip('\t')
    for i in range(len(mor)):
        if i>0:
            new_mor = new_mor+" "+mor[i][1:]
    new_mor = new_mor[5:].strip('\t')
    for i in range(len(gra)):
        if i>0:
            new_gra= new_gra+ " "+gra[i][1:]
    new_gra = new_gra[5:].strip('\t')
    return new_txt,new_mor,new_gra #str

def treat_sentence(word2morpho,txt,mor,gra):
    txt = txt.split(" ")
    mor = mor.split(" ")
    gra = gra.split(" ")
    if len(mor)!=len(txt) or len(mor)!= len(gra) or len(gra)!=len(txt):
        print("SYSTEM ERROR",len(txt),len(mor),len(gra))
        print(txt)
        print(mor)
        print(gra)
    #######"len(txt = len(mor) mais len(gra) est != (pas la même separation pr les deps)"
    for i in range (len(txt)):
        for algo in word2oseg_ortho:
            if txt[i] in algo:
                if txt[i] not in word2morpho:
                    word2morpho[txt[i]]= [mor[i],gra[i]]
    return word2morpho

def return_dic(child):
    cf = read_cha_files(child)
    return(built_word_to_morpho(cf))
    """
print(word2oseg_ortho[0]["weekend"])
print(word2oseg_ortho[1]["saying"])
print(word2oseg_ortho[1]["butterfly"])

print("###################    RECHERCHE DE PATTERNS      ########################")
for algo in word2oseg_ortho:
    for word in algo:
        if word in word2morpho:
            print(word, algo[word],word2morpho[word])

"""