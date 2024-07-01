import os
import shutil

src = "C:\\Users\\mpoat\\Desktop\\folder\\test_mvd.txt"
srcdir = "C:\\Users\\mpoat\\Desktop\\folder"

try:
    #os.remove(src)
    #os.rmdir(srcdir)
    shutil.rmtree(srcdir) # considered dangerous! rm -rf
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("You cannot delete a dir with files in it")
else:
    print(srcdir+" was deleted")
