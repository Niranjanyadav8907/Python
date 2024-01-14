# ek function bnaaiye jo check kre 3 number me bdha kon hain 

def greater(a,b,c ):
    if a>b and a<c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(greater(10,20,30))

