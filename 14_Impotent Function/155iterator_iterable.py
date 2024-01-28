
# iterator vs iterables

numbers = [ 1,2,3,4] # iterables

squares  = list(map(lambda a:a**2, numbers)) # iterator
#print(squares)



#tuples,string, list sbhi hote hain iterables

#for i in numbers:
#print(i)

# iterables
number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
#print(iter(numbers)) ye bhi ek object hain 


 
# iterator dairect call hota hain 

#print(next(squares))
#print(next(squares))
#print(next(squares))


