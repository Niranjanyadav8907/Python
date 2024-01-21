# list comprehension with if statement

numbers = list(range(1,11))
# [1, 2, ,3, 4, 5, 6, ,7,  8, 9, 10]
# even_nums = [2,4,6] # hmme print krana hain even number 1 se 10 ke bich me 

nums = []
for i in numbers:
    if i%2 == 0: # 1 likh odd number bhi print kra skte hain 
        nums.append(i)
print(nums)

#comprehension use krke

even_nums1 = [i for i in numbers if i%2 == 0]
even_nums2 = [i for i in range(1,11) if i%2 == 0]
print(even_nums1)
print(even_nums2)


