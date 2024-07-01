# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = "Mike" # gloval scope (available inside & outside functions)

def display_name():
    name = "Poat"   # local scope (available only inside this function. Comment this line and run code to use global var
    print(name)

display_name()
print(name)

# Python used LEGB when it comes to variables in this order top to bottom
# L = Local
# E = Enclosing
# G = Global
# B = Built-in