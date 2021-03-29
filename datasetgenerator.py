import os

import json
import shutil, sys
from os.path import join




for subdir, dirs, files in os.walk(r'/poracle-experiments/.poracle/log/test1/1/ORG'):
    for filename in files:
        #subdir = '/poracle-experiments/benchmark/APR-Efficiency/Patches/NFL/Cardumem'
        #print(subdir)
        #i += 1
        filepath = subdir + os.sep + filename
        #print(filename)
        if filepath.endswith("IN.log"):
            path = filepath
            #with open(path, 'r') as file:
                #info = file.read()
            #print(info)
            x = (path + "/")
            tool = os.path.dirname(x).split('/')[8]
            file1 = open(path, "r+")
            #file2 = open("/poracle-experiments/.poracle/log/test1/1/ORG/id_000000010/OUT.log", "r+")
            #text = file1.read().rstrip("\n") + ';' + file2.read().rstrip("\n")
            #print(file1.read())
            #print (filename)
        else:
            path1 = filepath
            # with open(path, 'r') as file:
            # info = file.read()
            # print(info)
            x = (path1 + "/")
            tool = os.path.dirname(x).split('/')[8]
            file2 = open(path1, "r+")
            # text = file1.read().rstrip("\n") + ';' + file2.read().rstrip("\n")
            #print(file2.read())
            #print(filename)
            text = file1.read().rstrip("\n") + ';' + file2.read().rstrip("\n")+';True'
            print (text)







            #print (os.path.dirname(x).split('/')[7])

            #sample_name = os.path.dirname(x).split('/')[7]
            #y = sample_name.split('-')[0]
# file1 = open("/poracle-experiments/.poracle/log/test1/1/ORG/id_000000010/IN.log", "r+")
# file2 = open("/poracle-experiments/.poracle/log/test1/1/ORG/id_000000010/OUT.log", "r+")
# text = file1.read().rstrip("\n")+';'+file2.read().rstrip("\n")
# print (text)