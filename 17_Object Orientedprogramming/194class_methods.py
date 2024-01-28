
# class methods
# difference between class methods and insatnce methods

class person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"you have created{cls.count_instances} instances of person class"



    def _full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18
    

p1 = person('Niranjan', 'Kumar', 21)
p2 = person('Arjun', 'jha', 20)

print(person.count_instances())



# class variable - hrr object keliye ek hi hota hain class variable
# class attribute- 
# insatace methode pahla argument jo hota hain wo object khud  hota hain
# class method me pahla argument class khud hota hain

# hmm aisa function kaise bnay jisme pahla argument class khud ho iske liye 
# use krte hai @decorater


