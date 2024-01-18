user_info = {
    'name' :'Niranjan',
    'age': 22,
    'fav_movies' : ['xyz', 'jhhkj', 'uouo'],
    'fav_tunes' : [ 'awakening', 'fairy tale'],

     
}

## how to add data dictionaries me kaise add krte hain

#user_info['fav_songs'] = ['songe1', 'songe2']
#print(user_info)

##pop method  dic me kuchh delete krne keliye ye string return krta hain

popped_item = user_info.pop('fav_tunes')
print(f"popped item is {popped_item}") 
print(user_info)
# pale key likhenge phir remove kr dega uske baad value ko return kr dega 


# #popitem method-- randemly koi bhi key value delet krne keliye popitem ka use krte hain

popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item)) # tuple return krta hain popitem 




