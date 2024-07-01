# while loop = a statement that will executre its block of code,
#              as long as it's condition remains true

# x = 30
# while(x > 10):
#     x = x - 1
#     print(x)

#name = ""
###name = None
#while len(name) == 0:
###while not name:
    ###name = input("Enter your name: ")

###print ("Hello "+name)


def authenticate():
    # Set the correct password
    correct_password = "password123"

    # Ask the user for their password
    user_password = input("Enter your password: ")

    # Check if the entered password is correct
    while user_password != correct_password:
        print("Incorrect password. Try again.")
        user_password = input("Enter your password: ")

    # If the loop exits, the correct password has been entered
    print("You can enter.")

# Call the function to start authentication process
authenticate()
