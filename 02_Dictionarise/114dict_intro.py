#Q - why we use dictionaries?
# A -Because of limitations of lists, lists are not enough to represent
# real data.

# Example
#user = ['Niranjan', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]

# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this.

#Q what are dictionaries
# A unordered collections of data in key value pair.

# how to create dictionaries # pala tarika dic ko creat krne ka
 
#user = {'name': 'Niranjan', 'age': 22}
#print(user)
#print(type(user))

# second method to create dictionary

#user1 = dict(name ='Niranjan', age = 22) # idr name me '','' cote lgane ki jarurat nhi hain
#print(user1)

# how to access data frome dictionary
# NOTE- there is no indexing because of unorded collectione of data
# dictionary me data ko accsess krne keliye key ka use krte hain

#for Example 

#user1 = dict(name ='Niranjan', age = 22)
#print(user['name'])


# which type of data a dictionary
#anthing
# numbers , stringe, list ,dictionary

#user = ['Niranjan', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]

#aap aise bhi ek line me dic create kr skte hain


user_info = {
    'name' :'Niranjan',
    'age': 22,
    'fav_movies' : ['xyz', 'jhhkj', 'uouo'],

}
print(user_info['fav_movies']) # aise aap key naaam ke sath acsess kr skte hain





