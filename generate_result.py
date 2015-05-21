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


fgresult = open(_directory+"/ben_gresult","a+")


result=""
for item in os.listdir(directory):
     smalipath = directory + os.sep + item
     print smalipath
     if os.path.isdir(smalipath):
         os.system("python static_analysis.py -d "+smalipath)
         os.system("python dynamic_analysis.py -d "+smalipath)
         os.system("python get_final.py -d "+smalipath)

         filename= smalipath+'/result.json'
         f = file(filename)
         s1 = json.load(f)
         f.close
         print s1,type(s1)
         tmp=""
         tmp="2 "+tmp
         for i in range(1,51):
             tmp=tmp+str(i)+":"+str(s1[i])+" "
         print "tmp",tmp
         fgresult.write(tmp+"\n")




fgresult.close()



