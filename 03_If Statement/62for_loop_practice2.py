# practice for loop 
# ask user name and count each character
# Example "Harshit Vashisth"
# print count of each words
# output :

# H: 1
# a: 2
# r: 1
# s: 3
# h: 3
# i: 2
#  : 1
# v: 1

name = input("enter your name :")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} :{name.count(name[i])}")
        temp += name[i]

              
              
