__author__ = 'leon'

import linecache

import linecache
import os
import sys
import getopt
import random
import json

opts, args = getopt.getopt(sys.argv[1:],"t:p:",["test=","predict="])
for op, value in opts:
     if op in ("-t","--test"):
        test_file = value

     if op in ("-p","--predict"):
        predict_file = value




#ftest = "/home/leon/Downloads/libsvm-master/tools/random_test_4"
#fpredict = "/home/leon/Downloads/libsvm-master/tools/random_test_4.predict"

ftest = test_file
fpredict = predict_file

count = len(open(fpredict,'rU').readlines())

#print count

count_benign = 0
count_wubao = 0
wubao = 0
count_malware = 0
count_jianchu = 0
for i in range(1,count+1):
    line_predict = linecache.getline(fpredict, i)
    line_test = linecache.getline(ftest,i)
    #print line_test[0],line_predict[0]
    if line_test[0] == '2':
        count_benign = count_benign + 1

    if line_test[0] == '1':
        count_malware = count_malware +1


    if (line_test[0] == '2') and (line_predict[0] == '1'):
        count_wubao = count_wubao + 1

    if (line_test[0] == '1') and (line_predict[0] == '1'):
        count_jianchu =count_jianchu + 1





if count_wubao == 0:
    wubao = 0

else:
    wubao = float(count_wubao)/float(count_benign)


if count_jianchu == 0:
    jianchu = 0
else:
    jianchu = float(count_jianchu)/float(count_malware)


print "count_benign",count_benign
print "count_malware",count_malware
print "count_wubao",count_wubao
print "count_jianchu",count_jianchu
print "wubao",wubao
print "jianchu",jianchu