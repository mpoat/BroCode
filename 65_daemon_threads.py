# daemon thread = a thread that runs in the backgroud, not import for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                   ex. background tasks, garbage collections, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print()
        print("logged in for: ",count, "seconds")
# With daemon=True, when the non-daemon threads are complete, it will kill the timer thread
x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon()) #to check if a program is a damon

answer = input("Do you wish to exit")