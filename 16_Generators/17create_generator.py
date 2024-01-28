
# create your first generator with generator function

# generator ko bnnane keliye kya use krte hain
# 1 generators function
# 2 generators comprehension

# 1 generators function
# for example aisa function difine kro  jo as argument input 10 lega  or 
# function print krega 1 tp 10 numbers

def num(n):
    for i in range(1,n+1):
        print(i)
num(10)

#  same code ka # generators function bnna hain

def num(n):
    for i in range(1,n+1):
        yield(i)       
print(num(10))


