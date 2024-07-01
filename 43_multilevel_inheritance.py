# multi-level inheritance = when a derived (child) class inherits another derived (child) class

#This class is like the Grandparent
class Organism:

    alive = True

#This class is like the parent
class Animal(Organism):

    def eat(self):
        print("This animal is eating")

#This class is the child
class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()