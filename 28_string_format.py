# str.format() =    optional method that gives users
#                   more control when displaying output

#{} are placeholder for a value or variable

# animal = "cow"
# item = "moon"

#print("The "+animal+" jumper over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) # positional argument
#print("The {animal} jumped over the {animal}".format(animal="cow",item="moon")) # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

#-----#

# name = "Mike"
# print ("Hello, my name is {}".format(name))
# print ("Hello, my name is {:10}. Nice to meet you".format(name))
# print ("Hello, my name is {:<10}. Nice to meet you".format(name))
# print ("Hello, my name is {:>10}. Nice to meet you".format(name))
# print ("Hello, my name is {:^10}. Nice to meet you".format(name))

#-----#

number = 3.142

print("The number pi is {:.2f}".format(number))
# print("The number is {:,}".format(number)) # Put comment for 1000s
# print("The number is {:b}".format(number)) # show in binary
# print("The number is {:o}".format(number)) # show in octal
# print("The number is {:X}".format(number)) # show in hexidecimal
# print("The number is {:e}".format(number)) # show in hexidecimal
