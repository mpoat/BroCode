# sort() method     = used with lists
# sort() function   = used with literables

#List of tuples
# students = (("Charlie","D", 36),
#             ("Amy", "F", 60),
#             ("Eric", "C", 78),
#             ("Bob", "A", 33),
#             ("Dave","B", 20))


#Tuple of Tuples
students = (("Charlie","D", 36),
            ("Amy", "F", 60),
            ("Eric", "C", 78),
            ("Bob", "A", 33),
            ("Dave","B", 20))

#students.sort() # easy sorts by 1st column
#grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students.sort(key=age)

sorted_students = sorted(students,key=age) # used for tuple of tuples

#students.sort(key=grade,reverse=True)

for i in sorted_students:
    print(i)