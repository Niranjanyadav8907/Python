# function
# list, reverse_str = true
# list

def func(l, **kwarge):
    if kwarge.get('reverse_str') == True:
         return [name[::-1].title() for name in l]
    else:
         return[name.title() for name in l]
    
names = ['Niranjan', 'Mohit']
print(func(names, reverse_str = True))

