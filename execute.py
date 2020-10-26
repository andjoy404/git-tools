import os
from sys import argv
import git
import sys
from win10toast import ToastNotifier

# path_root = "C:\\Users\\GDA-Admin\\Documents\\GTech\\Python\\development\\git\\repo\\"
path_root = "C:\\Users\\GDA-Admin\\Documents\\GTech\\repo_gtech\\None\\Mapemall-2.0\\"
dir_root = os.listdir(path_root)

param_service = (' ' .join(sys.argv[1:2:]))
param_command = (' ' .join(sys.argv[2:]))


def service_name():
    if param_service == "jarvis":
        j_path = path_root + "\\" + param_service
        j_list = os.listdir(j_path)
        for j in j_list:
            os.chdir(j_path)
            os_dir = os.listdir(j)
            parent_dir = j_path + "\\" + j
            os.chdir(parent_dir)
            name_dir = os.path.basename(parent_dir)
            print(name_dir)
            os.system(param_command)
    elif param_service == "helix":
        h_path = path_root + "\\" + param_service
        h_list = os.listdir(h_path)
        for h in h_list:
            os.chdir(h_path)
            os_dir = os.listdir(h)
            parent_dir = h_path + "\\" + h
            os.chdir(parent_dir)
            name_dir = os.path.basename(parent_dir)
            print(name_dir)
            os.system(param_command)
    elif param_service == "friday":
        f_path = path_root + "\\" + param_service
        f_list = os.listdir(f_path)
        for f in f_list:
            os.chdir(f_path)
            os_dir = os.listdir(f)
            parent_dir = f_path + "\\" + f
            os.chdir(parent_dir)
            name_dir = os.path.basename(parent_dir)
            print(name_dir)
            os.system(param_command)
    else:
        print("please choose service group : " + ' ' .join(dir_root))


service_name()
