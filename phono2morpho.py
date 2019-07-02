import os 
from collections import defaultdict
from read_folder import return_child_name

global child
child =return_child_name
rootd = "."

def read_cha_files(child):
    for subdir in os.listdir(rootd):
        
