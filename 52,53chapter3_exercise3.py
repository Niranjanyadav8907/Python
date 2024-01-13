# exercise one of three
# sum of n natural numbers
# ask a  user for natural number(n)
# print total from 1 to n


#solution sb se pahle hmme input krana tha 

n = input("enter a number : ")
n = int(n)         # int me change kr lete hin kyu ki hmme number se deal krna hain
total = 0          # varibel dicliar kiya jisme starting value hain 0
i = 1
while i <= n:      # use  dvra input number me condition check tb tk hota jayga jb diye input se chhota n ho
    total += i
    i+= 1          # i ka value updet hota rhe isliye ye use krte hain
    print(total)
