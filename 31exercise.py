# take two comma saparted input from user 
# 1 user's name , example - "Niranjan"
# 2 a single character, 

#output - 2 print line 
# 1 user's name lenngt 
# 2 count the charracter that inputed (bonus : case insensitive count)

name ,char = input ("enter comma separded name and character : ").split(",")
print(f"lenth of your name is {len(name)}")
#print(f"charcter count : {name.count()}") #case sensitive

# Niranjan- niranjan
print(f"charcter count : {name.lower().count(char.lower())}") # case sensitive ko count krne keliye 
# N - n
