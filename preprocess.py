import os

train_src = "train_py.txt"
train_tar = "train_tar.txt"
dev_src = "dev_py.txt"
dev_tar = "dev_tar.txt"
data_pos = "nlp"

os.system("th preprocess.lua -train_src %s -train_tgt %s -valid_src %s -valid_tgt %s -save_data %s"
          % (train_src, train_tar, dev_src, dev_tar, data_pos))

