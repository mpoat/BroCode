import os

path = "C:\\Users\\mpoat\\Desktop\\test2.txt"

#text = "Yooooooooo\nThis is some text\nHave a good day!\n"
#text = "Overwritten"
text = "Append some text using 'a'"


with open(path,'a') as file:
    file.write(text)
