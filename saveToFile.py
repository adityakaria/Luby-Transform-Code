import os
import math
import argparse
import numpy as np
from core import Symbol
import core
from encoder import encode
from decoder import decode

def saveToFile(file_blocks, drops_quantity, subdirectoryName):
    f = open("demofile.txt", "w")
    print("________________________encode & write to file start_________________________________")
    for curr_symbol in encode(file_blocks, drops_quantity=drops_quantity):
        f.write(str(curr_symbol.index) + ";" + str(curr_symbol.degree) + ";" + str(curr_symbol.index) + "-" + str(curr_symbol.degree) + ".npy" + ";;")
        dir = os.path.dirname(__file__)
        np.save(os.path.join(dir, subdirectoryName + "/" + str(curr_symbol.index) + "-" + str(curr_symbol.degree)), curr_symbol.data)
    print("_________________________encode & write to file end_________________________________")
    f.close()