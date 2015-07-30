__author__ = 'leon'

import linecache
import os
import sys
import getopt
import random
import json




opts, args = getopt.getopt(sys.argv[1:],"m:b:i:t:s:y:",["malware=","benign=","input=","test_num=","static=","dynamic="])
for op, value in opts:


    if op in ("-m","--malware"):
        malware = value

    if op in ("-b","--benign"):
        benign = value

    if op in ("-i","--input"):
        input = value

    if op in ("-t","--test_num"):
        test_num = value


    if op in ("-s","--static"):
            static = value

    if op in ("-y","--dynamic"):
            dynamic = value




os.system("python /home/leon/PycharmProjects/bullshitproject_svm/generate_result.py -d "+malware+" -o m"+" -s "+static+" -y "+dynamic)
os.system("python /home/leon/PycharmProjects/bullshitproject_svm/generate_result.py -d "+benign+" -o b"+" -s "+static+" -y "+dynamic)

count_mal = len(open(malware+'/mal_gresult','rU').readlines())
count_ben = len(open(benign+'/ben_gresult','rU').readlines())
finput = open(input,"a+")

for i in range(1,count_mal+1):
    line = linecache.getline(malware+'/mal_gresult', i)
    finput.write(line)


for i in range(1,count_ben+1):
    line = linecache.getline(benign+'/ben_gresult', i)
    finput.write(line)


os.system("python /home/leon/PycharmProjects/bullshitproject_svm/svm.py -d "+malware+"/mal_gresult -t "+test_num)
os.system("python /home/leon/PycharmProjects/bullshitproject_svm/svm.py -d "+benign+"/ben_gresult -t "+test_num)












