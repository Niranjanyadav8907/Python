# 2 number me se greater kon sa hain
def greater(a,b):
    if a > b :
        return a
    else:
        return b
    

# 3 number me se greatest kon sa hain
def greater(a,b,c ):
    if a>b and a<c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
#function inside function  
    
#greater(a,b )------ a or b sb se pahle hmm check kiya a or b me se kon sa bdha hai bta diya 
#greater(a or b , c )-----> uske baad hmm ne  greatest dobara call kiya a b  pass kiya or sath me c bhi kiya 

def new_greatest(a,b,c ):
    bigger = greater(a,b)
    return greater(bigger, c)
print(new_greatest(10,20,30))

    
    

    
