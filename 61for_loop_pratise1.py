# practice for loop 
# ask user a number like 1256
# caculate sum of digital -----> 1 + 2 + 5 + 6

# logic 
# num = "1256", is time lenth kya hai lenth 4 hain 
#int(num[0])------1
#int(num[0])------2
#int(num[0])------5
#int(num[0])------6
#indexing keliye  i-----> 0 to 3 tk jayga
 






total = 0
num = input("enter a number : ")
for i in range(0, len (num)):
    total += int(num[i])
print(total)