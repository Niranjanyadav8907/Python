# problem

# ask user to input a number containing more than one digit

#example 1256

# calculate 1+2+5+6 and print

# algorithm (method to solve problem in human language)
#ask input in string, i.e don't change string to int
#example "1256"
#pick string character one by one and change to int
#int(example[0]) + int(example[1]) .... go upto len(example)


number = input("enter a number") #ager number ke baad space dete ho to input ko bhi space dena hoga 
#for example use iput kraya "1256" iski lenth 4 , last index = 3 (o se count krte hai)
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total) 


