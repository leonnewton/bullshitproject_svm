__author__ = 'leon'

import linecache
import os
import sys
import getopt
import random
import json



opts, args = getopt.getopt(sys.argv[1:],"i:m:o:",["input=inp","model=","out="])
for op, value in opts:


    if op in ("-i","--input"):
        input_name = value

    if op in ("-m","--model"):
        model = value

    if op in ("-o","--out"):
        out = value


print input_name,model

scale_file = input_name+'.scale'
os.system("/home/leon/libsvm-master/svm-scale "+input_name+" > "+scale_file)

os.system("/home/leon/libsvm-master/svm-predict "+scale_file+" "+model+" "+out)

os.system("python /home/leon/PycharmProjects/bullshitproject_svm/calc.py -t "+input_name+" -p "+out)
os.system("python /home/leon/PycharmProjects/bullshitproject_svm/svm_result.py -t "+input_name+" -p "+out)

























