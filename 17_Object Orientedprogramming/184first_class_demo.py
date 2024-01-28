
# Objectives
# what is class
# how to create an class 
# what is init method --- is constructor
# what are attributes , instance varibales
# how to create our object


# what is class class is blue print, class me pahla letter capital Rakhna chahie
# class me koi bhi function define hoga usko method bolte hain


    # instance variables
    # print('init method // constructor get called')
class person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = person('Niranjan', 'Kumar', 24)  # class ki object
print(p1.first_name) 






