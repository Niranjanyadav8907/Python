# function returning two values
def func(int1, int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply # 2 value ek sath 

print(func(2,3))

# 2 alg varible me store kr skte hain
add, multiply = func(2,3)
print(add)
print(multiply)

# jb bhi function me ek sath 2  value return kroge 2 alg alg  value nhi dega  same hi dega 


