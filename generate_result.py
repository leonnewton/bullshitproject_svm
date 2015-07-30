__author__ = 'leon'

import os
import sys
import getopt
import json


    #_directory = raw_input("input the directory where you put the file : ")
opts, args = getopt.getopt(sys.argv[1:],"d:o:s:y:",["directory=","option=","static=","dynamic="])
for op, value in opts:
        if op in ("-d","--directory"):
            _directory = value

        if op in ("-o","--option"):
            option = value

        if op in ("-s","--static"):
            static = value

        if op in ("-y","--dynamic"):
            dynamic = value




directory=_directory

if option == 'm':
    fgresult = open(_directory+"/mal_gresult","a+")
else:
    fgresult = open(_directory+"/ben_gresult","a+")


result=""
for item in os.listdir(directory):
     smalipath = directory + os.sep + item
     print smalipath
     if os.path.isdir(smalipath):
         os.system("python static_analysis.py -d "+smalipath)
         os.system("python dyna_test.py -d "+smalipath)
         os.system("python get_final.py -d "+smalipath+" -s "+static+" -y "+dynamic)

         filename= smalipath+'/result1.json'
         f = file(filename)
         s1 = json.load(f)
         f.close
         print s1,type(s1)
         tmp=""
         if option == 'm':
            print 'mal'
            tmp="1 "+tmp
         else:
            print 'ben'
            tmp="2 "+tmp
         for i in range(1,51):
             tmp=tmp+str(i)+":"+str(s1[i])+" "
         print "tmp",tmp
         fgresult.write(tmp+"\n")




fgresult.close()



