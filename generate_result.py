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

directory=_directory

result=""
for item in os.listdir(directory):
     smalipath = directory + os.sep + item
     print smalipath
     if os.path.isdir(smalipath):
         os.system("python bullshit_staticanalysis.py -d "+smalipath)
         os.system("python dynamicanalysis.py -d "+smalipath)
         os.system("python get_final.py -d "+smalipath)

         filename= smalipath+'/result.json'
         f = file(filename)
         s1 = json.load(f)
         f.close










