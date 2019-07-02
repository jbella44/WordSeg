import os 
from collections import defaultdict
import decode_morpho as dm
from ortho2morpho import return_dic
from read_folder import return_child_name
from all_correspondences import built_word2oseg_ortho

global word2morpho
global child 
child = return_child_name()
word2morpho = return_dic(child)

global word2oseg_ortho
word2oseg_ortho = built_word2oseg_ortho()

global nb2algo
nb2algo = {
    0: "tpabs",
    1:"tprel",
    2:"puddle",
    3:"dibs",
    4:"ag",
    5:"00",
    6:"05",
    7:"10"
    }

global prefix_res
global suffix_res
global pre_suf_res

prefix_res = defaultdict(list)
suffix_res = defaultdict(list)
pre_suf_res = defaultdict(list)
    

def rewrite_morpho(word2morpho):
    for word in word2morpho:
        m_word = word2morpho[word][0].split('|')
        print(m_word)
        for x in m_word:
            idx_x = m_word.index(x)
            for affix in dm.affixes:
                if affix in x:
                    for elt in dm.affixes[affix]:
                        tmp = x.replace(affix,elt)
                        #print(word,m_word,tmp)
                        len_aff = len(elt)
                        if elt == word[-len_aff:]:
                            #x = tmp
                            m_word[idx_x] = tmp
        mword = ""
        for elt in m_word:
        mword = mword+elt+('|')
        word2morpho[word][0] = mword
    return word2morpho

word2morpho = rewrite_morpho(word2morpho)


####NB : Les lettres doublées avant un suffixe ne le sont pas ! ex: "stop-ing"
def treat_oseg():
    for algo in word2oseg_ortho:
        idx_algo = word2oseg_ortho.index(algo)
        pre_path = "./English/wsexp.zi_/wsexp/newres/scratch2/mbernard/experiments/wsexp/"+child+"-prefixes-"+nb2algo[idx_algo]+".txt"
        prefile = open(pre_path,encoding="utf8")
        store_res_per_arlgorithm(algo,idx_algo)

def store_res_per_arlgorithm(word2oseg_o,idx_algo):     
    for word in word2oseg_o:
        for oseg in word:
##a continuer later