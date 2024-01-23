# lambda expression (anonymous function)

# lambda expression ek function jise hmm ek hi line me difine kr dete hain

def add(a,b):
    return a + b

add2 = lambda a, b : a+ b
print(add2(2,3))

# lambda  function ko vairibel me asine nhi krte hain 

#  lambda function ka use....built in , reduce, filter

# Example 2 function difine

multiply = lambda a,b : a*b
print(multiply(2,3))


# lambda function ka koi naam nhi hota example

print(add)
print(add2)
print(multiply)