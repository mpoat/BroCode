name = "Mike Poat"

print(len(name))               # prints length of name
print(name.find("k"))          # prints char location of letter in (name)
print(name.capitalize())       # capitalizes the first letter
print(name.upper())            # print name is all upper case
print(name.lower())            # prints name in all lower case
print(name.isdigit())          # to see if its a digit
print(name.isalnum())          # To see if string only contains letters
print(name.count("a"))         # prints how many "a" are in the name
print(name.replace("o","a"))   # repalce all "o" with "a"
print(name*3)                  # will print name 3 times




words = ['apple', 'banan']
print([w[0].upper() for w in words])

