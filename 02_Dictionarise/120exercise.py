 # exercise
# define a function that takes a number (n)
# return a dictionary containing cube of numbers from (n)
# return a dictionary containining cube of number of number from 1 to n 

# example 
# cube_finder(3)
# {1:1, 2:8, 3:27}

# cube finder

def cube_finder(n):
    cubes = {}
    for i in range(1, n+1): # range kaha tk jati hain -1 tk isliye (n+1)
        cubes[i] = i**3
    return cubes

print(cube_finder(10))