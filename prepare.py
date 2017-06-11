# -*- coding:GBK -*-
import random


def chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False

tar_in = open("touchpal.680k.txt", "r")
py_in = open("touchpal.680k.py.txt", "r")
train_out_tar = open("train_tar.txt", "w")
train_out_py = open("train_py.txt", "w")
dev_out_tar = open("dev_tar.txt", "w")
dev_out_py = open("dev_py.txt", "w")
tar = "1"
try:
    while tar != "":
        tar = tar_in.readline()
        py = py_in.readline()
        first = True
        cache = ""
        for i in range(len(tar)):
            if chinese(tar[i]):
                if first:
                    first = False
                else:
                    cache = cache + " "
                cache = cache + tar[i]
        cache = cache + "\n"
        if random.random() < 0.005:
            dev_out_tar.write(cache)
            dev_out_py.write(py)
        else:
            train_out_tar.write(cache)
            train_out_py.write(py)
finally:
    train_out_py.close()
    train_out_tar.close()
    dev_out_py.close()
    dev_out_tar.close()
    tar_in.close()
    py_in.close()