import os
import sys #?

path = os.getcwd()

i = 0
Carpetas = {}
Principal = ""

for subdir, dirs, archivos in os.walk(path):
    dir_name = str(subdir).split("/")
    dir_name = dir_name[len(dir_name)-1]
    
    if len(Principal) < 1:
        Principal = dir_name 
    carpetas_archivos = []

    for dir_ in dirs:
        carpetas_archivos.append(dir_)
    for file_ in archivos:
        carpetas_archivos.append(file_)
    
    Carpetas[dir_name] = carpetas_archivos

resultado = []

def recursive_tree(folder, num):
    archivoss = ""
    num = num + "-"
    try:
        archivoss = Carpetas[folder]
        return go_through_list(archivoss, len(archivoss)-1, num)
    except:
        Exception()

def go_through_list(list_, index, num):
    if len(num) == 2:
        resultado.append(str(list_[index]))
    else:
        resultado.append(num + " " + str(list_[index]))
    if index == 0:
        recursive_tree(list_[index], num)
        return 
    else:
        recursive_tree(list_[index], num)
        return go_through_list(list_, index - 1, num)    

recursive_tree(Principal, " ")

for item in resultado:
    print(item) 