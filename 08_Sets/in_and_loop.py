# in keyword in sets and for lop

s = {'a', 'b', 'c'}

#in keyword to check if item is present or not in set 
if 'a' in s:
    print("present")
else:
    print("not present")


# for loop   
for item in s:
    print(item)


# set maths mtlb set me kuchh mathematical operations kr skte hain
# union (jo dono me hai use combine karna)
# intersection ( jo dono cooman ho)

s1 = {1,4,5,6}
s2 = {3,4,5,6}

# union {1,2,4,5,6}
# | union keliye ye use krte hain
union_set = s1 | s2
print(union_set)


# intersection 
print(s1 & s2)

