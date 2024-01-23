 # make flexible functions

# *operator
# *args

# * *operator ,*args.. ki jarurat kyu pdha 
def total(a,b):
    return a+b
print(total(3,4 ))
#  2 se adhik argument dene pr error aa
#  jata hai (normliy 2 positional arguments accsept krta hain)
#  isi probelem ko duir krne keliye in use kiya jata hain
# *args use krne pr tuple me connvert bhi hota hain

def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4))
