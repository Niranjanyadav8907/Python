# list comprehension
# withe the help of list comprehension we can created of list in one line 

# create a list of sequares from 1 to 10 


# fopr example 1 to 10  ka sqaures print krana hain list in one line 
sqaures = []
for i in range (1,11):
    sqaures.append(i**2)
print(sqaures)

#list comprehension use krke list kaise creat krte hain
 
sqaures2 = [i**2 for i in range(1,11)]
print(sqaures2)


# example 2 aapko el list creaate krna hain negative number ka 

nagative = []
for i in range(1,11):
    nagative.append(-i)
print(nagative)

#comprehension use krke same negative number pro... ko krte hain

new_negative = [-i for i in range(1,11)]
print(new_negative)


# example 3

name = ['Nirnjan', 'arjun' , 'Rohit']
# new lisrt = ['N', 'a', 'R'] aise print ho mtlb net list me bs name ka phla char print ho 
new_list = []
for name in name:
    new_list.append(name[0])
print(new_list)

#comprehension use krke same code ko 

name = ['Nirnjan', 'arjun' , 'Rohit']
new_list2 = [name[0] for name in name]
print(new_list2)
