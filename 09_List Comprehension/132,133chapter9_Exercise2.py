 # num to stringe 
# define a function

# example 
# input.....>[True, False, [1,2,3], 1, 1.0, 3]
# output ....> ['1', '1.0', '3']

# ek fun difine krna hain as list usme kuchh bhi input ho skte stringe floate number
# any type data input

def num_to_string(l):
    return[str(i) for i in l if (type(i)== int or type(i) == float)]

print(num_to_string([True, False, [1,2,3], 1, 1.0, 3]))


    