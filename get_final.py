__author__ = 'leon'

import sys
import getopt
import json



if __name__ == "__main__":
    #_directory = raw_input("input the directory where you put the file : ")

    opts, args = getopt.getopt(sys.argv[1:],"d:h","directory=help")
    for op, value in opts:
        if op in ("-d","--directory"):
            _directory = value




filename= _directory+'/static.json'


f = file(filename)
s1 = json.load(f)
f.close



filename= _directory+'/dynamic.json'


f = file(filename)
s2 = json.load(f)
f.close


s=[0]*51
for i in range(1,51):
    s[i]=s1[i] or s2[i]



f = open(_directory+"/result.json","w")
f.write(json.dumps(s))
f.close()



#print "s1",s1
#print "s2",s2
#print "s",s






