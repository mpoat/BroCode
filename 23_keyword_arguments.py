# keywork arguments     = arguments preceded by an identifies when we pass them to a function
#                         The order of the arguments doesn't matter, unlike positional arguments
#                         Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Mike",middle="Dude",first="Poat")