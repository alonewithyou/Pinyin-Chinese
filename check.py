import os
import sys

fileList = os.listdir(sys.path[0])
modelList = []
for file in fileList:
    if "t7" in file and "nlp_epoch" in file:
        modelList.append(file)
print(modelList)

best_acc = 0.
best_model = ""

#modelList = ['nlp_checkpoint.t7']

for model in modelList:
    src = "dev_py.txt"
    output = "dev_out.txt "

    os.system("th translate.lua -log_file log -model %s -src %s -output %s -gpuid 1"
              % (model, src, output))

    f1 = open("dev_tar.txt")
    f2 = open("dev_out.txt")
    passed = 0
    total = 0
    try:
        s1 = f1.readline()
        s2 = f2.readline()
        while s1 != "":
            total += 1
            if s1 == s2:
                passed += 1
            s1 = f1.readline()
            s2 = f2.readline()
    finally:
        f1.close()
        f2.close()
    if passed / total > best_acc:
        best_acc = passed / total
        best_model = model
    print("Accuracy for %s: %.3f" % (model, passed / total))


os.system("th tools/release_model.lua -model %s -gpuid 1" % best_model)
print("Best acc: %.4f" % best_acc)
print("Best model: " + best_model)
