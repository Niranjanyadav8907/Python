# sets comprehension......

#set bnana hain 1 se 10 tk ka square
# set comprehension me aap {k:v} aise nhi likh skte hain nhi to dictionary creat ho jaayga

s = {k**2 for k in range(1,11) }
print(s)       # set me koi oder nhi hota kaise bhi print ho skta hain


# example 2 aapke pass koi hain name la list hain name ke aapko frist chr print kran ho set me 

name = ['Niranja'  , 'Arjun',  'Chitranjan']
first = {name[0] for name in name}
print(first) 

