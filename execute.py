import os
from sys import argv
import git
import sys
from win10toast import ToastNotifier

# pathRoot = "C:\\Users\\GDA-Admin\\Documents\\GTech\\Python\\development\\git\\repo\\"
pathRoot = "C:\\Users\\GDA-Admin\\Documents\\GTech\\repo_gtech\\None\\Mapemall-2.0\\"
dirRoot = os.listdir(pathRoot)

paramService = (' ' .join(sys.argv[1:2:]))
paramCommand = (' ' .join(sys.argv[2:]))


def service_name():
    if paramService == "jarvis":
        jPath = pathRoot + "\\" + paramService
        jList = os.listdir(jPath)
        for j in jList:
            os.chdir(jPath)
            osDir = os.listdir(j)
            parentDir = jPath + "\\" + j
            os.chdir(parentDir)
            nameDir = os.path.basename(parentDir)
            print(nameDir)
            os.system(paramCommand)
    elif paramService == "helix":
        hPath = pathRoot + "\\" + paramService
        hList = os.listdir(hPath)
        for h in hList:
            os.chdir(hPath)
            osDir = os.listdir(h)
            parentDir = hPath + "\\" + h
            os.chdir(parentDir)
            nameDir = os.path.basename(parentDir)
            print(nameDir)
            os.system(paramCommand)
    elif paramService == "friday":
        fPath = pathRoot + "\\" + paramService
        fList = os.listdir(fPath)
        for f in fList:
            os.chdir(fPath)
            osDir = os.listdir(f)
            parentDir = fPath + "\\" + f
            os.chdir(parentDir)
            nameDir = os.path.basename(parentDir)
            print(nameDir)
            os.system(paramCommand)
    else:
        print("please choose service group : " + ' ' .join(dirRoot))


service_name()
