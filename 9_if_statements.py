# if statement = a block of code that will execute only if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are very old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You haven't been bornt yet")
else:
    print("You are a child")

