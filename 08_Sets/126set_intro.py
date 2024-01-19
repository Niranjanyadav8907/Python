# set data type
# unordered collection of unique items

s = {1, 2,3 ,2} # uniq ka mtlb set me hota hain hr item uniq hona same 2 hone pr ek hi count hoga
#print(s)
#print(s[1]) unordered collection ka mtlb aap indexing nhi kr skte hain 


# set kyu use krte hain 
l = [1,2,3,4,5,5,5,5,7,7,8]
#remove duplicate jo same number hain
 
s2 = set(l) # s2 =list(set(l)) set me convert krke phir se list me convert kr skte hain ye sb se importent use hain set ka
print(s2)


# #set methode ,,,,  set me  add kra skte hain
s = {1, 2,3 ,2}
s.add(4)
print(s)

# # set me remove 
#s.remove(3)
#print(s)

## Discard method  jb ko number set me nhi hain or remove krne ki kosis kr rhe ho to error aa rha hoga to uiske jgh ye method use kr skte hain
#s.discard(4)
#print(s)

## Clear method 
#s.clear
#print(s)

## copy method
#s1 = s.copy
#print(s1)



## set me aap kya kya stor kr skte hain
# set me aap list or dicsanry ko store nhi kr skte hain
#s = {1, 2,3 ,2}
s = {1, 1.2 ,'Niranjan'} # ye sb store kr skte hain
print(s)









