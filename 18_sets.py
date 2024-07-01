# set = collection which is unordered, unindexed. No duplicate values allowed
# set will be unordered when you print (different each time) and if there are duplicates it will only print 1


utensils = {"fork", "spoon","knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)

#create new set
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes)) # prints the difference between the two sets

print(utensils.intersection(dishes)) # returns the item they have in common

# for x in dinner_table:
#     print(x)