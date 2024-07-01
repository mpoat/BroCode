# thread = a flow of execution. Like a separate order of instructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only one thread to hold the control of the Python interpreter

# cpu bound = program/take spends most of its time waiting for internal event (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of times waiting for external events (user input, web scraping)
#            user multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("you ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
