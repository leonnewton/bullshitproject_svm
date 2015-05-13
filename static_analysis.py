__author__ = 'leon'


"""
@AUTHOR: Wendan Kang
@VERSION: 1.6
@FUNCTION: 1. Compare permission and sensitive API to make final list ( first ten elements);
           2. Detect Dynamic Loading (the eleventh element);
           3. Detect Root ( the twelfth element);
           4. Ad or not;
           5. Icon or not.
           6. Extra permission detect.
@NOTE: Input: python ../SensitiveBehaviorDectector.py -d diretory
       Output: 1. List of sensitive final record (.json)
               2. List of sensitive permission record (.json)
               3. List of the path (.json)
"""

import os
import sys
import getopt
import json
from xml.dom import minidom


# the struct for later output ---- which sensitive behave exist in which smali(use path to represent it)
class PathToBehave:

    Path = ''
    Behave =  [0]*51


    def __init__(self,_path,_Behave):
        self.Path = _path
        self.Behave = _Behave

class permissionTag:
    permissionName = ''
    tag = ''

    def __inti__(self, _permisionName, _tag):
        self.permissionName = _permisionName
        self.tag = _tag


class Detect_Sensitive_Behavior:

    directory = ''               #carry the file directory
    smalipath = ''               #temporary, carry every smali path which contains sensitive behavior
    Sensitive_Behavior =   [0]*51  #temporary, carry every smali's behavior record
    _FinalSenBehavior =     [0]*51     #all sensitive behaviors the whole file contains
    SensitiveWord = ["",
                    "File;->exists",
                    "getDeviceId",
                    "getSubscriberId",
                    "getCurrentPhoneType",
                    "getAction",
                    "startService",
                    "getOriginatingAddress",
                    "getMessageBody",
                    "getLine1Number",
                    "sendTextMessage",
                    "File;->mkdir",
                    "abortBroadcast",
                    "getSimSerialNumber",
                    "getRunningServices",
                    "Runtime;->exec",
                    "setComponentEnabledSetting",
                    "getSharedPreferences",
                    "getSimOperator",
                    "Class;->forName",
                    "getDisplayMessageBody",
                    "getDisplayOriginatingAddress",
                    "getInstalledPackages",
                    "getNetworkOperatorName",
                    "sendBroadcast",
                    "ProcessManager;->exec",
                    "DexClassLoader;-><init>",
                    "system;->loadDex",
                    "loadUrl",
                    "Intent;->putExtra",
                    "getCellLocation",
                    "FileReader;-><init>",
                    "NetworkInfo;->isConnected",
                    "PowerManager;->release",
                    "PowerManager;->acquire",
                    "Timer;->scheduleImpl",
                    "getRunningTasks",
                    "getSimOperatorName",
                    "Log;->d",
                    "openFileOutput",
                    "getPhoneType",
                    "getSimCountryIso",
                    "setWifiEnabled",
                    "startActivityForResult",
                    "SystemProperties;->get",
                    "getMacAddress",
                    "setLatestEventInfo",
                    "stopService",
                    "sendMultipartTextMessage",
                    "NotificationManager;->notify",
                    "getNetworkType"
]

    RootWord = ["getRuntime()", "exec", "\"su\""]

    _root = [0,0,0]
    _pathToBehaveArray = []          #the list of class PathToBehave, to record every smali that has sensitive words
    countForSenSmali = -1       #the number of sensitive .smali, start from 0 'cause it will be an index of a list
    _pathToBehaveDic = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{},11:{}}




    def __init__(self,_directory):
        self.directory = _directory


    # detect a singal .smali and return the result
    def detect(self,smalipath):

        self.Sensitive_Behavior =  [0]*51
        self.tagAPI = 0            #a tag for samli if it contains sensitive words
        self._root = [0,0,0]
        #print self.smalipath
        for line in file(self.smalipath):

            for i in range(1,51):    #16 is the number of the list of SensitiveWord

                if line.find(self.SensitiveWord[i]) > 0:


                    self.Sensitive_Behavior[i] = 1
                    self.tagAPI = 1      #change the tagAPI to 1 to mark that this smali contains sensitive words





    #detect all the .smali
    def DetectAll(self,directory):
        #print "hate"
        for item in os.listdir(directory):
            self.smalipath = directory + os.sep + item
            #print self.smalipath

            if os.path.isdir(self.smalipath):
                if "android" in self.smalipath:
                    print "android ignored"
                else:
                    self.DetectAll(self.smalipath)      #recursion when it is a dir

            elif item.endswith(".smali"):           #detect when it ends with ".smali"
                self.detect(self.smalipath)
                if self.tagAPI == 1:
                    #print "---",self.Sensitive_Behavior
                    pathtobehave = PathToBehave(self.smalipath, self.Sensitive_Behavior)   #build a PathToBehave class
                    self._pathToBehaveArray.append(pathtobehave)       #add to the list
                    self.countForSenSmali = self.countForSenSmali + 1
                    #print "temporary",pathtobehave.Behave
                    #print self.countForSenSmali,self._pathToBehaveArray[self.countForSenSmali].Behave




    def ArrayToDic(self):
        for i in range(1,51):
            #print "i:",i
            #tag = -1
            path = []
            for j in range(0,len(self._pathToBehaveArray),1):
                #print "j:",j

                if self._pathToBehaveArray[j].Behave[i] == 1:
                    #tag = tag + 1
                    #print "tag:",tag

                    path.append(self._pathToBehaveArray[j].Path)
                    #string = "%s%d"%("path",tag)
                    #self._pathToBehaveDic[i][string] = self._pathToBehaveArray[j].Path
            self._pathToBehaveDic[i] = path




    #collect all behaviors in single .smali
    def FinalSenBehavior(self):
        for i in range(1,51):

            for j in range(0,len(self._pathToBehaveArray)):
                #print i,j,self._pathToBehaveArray[j].Behave[i]

                if self._pathToBehaveArray[j].Behave[i] == 1:
                    self._FinalSenBehavior[i] = 1
                    #print "=",i,j,self._FinalSenBehavior[i]
                    break

        #print "API:", self._FinalSenBehavior






if __name__ == "__main__":
    #_directory = raw_input("input the directory where you put the file : ")

    opts, args = getopt.getopt(sys.argv[1:],"d:h","directory=help")
    for op, value in opts:
        if op in ("-d","--directory"):
            _directory = value
    '''
        if op in ("-h","--help"):
            print

            SensitiveBehaviorDectector.py [option][value]
            -h or --help
            -d or --directory file = "the directory of the file"
        '''
    detector = Detect_Sensitive_Behavior(_directory)
    detector.DetectAll(detector.directory)
    #for i in range(0,len(detector._pathToBehaveArray),1):
       # print detector._pathToBehaveArray[i].Behave,detector._pathToBehaveArray[i].Path
    detector.ArrayToDic()
    #print detector._pathToBehaveDic
    detector.FinalSenBehavior()




    #print detector._FinalSenBehavior

    #print "path",detector._pathToBehaveDic
    #print "permisstionTag",androidname.permissionTagDic

    f = open(_directory+"/Path.json","w")
    f.write(json.dumps(detector._pathToBehaveDic))
    f.close()





    f = open(_directory+"/static.json","w")
    f.write(json.dumps(detector._FinalSenBehavior))
    f.close()























