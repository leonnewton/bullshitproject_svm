
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




testfile= _directory+'/random_test_2'
prefile= _directory+'/random_test_2.predict'

count = len(open(testfile,'rU').readlines())


count_wubao = 0
count_shiji_ben = 0
count_shiji_mal = 0
count_jianchu = 0
for i in range(1,count+1):
    line_test = linecache.getline(testfile, i)
    line_pre = linecache.getline(prefile, i)
    #print i,'line_test',line_test[0]
    #print i,'line_pre',line_pre[0]
    linetest = int(line_test[0])
    linepre = int(line_pre[0])
    #print linetest,linepre
    if linetest == 2:
        count_shiji_ben = count_shiji_ben + 1

    if linetest == 1:
        count_shiji_mal = count_shiji_mal + 1


    if linetest == 2 and linepre == 1:
        count_wubao = count_wubao + 1

    if linetest == 1 and linepre == 1:
        count_jianchu = count_jianchu + 1

print count_wubao,count_shiji_ben
index_wubao = float(count_wubao)/float(count_shiji_ben)
index_jianchu = float(count_jianchu)/float(count_shiji_mal)
print "wubao",index_wubao
print "jianchu",index_jianchu





























