#  question
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


#question
# "   Niranjan   "___________>"Niranjan"___________phir lower alfa me change krenge "niranjan"
# same work kisi chr keliye bhi kr ke dekhte hai 
#"   H  "______space remove______________"H"_________lower change_________h
#name.strip().lower().count(char.strip().lower()) # ye line number 15 me {past krna hai or check kr skte hain


