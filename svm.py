__author__ = 'leon'



import linecache
import os
import sys
import getopt
import random
import json



opts, args = getopt.getopt(sys.argv[1:],"d:h","directory=help")
for op, value in opts:
    if op in ("-d","--directory"):
        _directory = value


outnum = 20

count = len(open(_directory,'rU').readlines())


which = random.sample(range(1,count+1),outnum)


fgresult = open("/media/LEON/random_test_4","a+")


for i in range(outnum):
    print which[i]
    line = linecache.getline(_directory, which[i])
    fgresult.write(line)

fgresult.close()