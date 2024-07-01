import time
#for loop = a statement that will executre its block of code
#           a limited amount of times
#
#           while loop = unlimited
#           for loop = limited

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):     #(50 is inclusive, 100+1 means to include 100, step by 2)
#     print(i)

# for i in "Mike Poat":             # Each letter is iterated over
#     print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(.1)
print("Happy New Year!")


#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())