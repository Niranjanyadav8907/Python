# tuples
# tuples are immutable
# tuples are ordered collections of data
# tuples can store any data type
# you cannot change (add or delete) values from tuple once it created
# but can add, delete data from list which is present inside tuples

mixed = (1,2,3,4,5, 'six')
# no append, no pop, no insert, no remove
# only count and index

# functions
#min(), max(), len(), sum()

mixed2 = (1,2,3,4,5, [6,7,8])
mixed2[5].pop()
print(mixed2)