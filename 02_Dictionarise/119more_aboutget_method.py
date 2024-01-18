 # more abote get, two same keys in dictionaries

user = {'name':'Niranjan', 'age' :22} # ek dic me 2 key same ho to kya hoga 
print(user.get('name'))
print(user.get('names', 'not found!')) # none ko over ride kaise kr skte hain


 # ek se jyda ki ho to kya hoga 

user = {'name':'Niranjan', 'age' :22, 'age': 34} # dic me 2 key hoti hai to baad wala key bs count hoata hain
print(user)
