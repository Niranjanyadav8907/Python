
#decorators - enhance the functionality of other functions

# decorators ek function hi ye finction ke functionality ko acuare krta hain
#@ use for decorator_function

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function ')
        any_function()
    return wrapper_function


# this is awesome function 
@decorator_function # shortcut method
def func1():
    print('this is function 1 ')


# this is awesome function --- ek aisa extra line print ho 
def func2():
    print('this is function 2 ') 


var = decorator_function(func1)
var = decorator_function(func2)
print(var)

