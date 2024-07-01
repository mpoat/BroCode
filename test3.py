# #Dictionary Aggregation
# inv = {
#     'Sword': 1,
#     'Potion': 3
# }
# loot = {
#     'Sword': 1,
#     'Potion': 2,
#     'Shield': 1
# }
# new_inv = {
#     k: inv.get(k, 0) + loot.get(k, 0)
#     for k in set(inv | loot)
# }
# print(new_inv)

# #Fibonacci
#
# def fibonacciDynamic(n):
#     fib = [0] * (n + 1)
#     print(fib)
#     fib[1] = 1
#     print(fib)
#     sm = fib[0] + fib[1]
#     print(sm)
#
#     for i in range(2, n + 1):
#         fib[i] = fib[i - 1] + fib[i - 2]
#         sm = sm + fib[i]
#     return sm
#
#
# n = 4
# print(fibonacciDynamic(n))

#Find the Dominator
# A = [3, 2, 3, 4, 4, 3, 3, 3, -1]
# length = len(A)
# srtA = sorted(A)
#
# print(srtA)
#
# b = 1
# #for i in range(len(srtA)):
# for i in (srtA):
#      if i == srtA[-1]:
#           print("blah")
#           break
#           #print("last elm "+str(srtA.index(i)))
#      elif srtA[i] == srtA[i]:
#           print(i)
#           #print("Ans: "+str(srtA[i])+" matches "+str(srtA[i+1]))
#
#
#      #print(srtA[i])

# def solution(A):
#      if not A:
#           return -1
#
#      candidate = None
#      c = 0
#
#      # Find a candidate for the dominator
#      for num in A:
#           if c == 0:
#                candidate = num
#                c += 1
#           else:
#                if candidate == num:
#                     c += 1
#                else:
#                     c -= 1
#      print(candidate)
#      # Verify if the candidate is the dominator
#      c = A.count(candidate)
#      print(c)
#      if c > len(A) // 2:
#           return A.index(candidate)
#      else:
#           return -1
#
#
# # Example usage:
# A = [3, 4, 3, 2, 3, -1, 3, 3]
# print(solution(A))  # Output could be any index where dominator occurs, e.g., 0, 2, 4, 6, or 7

# def f():
#      for i in range(3):
#           yield i
# result = list(f())
# print(result)

#---------

# import re
# testString = 'Yellow Blue Gold Green'
#
# print(re.search(r'Blue',testString).group(0))

#------------

# n = 12
# names = [[]] * n
# print(names)
# blah = [2] * n
# print(blah)
#
# employee = "Adam"
# m = 6
# names[m].append(employee)
# print(names)
#
# def get(self):
#     print("hi")
# get("hi")
#
#
# def test(x):
#     if x % 3 == 0 : return test(x/3)
#     if x % 2 == 1 : return x
#     return test(2*x+1)
# print(test(100))

i = 150
j = 300
if ((True == False) and (False in (False,))) == True:
    print(i)
elif (True == False) in (False,) == False:
    print(j)
else:
    print("No")

numbers = 3

age = 18

if age > 35:
    print("valid")
elif age==18:
    print("inv")
else:
    pass


exampple = ["bob","cinda","lou"]
print("Example: %s" % exampple)

class Example:
    def test(self):
        print("example testing")

class Test(Example):
    def testing(self):
        print("Online Testing")

i = Test()
i.testing()
i.test()