# ask a user for name
# Example Harshit Vashisth
# print count of each words
# output :

# H: 1
# a: 2
# r: 1
# s: 3
# h: 3
# i: 2
# v: 1

#name = ("plese enter your name ")
#harshi vashisth
#name.count("h"),name.count(name[0]) = 2 kitne baar hain
#name.count("a"),name.count(name[1]) = 1
#name.count("r"),name.count(name[2]) = 1
#name.count("s"),name.count(name[3]) = 1
#name.count("h"),name.count(name[4]) = 1 

#output
# h : 2
# a : 1  aise out put aayga 

# ager kisi naam me same chr 2 baar ho to wo ek baar hi print count ho aisa kaise hoga dekhte hain

name = input("plese enter your name ")
i = 0
while  i < len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1


# jo chr ek baar count ho gya use dobara n count kre iske liye code 

name = input("plese enter your name ")
temp_var = ""
i = 0
while  i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1





