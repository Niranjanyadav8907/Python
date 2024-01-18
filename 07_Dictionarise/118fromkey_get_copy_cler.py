# fromkes key kaise bnate hain
#d ={'name' : 'unknown', 'age' : 'unknon'}

d = dict.fromkeys(['name', 'age', 'height'], 'unknowan') # list ki key bnana hain name, age height or sbhi key ki value unknown
print(d)


d = dict.fromkeys("age",'unknowan') # agr aap stringe likhenge to alg alg key bn jayga
print(d)


d = dict.fromkeys(range(1,11), 'unknowan') # agr aap 1 se 10 number print karange to 1 se 10 tk alg alg key bn jayga 
print(d)


# aap value me kuchh bhi dal skte hain 
d = dict.fromkeys(['name', 'age'],['unknowan', 'unknowan'])
print(d)


# get method kaafi use full methode hain 
# for example mere pass ek dictionarise hain muhje  dic me se  ek key ko accses krna hain

d ={'name' : 'unknown', 'age' : 'unknon'}
#print(d['name'])

print(d.get('name')) # aise likh kr aap accses  kr skte hain  ((name jhg aisa kuchh likh de jo dicsanry me hain hi nhi  to error retun nhi kreaga uske jgh pr nun return krega 

print(d.get('names')) # name ki ke jg pr kuchh or likhne pr


if d.get('names'):
    print('present')
else:
    print('not present')


# if none---------> false   else -------> true


#dictionarise clear method   
d ={'name' : 'unknown', 'age' : 'unknon'}
d.clear()
print(d)


# copy method 
d1 = d.copy()
print(d1)








