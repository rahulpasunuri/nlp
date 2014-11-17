##this file is the tools that will constantly be used by other files.
##1. write_csv(filename,listOfNumbers)  
##
##
##
#import sklearn
#from sklearn import preprocessing as prep
import numpy as np
import sys
def write_csv(filename,numbers):
    numbers
    lines = [ str(x) + "\n"  for x in numbers]
    OUT = open(filename+".csv","w")
    OUT.writelines(lines)
    OUT.close()


def normalize_columns(arr):
    rows, cols = arr.shape
    for col in xrange(cols):
        mm = abs(arr[:,col]).max()
        if mm  ==0:
           arr[:,col] = 0
        else: 
           arr[:,col] /= mm
    return  arr

def normalize_list(matrix):
    """ Normalize a list of list and make it into a list """
    arr = np.array(matrix)
    normm = normalize_columns(arr)
    normm = normm.tolist()
    return normm


if __name__ == "__main__":
    m = [
        [-2.0,3.0,0.0,0.0,5.0],
        [1.0,0.0,5.0,0.0,0.0],
        [3.0,0.0,3.0,-4.0,-2.0],
        [2.0,-3.0,0.0,0.0,-5.0],
        [-1.0,0.0,-5.0,0.0,0.0],
        [-3.0,0.0,-3.0,4.0,2.0]
        ]

    norm = normalize_list(m)
    print norm




