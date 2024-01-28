
## Encapsulation - apne data ko  or us data ke  sath jo
# funsality perform kr skte hain wo vali method ek hi jgh likhna 
# encapsulation kahlata hain

class phone:
    def _init_(self, brand, model_name,price):
     self.brand = brand
     self.model_name = model_name
     self.price = price

    def full_a_call(self,phone_number):
     print(f"calling {phone_number}...")


     def full_name(self):
      return f"{self.brand} {self.model_name}"


# abstraction -abstraction ka matlab hota hai complexity ko hide krna 

l = [3,4,1,2]
l.sort() # tim sort
print(l)


# _name # convention of private name
#__name___ # dunder/magic methods


# Name Mangling # __name iske help se python me name change kiya
#jata hain


