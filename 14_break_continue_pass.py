# Loop Control Satements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

#BREAK
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break                     # Once name is met, it ends the loop

#CONTINUE
# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue                     # Skips to the next iteration of the loop
#     print(i, end="")

#PASS
for i in range(1,21):
    if i == 13:
        pass                         # Does nothing, acts as a placeholder. Skips #13
    else:
        print(i)