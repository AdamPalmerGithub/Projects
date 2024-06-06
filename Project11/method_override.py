'''A program using classes to work out if the user is an adult or a child.'''

class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):    #parent class with objects
        self.name = name 
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour


    def can_drive(self):
        print(f"{self.name} is old enough to drive.")      #function for driving

class Child(Adult):                                         #child class with function for cannot drive
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

name = input("What is your name?: ")                      #user inputs
age = int(input("What is your age?: "))
hair_colour = input("What is your hair colour?: ")
eye_colour = input("What is your eye colour?: ")

if age >= 18:
    g = Adult(name, age, hair_colour, eye_colour)        #checks if user is an adult or child or not and uses the apropriate class 
else:
    g = Child(name, age, hair_colour, eye_colour)

person_1 = g

g.can_drive()