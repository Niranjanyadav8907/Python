#******** Gate smashers************

#   It is a special method within a class that gets automatically
#  called when an object is created.
# • It is used to initialize the attributes of the object.
# • It is written with _init_


class faculty:
    def putdata(self):  # methode1
        self.id = int(input("enter faculty id "))
        self.name = input("enter name")
        self.salary=float(input("enter faculty salary"))
    
    def display(self):       #method2
        print("faculty id:" ,self.id)
        print("faculty name:", self.name)
        print("faculty salary", self.salary)

a = faculty()
a.putdata()
a.display()

## a.putdata() bina likhe automatically initialize kaise kra skte hai
# ye constructors ke help se krte hain

class faculty:
    def __init__(self):# methode1
        self.id = int(input("enter faculty id "))
        self.name = input("enter name")
        self.salary=float(input("enter faculty salary"))
    
    def display(self):       #method2
        print("faculty id:" ,self.id)
        print("faculty name:", self.name)
        print("faculty salary", self.salary)

a = faculty()
#a.putdata() # constructors me direct call kr skte hain
a.display()

## paira miter kaise pass krte hain 

class faculty:
    def putdata(self,a,b,c):  # methode1
        self.id = a
        self.name = b
        self.salary= c
    
    def display(self):       #method2
        print("faculty id:" ,self.id)
        print("faculty name:", self.name)
        print("faculty salary", self.salary)

a = faculty(1,"Niranjan", 10000)
a.display()



