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



os.system('python /home/leon/PycharmProjects/bullshitproject_svm/svm_auto.py -m '+malware+' -b '+benign+' -i '+input+' -t '+test_num+' -s '+static+' -y '+dynamic)
os.system('cp /home/leon/Downloads/test_709/random_train_1 /home/leon/libsvm-master/tools/random_train_1')
os.system('cp /home/leon/Downloads/test_709/random_test_1 /home/leon/libsvm-master/tools/random_test_1')


os.system('cd /home/leon/libsvm-master/tools && python easy.py random_train_1 random_test_1')

os.system('cd /home/leon/libsvm-master && ./svm-predict /home/leon/Downloads/test_709/input /home/leon/libsvm-master/tools/random_train_1.model /home/leon/Downloads/test_709/output')

os.system('python /home/leon/PycharmProjects/bullshitproject_svm/svm_result.py -t /home/leon/Downloads/test_709/input -p /home/leon/Downloads/test_709/output')

os.system('rm /home/leon/Downloads/test_last/benign_result/ben_gresult /home/leon/Downloads/test_last/malware_result/mal_gresult /home/leon/Downloads/test_709/input')

os.system('rm /home/leon/Downloads/test_709/output /home/leon/Downloads/test_709/random_test_1 /home/leon/Downloads/test_709/random_train_1')

os.system('rm /home/leon/libsvm-master/tools/random_test_1 /home/leon/libsvm-master/tools/random_train_1 /home/leon/libsvm-master/tools/random_train_1.range')

os.system('rm /home/leon/libsvm-master/tools/random_train_1.scale /home/leon/libsvm-master/tools/random_test_1.predict')

os.system('rm /home/leon/libsvm-master/tools/random_test_1.scale /home/leon/libsvm-master/tools/random_train_1.model /home/leon/libsvm-master/tools/random_train_1.scale.out')


os.system('rm /home/leon/libsvm-master/tools/random_train_1.scale.png')












