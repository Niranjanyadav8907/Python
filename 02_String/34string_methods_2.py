# replace() method
# find ()   method

string = "she is beautiful and she is good dancer"
print(string.replace(" ", "_"))
print(string.replace("is", "was")) # is ke jgh pr was keliye
print(string.replace(" is", "was", 2)) # kitne is ko change krna hai pairagraph me


#find method-- find method ka use krte hai  kisi word ki position pta chl ske string me chr ka bhi pta lga skte hai

print(string.find("is"))
print(string.find("is",1)) #position bta skte hai kaha se start kre 

is_post1= string.find("is") #is_post---> number
is_post2= string.find("is", is_post1 + 1 )
print(is_post2)
# particuler string ke positione ko janne keliye ye kr skte hain




 

