def add(a,b):
    if (type(a) is int) and  (type(b) is int):
        return a+b
    raise TypeError('OOps, you are passing worng data type')

print(add('2', '3'))


