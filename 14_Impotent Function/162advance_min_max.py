# advance min() and max  ()
# min()------ sb se chhota 
# max()-------sb se bdha 

numbers = [1,2,3,4,5,6,7]
print(min(numbers))

# name naam ki koi string hain or aapko pta krna hain sb se kis 
# string ka lent hain aap kaise pta krenge 

def func(item):
    return len(item)
names = ['Niranjan', 'Arjun', 'Chitaranjan']
print(min(names,key = func))

# isi chij ko hmm lamda use krke short me kr skte hain
names = ['Niranjan', 'Arjun', 'Chitaranjan']
print(max(names, key = lambda item :len(item)))



## exmple 2  score kiska jyda ye dekhna ho to..

### print(max(student2.key = lambda item:item.get('score))['name'])




