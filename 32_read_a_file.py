import os
import stat

path = "C:\\Users\\mpoat\\Desktop\\test.txt"

try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
#print(file.closed)

size = os.stat(path)[stat.ST_SIZE]
print(size)