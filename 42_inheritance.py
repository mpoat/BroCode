class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Shape:
    def square(self):
        print("This shape is Square")

    def rectange(self):
        print("This shape is Rectangle")

class Rabbit(Animal, Shape):
    def run(self):
        print("this rabbit is running")

class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.square()
rabbit.run()
rabbit.eat()
fish.sleep()
hawk.fly()