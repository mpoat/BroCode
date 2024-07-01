# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Mike Poat"

#first_name = name[0:4:2]
first_name = name[:-1]           # [0:3]
last_name = name[5:]            # [5:end]
funky_name = name[::3]          # [0:end:3]
reversed_name = name[::-1]      # [0:end:-1]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
# print(website1[slice])
# print(website2[slice])

#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)