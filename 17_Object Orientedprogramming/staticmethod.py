#******* Code-yug**********

# types of methods 
# 1 instance method
# 2 class methods
# 3 static methods

# Methods which performs operations on external data 
# exteranal data mtlb aisa data jo class se n object se belong krta ho 

# it can also perform operations on class data

# no need to pass object or class reference
# created using decorator @staticmethod
# static method me class or object refrence nhi dena pdhta hain

## static method aisa method hota hai jo external  data pr kaam
# krta hain  n class ka ho n object ka ho 

class Bank:
    bank_name= 'BOI'
    rate_of_interest=12.25
    @staticmethod
    def simple_interest(prin,n):
        si = (prin*n*Bank.rate_of_interest)/100
        print(si)


print=float(input("Enter principle amount:"))
n= int(input("Enter number of years:"))
#Bank.simple_interest(prin,n)
    


