
# decorator is function that takes another function as argument and returns a function 

def decorator(func):
    def wrapper():
        print('Transaction initiated')
        func()
        print('Transaction initiated')
    return wrapper

def hello():
    print('..Executing all steps of transaction...')

    hello1 = decorator(hello)
    hello()


# gate smashers
