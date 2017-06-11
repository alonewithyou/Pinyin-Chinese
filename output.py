import os, sys

delSpace = 1
models = os.listdir(sys.path[0] + "/save/")
cnt = 0

for model in models:
    print(model)
    os.system("th translate.lua -log_file log -model ./save/%s -src test_py_syllable.txt -output res%d.txt -gpuid 1"
              % (model, cnt))
    cnt += 1

ans = open("test-out.txt", "w")
info = []
for i in range(cnt):
    f = open("res%d.txt" % i, "r")
    tmp = f.readlines()
    info.append(tmp)
    f.close()

for j in range(2001):
    answer = ""
    tot = 0
    for i in range(cnt):
        info[i][j] = info[i][j][:-1]
        if answer == "" or answer == info[i][j]:
            answer = info[i][j]
            tot += 1
        else:
            tot -= 1
            if tot == 0:
                answer = ""
    if delSpace:
        for i in range(len(answer)):
            if answer[i] != " ":
                ans.write(answer[i])
    ans.write("\n")

ans.close()