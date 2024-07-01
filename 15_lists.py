# list = user to store mulitple items in a single variable

food = ["pizza", "hamburgers", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

#food.append("ice cream")
#food.remove("hotdog")
#food.pop() # removes the last value
#food.insert(0, "cake") # inserts cake at the begining
#food.sort() # sorts in alphabetical
#food.clear() clears the list

for x in food:
    print(x)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)