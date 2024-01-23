# *args wuth noraml parameter

def multiply_nums(*args):  # jb functin difine krte hai usko pairameter bolte hain
    multiply = 1           # function call ko aargumet 
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(1,2,3,4,5))

# *args me aap kucch n pass kray tbhi error nhi aayga 
# but num me aisa nhi hain error aa jayga 