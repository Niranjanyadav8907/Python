
# lambda expression practics

def is_even(a):
    if a %2 ==0:
        return True
    return False


##same pro.. ko lambda kaise chhota likh skte hain

def is_even(a):
    return a %2 == 0   # a%2 == 0 --- True, False
print(is_even(6))

#lambda use krke same pro
iseven2 = lambda a : a%2==0
print(iseven2(6))

## example 2 or function lambda me kaise difine kr skte hain
# ek function difine krte hain jo string ke last chr print kre

last_char = lambda s : s [-1]
print(last_char('Niranjan'))

# lambda expression me  if ,else ko kaise use krte hain

def func(s):
    if len(s) > 5:    # 5 se jyda chr hona chahiye 
        return True
    return False

func = lambda s : True if len(s) > 5 else False
print(func('abs'))

#same code ko chote me change karte hain

def func(s):
    return len(s) > 5

func = lambda s : len(s) > 5
print(func('abdggs'))







