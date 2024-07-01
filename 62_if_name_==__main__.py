# # Python interpreter set "special variables", one of which is __name__
# # Python will assign the __name__ variable a value of '__main__ if its
# # the initial module being run
#
# *******************************
# if __name__ == '__main__'
# *******************************

# import module_two
# print(__name__)
# print(module_two.__name__)

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")