
#**** code-yug*****
# The word "polymorphism" means "many forms", and in programming it 
#refers to methods/functions/operators with the same name that can 
#be executed on many objects or classes.

## polymorphism in python is an ability of python object to take
# many forms.

## if a variable , object , method performs different behaviour according
# to situation is called as polymorphism

# example
# + :- python object

#print(10+20)   # 30
# print("hello "+" welcome")  #hellowelcome

# len("hello")  # 5 #count number rof characters
#len(['h', 'e', 'llo']) #3  # count number of items
# len(dictionary)  #number of keys


#example
#For example, say we have three classes: Car, Boat, and Plane, 
#and they all have a method called move():


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()







