# looping in tuples
mixed = (1,2,3,4,5,)
# for loop and tuple
for i in mixed:
    print(i)


# tuple with one element
# aapko  ek aise  tuple bnana ho jisme bs ek hi element ho 
nums = (1,) #  python jb aisa bnan ho ki ek hi elment hain to , lgana pdhega jis python ko pta chle ki ye tuple  hain
word = ('Niranjan1')
print(type(nums))



# tuple without praenthesis
guitars = ' yamaha', ' baton rouge', 'taylor'
print(type(guitars))


# tuple unpacking 
guitarists = ('Niranjan', 'Chitranjan', 'Arjun')
guitarist1 , guitarist2, guitarist2 = (guitarists)
print(guitarist1)


# list inside tuples
# but liat ke ander sb kr skte hin
favorites = ('Niranjan', [ 'Arjun', 'Chitranjan'])
favorites[1].pop()
print(favorites)



# some functions that you can use with tuples
# min ,, max ,sum 

# print(max(mixed))


