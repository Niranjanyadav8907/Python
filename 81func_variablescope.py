# variable scope

x= 5 # global variable 
def func():
    global x  # func ander global variable ko change kr skte hai but btana pdhta hain 
    x = 7     # jo variable func ke ander difine hote hain unhe hmm ( local variable)
    return x

print(func())
print(x)

 
