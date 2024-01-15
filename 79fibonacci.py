# fibonacci series
# 0 1 1 2 3 5 8 13 21 34
#fibonacci series me pahla or dusra number fiax rhta hain 0 or 1
# or tisra number hota hain 1 ye pahle or dusre ka sum hota 0+1 = 1 aise hi left side se 2 sum krte jate hain

# 1-----> 0
# 2-----> 0 1
# 3-----> 0 1 1 

#for i in range(1,11):
 #   print(i, end = " ")


#main code 

def fibonacci_seq(n):
    a = 0 # first number fibonacci ka 
    b = 1 # second number
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b) # a b , 0, 1 aap comma lga kr ko chij print krate hain (space separated print)
    else:
        print(a,b, end = " ") 
        for i in range (n-2):
            c = a + b # c = 1 ,2 ,3
            a = b  # a = 1 , 1 , 2
            b = c    # b = 1 ,2 , 3 loop chl rha hain
            print(b, end = " " )

fibonacci_seq(10)






