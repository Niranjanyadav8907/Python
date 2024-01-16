## generate list with range functione
#numbers = list(range(1,11))
#print(numbers)



## somthinge more about pop method
#numbers = list(range(1,11))
#print(numbers)
#poppoed_item = numbers.pop ----- pop krke ye return bhi krta hain 
#numbers.pop()
#print(numbers)


## index method apne list me fine krna hai prticuler number kaha pr hain

#numbers = list(range(1,11))
#numbers = (1,2,3,4,5,6,7,8,9,10,1)
#print(numbers.index(1)) #  .index(1,3) ager list me same number 2 baar hai to hmm bta skte hai ki kaha se start krna hai or dusre number ka positione jan skte hain


# pass list to a function  hmm apne function ke ander list bhi pass kr skte hain 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))



