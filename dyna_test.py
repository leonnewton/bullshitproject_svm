__author__ = 'leon'

import os
import sys
import getopt
import json
import string




opts, args = getopt.getopt(sys.argv[1:],"d:h","directory=help")
for op, value in opts:
    if op in ("-d","--directory"):
        _directory = value

dynamic=[0]*51

filename= _directory+'/pid.txt'
for line in file(filename):
    line=line.strip('\n')
    result = ' '.join(line.split())
    result = result.split(' ')
    print result
    pid = int(result[1])



test = 'APICALL'




filename1= _directory+'/log'
i = 1
for line in file(filename1):

        i = i + 1
        APICALL = 0
        pid_eq = 0
        line = line.strip('\n')

        result = line.split('(')

        result = result[0].split('/')

        result1 = result[1]

        if 'APICALL' in result1:

            APICALL = 1





        result = line.split('(')
        result = result[1]
        result = result.split(')')
        pid_test = int(result[0])
        #print 'pid_test',pid_test

        if pid_test == pid:
            pid_eq = 1


        if APICALL == 1  and pid_eq == 1:
            result = line.split(':')
            result = result[1].split(' ')
            dynamic_number = int(result[1])
            print dynamic_number
            dynamic[dynamic_number ]=1
            #print      dynamic[dynamic_number ]



f = open(_directory+"/dynamic.json","w")
f.write(json.dumps(dynamic))
f.close()
