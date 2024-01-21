
# list comprehension with if else

nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4,-3,8]  # odd number ko - krna hain or even number ko 2*2 krna hain

new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-1)
print(new_list)

#list comprehension ke sath

new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]
print(new_list)
