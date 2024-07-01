# nested function calls = function calls inside other functions calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for next outer function

num = input("Enter a whole positive number: ")      # replacing these 4 lines of code with 1 below
num = hex(num)
# num = float(num)
# num = abs(num)
# num = round(num)
print(num)

#print (round(abs(float(input("Enter a whole positive number: ")))))

print("The number is {:b}".format(number)) # show in binary