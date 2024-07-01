import time

# print(time.ctime(0)) # The begining time converted in sections
#
# print(time.time()) # Return current time in seconds
#
# print(time.ctime(time.time())) # PRint the current time in time format
#
# print("")
#
# #********
#
# time_object = time.localtime() # Time in a structured format
# #time_object = time.gmtime() #UTC time
# print(time_object)
# #convert to a readable string
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)        #docs.python.org/3/library/time.html
# print(local_time)

# #********

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ********
#ASC time will convert a tuple representation or time object to a readable string
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

#convert to an Epoch date
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)