# common methods to delete data from list

fruits = [ ' orange', 'apple', 'pear,' 'banana', 'kiwi']
# pop method data ko delete use method  ye last eliment ko delete kr deta hain
fruits.pop()
print(fruits)

## arugumet pass kra kr aap jise chahe use delete kra skte hain
fruits = [ ' orange', 'apple', 'pear,' 'banana', 'kiwi']
fruits.pop(2)
print(fruits)

#delete opreter
fruits = [ ' orange', 'apple', 'pear,' 'banana', 'kiwi']
del fruits[1]
print(fruits)

#remove methods
fruits = [ ' orange', 'apple', 'pear,' 'banana', 'kiwi']
fruits.remove('apple') # or 2 apple ho to ye bs pahle wale apple ko remove krega 
print(fruits)

#data ko add krne keliye
#append , extent , insert

#data ko delet krne keliye 
#pop, remove, del







