# functione practice

# to ek fun define krte hain jo as a input ek paira miter lega ek name lega or hmme or hmme return krega use name ka last chr

def last_char(name):
    return name[-1]

print(last_char("Niranjan kumar yadav"))

#for example odd hai ya even ek aisa fun define krte hain 

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
print(odd_even(9))   

#isko ab hmm thoda chhote me krte hain 

def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"
print(odd_even(10)) 

# ab ek funnction define krte is-_ven

def is_even(num) :
    if num%2 == 0:
       return True
    else:           # ya pr aap else hta kr return false ko bahr nikal skte hain
        return False
print(is_even(9))


# ab isko chhote tarike se krte hain 

def is_even(num):
    return num%2 == 0
print(is_even(10))

#parameter or argument in python ??

#function  define ko parameter ex-- num
#function call ko argumet ex ---10

# hmm abhi tk jo function define jo kiye wo sb input me kuchh le rhe the hmm hmm dekhte hain jo input me kuchh n le rhe ho 

def song():
    return "jai mata dii"
print(song())









    
