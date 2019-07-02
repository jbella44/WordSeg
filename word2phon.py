from collections import defaultdict
import os 

child = 'wil'
global word2phone 
word2phone = defaultdict(list)

def read_tags_and_golds(rootd):
    for subdir in os.listdir(rootd):
        subdir_split = subdir.split("-")
        if len(subdir_split)>1 and subdir_split[0]==child: 
            chemin = rootd+'/'+subdir
            if os.path.isdir(chemin)==True : 
                gold_path = chemin+'/'+'gold.txt'
                tags_path = chemin+'/'+'tags.txt'
                if os.path.isfile(gold_path)  ==True and os.path.isfile(tags_path)==True: 
                    g = open(gold_path,encoding="utf8")
                    t = open(tags_path,encoding="utf8")
                    golds = g.readlines()
                    tags = t.readlines()
                    create_dict_word_to_phon(word2phone,golds,tags)
    return word2phone
"""
def test_function():
    g = open("./results_do_concat_prov/eth-1-phone-ag/gold.txt",encoding="utf8")
    t = open("./results_do_concat_prov/eth-1-phone-ag/tags.txt",encoding="utf8")
    tags = t.readlines()
    golds = g.readlines()
    print(type(tags))
    print(type(tags[0]))
    print(golds[0])
    return golds,tags
    gs = ["hello world"]
    ts = ["he ;esyll; llo ;esyll; eword; w aa"]
    for g,t in zip(gs,ts):
        print("g",g)
        print("t",t)
        g = g.split(" ")
        t = t.split("eword")
        print(g)
        print(t)

g,t =test_function()
#test_function()
"""
def create_dict_word_to_phon(word2phone,gold,tag):
    for t_sent,g_sent in zip(tag,gold):
        t_sent = t_sent.split("eword")
        g_sent = g_sent.split(" ")
        for t_elt,g_elt in zip(t_sent,g_sent) :
            dict_key = g_elt.strip('\n')
            t_elt = t_elt.split(";esyll")
            t = []
            phon = []
            for syll in t_elt :
                inter = syll.split(" ")
                list_to_append = []
                for elt in inter : 
                    if elt.isalpha():
                        list_to_append.append(elt)
                t.append(list_to_append)
            for i in range(len(t)):
                phon+= t[i]
            if dict_key not in word2phone:
                word2phone[dict_key]= phon

