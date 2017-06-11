source = "extra_"
extra = ""

extra_tar = open(source + "tar.txt", "r")
extra_py = open(source + "py.txt", "r")
origin_tars = extra_tar.readlines()
origin_py = extra_py.readlines()
extra_tar.close()
extra_py.close()
extra_tar = open("extra_tar.txt", "w")
extra_py = open("extra_py.txt", "w")
new_tar = open(extra + "tar.txt", "r")
new_py = open(extra + "py.txt", "r")
extra_tar.writelines(origin_tars)
extra_py.writelines(origin_py)
for tar in new_tar.readlines():
    extra_tar.write(tar)
for py in new_py.readlines():
    extra_py.write(py)
extra_tar.close()
extra_py.close()
new_tar.close()
new_py.close()
