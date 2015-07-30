__author__ = 'leon'

import sys
import getopt
import json



if __name__ == "__main__":
    #_directory = raw_input("input the directory where you put the file : ")

    opts, args = getopt.getopt(sys.argv[1:],"d:s:y:",["directory=","static=","dynamic="])
    for op, value in opts:
        if op in ("-d","--directory"):
            _directory = value

        if op in ("-s","--static"):
            static = value

        if op in ("-y","--dynamic"):
            dynamic = value

static_num = int(static)
dynamic_num = int(dynamic)


print static_num,dynamic_num


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
    s[i]=static_num*s1[i] + dynamic_num*s2[i]



f = open(_directory+"/result1.json","w")
f.write(json.dumps(s))
f.close()



#print "s1",s1
#print "s2",s2
#print "s",s






