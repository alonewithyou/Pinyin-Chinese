import os
import sys

#print(sys.path[0])
#configList = os.listdir(sys.path[0] + "/config")

configList = ["3layer-512units-attention-0.4d"]

for config in configList:
    print("Dealing with " + config)
    os.system("python3 train.py ./config/" + config)
    os.system("python3 check.py")
    fileList = os.listdir(sys.path[0] + "/save")
    for file in fileList:
        if "release" in file:
            print("File detected, renaming to " + config + ".t7")
            os.system("mv ./save/" + file + " ./save/" + config + ".t7")