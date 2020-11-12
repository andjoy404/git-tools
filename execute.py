import os
from os import name, popen
from sys import argv
import sys

# uncomment pathRoot base on your operating system
# pathRoot = "C:\\Users\\Admin\\Documents\\repo-group-path\\" # windows path
# pathRoot = "/home/user/repo-group-path" # linux path
dirRoot = os.listdir(pathRoot)

par0 = (' ' .join(sys.argv[2:]))
parA = (' ' .join(sys.argv[1:2:]))
parB = (' ' .join(sys.argv[2:3:]))
parC = (' ' .join(sys.argv[3:4:]))
parD = (' ' .join(sys.argv[4:5:]))


def recDir():
    serviceList = (' ' .join(dirRoot))
    if parC == "current":
        sPath = pathRoot + "\\" + parA
        sList = os.listdir(sPath)
        for s in sList:
            os.chdir(sPath)
            parentDir = sPath + "\\" + s
            os.chdir(parentDir)
            nameDir = os.path.basename(parentDir)
            print(nameDir)
            os.system(parB + " " + parD + '|grep "*"')
    elif parA not in serviceList:
        print("please choose service group : " + serviceList)
    else:
        if parA in serviceList:
            sPath = pathRoot + "\\" + parA
            sList = os.listdir(sPath)
            for s in sList:
                os.chdir(sPath)
                parentDir = sPath + "\\" + s
                os.chdir(parentDir)
                nameDir = os.path.basename(parentDir)
                print(nameDir)
                os.system(par0)
        else:
            print("please choose service group : " + serviceList)


recDir()
