# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow use to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#del capitals[3]
# capitals.clear()


print(capitals['Germany'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print("")
for key,value in capitals.items():
    print(key, value)


print("$$$$$$$$$$$4")
print(capitals['USA'])