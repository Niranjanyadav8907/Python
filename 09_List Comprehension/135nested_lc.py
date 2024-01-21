# list comprehension in nested list

# nested list ka mtlb hota hain list ke ander list

example = [[1,2,3] , [1,2,3] ,[1,2,3]]

nested_camp = [[i for  i in  range(1,4)] for j in range (3) ]
print(nested_camp)


# normal tarike se kaise krte the

new_list  = []
for j in range(3):
    new_list.append([1,2,3])
print(new_list)    