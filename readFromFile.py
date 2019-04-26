import os
import math
import argparse
import numpy as np
from core import Symbol
import core
from encoder import encode
from decoder import decode

def readFromFile(subdirectoryName): 
    f = open("demofile.txt", "r")
    file_symbols1 = []
    print("___________________________read & build from file start______________________________")
    file_meta = f.read()
    file_meta = file_meta.split(";;")
    file_meta = file_meta[:-1]
    for file_meta_part in file_meta:
        file_meta_part = file_meta_part.split(";")
        dir = os.path.dirname(__file__)
        dataArray = np.load(os.path.join(dir, subdirectoryName + "/"+ file_meta_part[2]))
        file_meta_part[0] = int(file_meta_part[0])
        file_meta_part[1] = int(file_meta_part[1])
        file_symbols1.append(Symbol(index=file_meta_part[0], degree=file_meta_part[1], data=dataArray))
    # print("=====")
    print("____________________________read & build from file end______________________________")
    f.close()
    return file_symbols1