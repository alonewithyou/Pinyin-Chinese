source_ = "touchpal.680k.txt"
extra_ = "extra_tar.txt"

extra = open(source_, "r")
origin = extra.readlines()
extra.close()

extra = open(source_, "w")
new = open(extra_, "r")

extra.writelines(origin)
for st in new.readlines():
    extra.write(st)

extra.close()
new.close()
