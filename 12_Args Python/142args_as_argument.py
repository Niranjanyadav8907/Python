

def multiply_nums(*args):  
    multiply = 1           
    for i in args:
        multiply *= i
    return multiply

num = [2,3,4]  # aap list tuple kucch bhi use kr skte hain (2,3,4)
print(multiply_nums(*num)) # * num likhne se unpack ho jata hain 

