
# LIST COMPREHENSION SUMMARY

# for example ek list creat krna hain jisme 1 se 11 number ke square

square = []
for i in range(1,11):
    square.append(i**2)
print(square)

# COMPREHENSION use krke............................

square = [ i**2 for i in range(1,11)]
print(square)


# Example 2 if ko kaise use krte hain comprehnsion me 

even_num = [i for i in range(1,11) if i % 2 ==  0]
print(even_num)


# example 3  if and else dono conn ek sath use krte hain 
# if else 

#[1,2,3,4.......10]
#[-1,4, -3,,  8]

mixed = [ i* 2 if (i % 2==0) else -i for i in range(1,11)]
print(mixed)


#example 4 Nested list (list ke andfer list )

n1 = [1,2,3]  ,[1,2,3] ,[1,2,3]
new_list = [[ i for i in range (1,4)] for j in range(3)]
print(new_list)


