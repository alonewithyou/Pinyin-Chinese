import time, os

time.sleep(5)
py = open("pinyin.txt", "r")
for line in py.readlines():
    line = line[:-1]
    for c in line:
        if 'a' <= c <= 'z':
            time.sleep(0.02)
            os.system("xdotool key %s" % c)
    os.system("xdotool key KP_Space")
    time.sleep(0.05)
    os.system("xdotool key KP_Enter")

py.close()
