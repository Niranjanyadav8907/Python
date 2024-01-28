# Multiple inheritance - class is derived from multiple base clesses 


#Q. if we have created teacher and now one student joins
# master degree with becoming teacher then what??

#Ans :  just make subclass from  teacher so that student will 
#become teacher

class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()





#type of inheritance
# 1 single 
# 2 Multi-level
# 3 Hierarchical 
# 4 Multiple
# 5 Hybrid
# 6 cyclic
