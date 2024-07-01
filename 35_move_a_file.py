import os

src = "C:\\Users\\mpoat\\Desktop\\test2.txt"
dst = "C:\\Users\\mpoat\\Desktop\\folder\\test_mvd.txt"

try:
    if os.path.exists(dst):
        print("There is already a file there")
    else:
        os.replace(src,dst)
        print(src+" was moved")
except FileNotFoundError:
    print(source+" was not found")

fh = open(os.path.