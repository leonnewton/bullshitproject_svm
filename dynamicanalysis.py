__author__ = 'leon'

import os
import sys
import getopt
import json







if __name__ == "__main__":
    #_directory = raw_input("input the directory where you put the file : ")

    opts, args = getopt.getopt(sys.argv[1:],"d:h","directory=help")
    for op, value in opts:
        if op in ("-d","--directory"):
            _directory = value


dynamic=[0]*51

filename= _directory+'/hooklog'
for line in file(filename):
    #print line[0:2]
    #print "number",int(line[0:2])
    index=int(line[0:2])
    dynamic[index]=1



'''for i in range(1,51):
    print i,"",dynamic[i]'''


f = open(_directory+"/dynamic.json","w")
f.write(json.dumps(dynamic))
f.close()
