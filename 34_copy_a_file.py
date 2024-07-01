# Below are the functions of the 'shutil' module
# copyfile()    = copies content of a file
# copy()        = copyfile() + permission mode + destination can be a directory
# copy2()       = copy() + copies metadata (file's creation and modification times)

import shutil

src = "C:\\Users\\mpoat\\Desktop\\test2.txt"
dst = "C:\\Users\\mpoat\\Desktop\\test_dst.txt"

shutil.copy2(src,dst) #src, dst