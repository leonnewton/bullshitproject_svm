__author__ = 'leon'



import linecache
import os
import sys
import getopt
import random
import json



opts, args = getopt.getopt(sys.argv[1:],"d:t:",["directory=","test_num="])
for op, value in opts:
    if op in ("-d","--directory"):
        _directory = value

    if op in ("-t","--test_num"):
        test_num = value


print type(test_num),int(test_num)

outnum = int(test_num)

count = len(open(_directory,'rU').readlines())

print "count",count
which = random.sample(range(1,count+1),outnum)

print "which",which

ftrain = open("/home/leon/Downloads/test_709/random_train_1","a+")
ftest = open("/home/leon/Downloads/test_709/random_test_1","a+")

#ftrain = open("/media/LEON/random_train_1","a+")
#ftest = open("/media/LEON/random_test_1","a+")

line = linecache.getline(_directory, 0)
print "dijihang",line

for i in range(outnum):
    print "train",which[i],'i',i
    line = linecache.getline(_directory, which[i])
    ftrain.write(line)
for i in range(1,count+1):
    if i not in which:
        print "test",i
        line = linecache.getline(_directory, i)
        ftest.write(line)


ftrain.close()
ftest.close()
