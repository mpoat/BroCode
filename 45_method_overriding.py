class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):  #<--- This method overrides the eat method in the Animal class
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()