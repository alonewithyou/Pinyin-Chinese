import os
import sys

script, config = sys.argv

configFile = open(config, "r")


def read():
    ret = configFile.readline()
    ret = ret[:-1]
    return ret


data = read()
brnn = read()
layer = read()
rnnsize = read()
dropout = read()
report = read()
residual = read()
attention = read()
# -attention <string> (accepted: none, global; default: global)
# -global_attention <string> (accepted: general, dot, concat; default: general)
end = read()

os.system("cp *release.t7 save/")
os.system("mv nlp_epoch*.t7 backup/")
os.system("th train.lua -data %s -gpuid 1 -save_model nlp %s %s %s %s %s %s %s %s" %
          (data, brnn, layer, rnnsize, dropout, report, attention, residual, end))

configFile.close()
