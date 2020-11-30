import os
import sys
from sys import argv

'''
# define root path of your repository, choose one base on your operating system
pathRoot = "C:\\Users\\Admin\\Documents\\repo-group-path\\" # windows path
pathRoot = "/home/user/repo-group-path" # linux path
'''
dirRoot = os.listdir(pathRoot)

par0 = (' ' .join(sys.argv[2:]))
parA = (' ' .join(sys.argv[1:2:]))
parB = (' ' .join(sys.argv[2:3:]))
parC = (' ' .join(sys.argv[3:4:]))
parD = (' ' .join(sys.argv[4:5:]))

'''
# list excluded repo that not to be an executed
# if you don't want to use this, just commet whole 'exc' variable
exc = [
    "repo-a",
    "repo-b",
    "repo-c"
]
'''


def recDir():
    serviceList = (' ' .join(dirRoot))
    sPath = pathRoot + "\\" + parA
    sList = os.listdir(sPath)
    if 'exc' in globals():
        mcList = [' '.join(w for w in s.split()if w not in exc)
                  for s in sList]
        cList = [x for x in mcList if x]
    else:
        cList = os.listdir(sPath)
    if parC == "current":
        # sPath = pathRoot + "\\" + parA
        # sList = os.listdir(sPath)
        for s in cList:
            os.chdir(sPath)
            parentDir = sPath + "\\" + s
            os.chdir(parentDir)
            nameDir = os.path.basename(parentDir)
            print(nameDir)
            os.system(parB + " " + parD + '|grep "*"')
            print('/n')
    elif parA not in serviceList:
        print("please choose service group : " + serviceList)
    else:
        if parA in serviceList:
            # sPath = pathRoot + "\\" + parA
            # sList = os.listdir(sPath)
            for s in cList:
                os.chdir(sPath)
                parentDir = sPath + "\\" + s
                os.chdir(parentDir)
                nameDir = os.path.basename(parentDir)
                print(nameDir)
                os.system(par0)
                print('\n')
        else:
            print("please choose service group : " + serviceList)


recDir()
