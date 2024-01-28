
# generators
# generators are iterators

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


# what is a generators

# memory ------[................] koi tuple hain usme me koi data ek hi baar
# incude rhta hain but # generators me aisa nhi hota # generators ek baar me 
# ek data # generators hota hain for exaple aap ek loop chlay phir

# l =  [1,2,3,4]
# memory---(1)
# ------------(2) aise kaam krta hain # generators