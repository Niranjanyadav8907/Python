
# filter function 

def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,7,9]

evens = tuple(filter(is_even,numbers)) # lamda use 
print(evens)


# filter function kisi number ya string ko user ke prticuler
#istrekchar ko follow kr ke deta hain
#filter function me bhi lambda use kr skte hain

##......evens = tuple(filter(lambda a:a%2==0,numbers))


