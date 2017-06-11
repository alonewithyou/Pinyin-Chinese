import os, sys

srtList = os.listdir(sys.path[0])

cnt = 0

for srt in srtList:
    if ".srt" in srt:
        os.system("./cvgen.py '" + srt + "' tar.txt")
        os.system("python3 produce.py")
        os.system("python union.py")
        os.system("rm '" + srt + "'")
        print("Done with %s" % srt)
        cnt += 1

print("%d files found in total" % cnt)