
l1 = [1,3,4,7]
l2 = [2,4,6,8]

l = [(1,2), (3,4), (5,6), (7,8)]

# l se aapko l1,l2 jaisa zip list bnnana hain
# * operator with zip

#print(list(zip(*l)))  # 2 no list ko alg line me kaise pritn kr skte hain

l1, l2 = (list(zip(*l)))
print(list(l1))
print(list(l2))

# number ke hisanb se kaise print kra skte hain small to big number

l1 = [1,3,4,7]
l2 = [2,4,6,8]

new_list =[]
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)




