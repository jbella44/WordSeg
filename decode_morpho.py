import os
from collections import defaultdict

global affixes
global type_of_affixes
global pos_codes 

affixes = defaultdict(str)
type_of_affixes = {"#":"prefix","-":"sufix","&":"fusional"}
affixes = { 
    "CP":['er','r'],
    "SP":['est','st'],
    "DIM":['ie'],
    "PL":['s','es'],
    "POSS":["'s","'"],
    "3S":['s','es'],
    "PAST":["ed","d"],
    "PRESP":["ing"],
    "PASTP":["en"],
    "UN":["un"],
    "LY":["ly"],
    "ER":["ex"],
    "DIS":["dis"],
    "MIS":["mis"],
    "OUT":["out"],
    "OVER":["over"],
    "PRE":["pre"],
    "PRO":["pro"],
    "RE":["re"]
}
pos_codes = ["n","v","co"]
