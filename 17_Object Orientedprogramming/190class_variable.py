
# class variable 
# class variable ki value hrr varibel ke sath share hota hain

# circle
# area
# circum

class circle :
    def __init__ (self, radius, pi):
        self.radius = radius
        self.pi = pi
    def calc_circumference(self):
        return 2*self.pi*self.radius
    
c = circle(4,3.14)
c1 = circle(5,3.14)
print(c.calc_circumference())

# but yeha pr 2  probelm hain (pi ka value hrr object keliye same hain or )
# dobara dobara likh rhe hai ye glt ho gya 
# probelem num 2 memory me hr object kelieye ye varibel alg alge hoga jis se 
# memory me bhi dikkt hoga 

# in sbhi pro.. ko dur krne keliye class variable ka use krte hain

class circle :
    pi = 3.14 # idr hi class varibele difine kr denge 
    def __init__ (self, radius):
        self.radius = radius

    def calc_circumference(self):
        return 2*circle.pi*self.radius
    
c = circle(4)
c1 = circle(5)
print(c.calc_circumference())



        


