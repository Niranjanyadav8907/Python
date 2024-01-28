
# any, all function
# any ek alg function hai or all ek alg function hain

numbers1 = [2,4,6,8,10]
numbers2 = [1,2,4,5,6,7]

# for example aapko pta lgana hain num1 sare number even hain ya nhi 
# aap hr number ke baad even hain [2 True], [4 True]
evens1 = []
for num in numbers1:
    evens1.append(num%2==0)

#print(evens1)
print(all([True, True, True, True, True])) # all function check krta hai sare 

# True hain ya nhi 


