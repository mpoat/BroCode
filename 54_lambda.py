# lambda function    = function written in 1 line using lambda keyword
#                     accepts any number of arguments, but only has one expression.
#                     (think of it as a shortcut)
#                     (useful if needed for a short period of time, throw-away)

#lambda parameters:expression

# def double(x):
#     return x * 2
#
# print(double(5))

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False


print(multiply(2,4))
print(age_check(18))

from functools import reduce
x = reduce(lambda x,y : [y] + x, list(range(5)), [])
print(x)