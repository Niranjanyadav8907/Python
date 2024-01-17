user_info = {
    'name' :'Niranjan',
    'age': 22,
    'fav_movies' : ['jai  ho', 'animal', 'red'],
    'fav_tunes' : [ 'raam ', 'raam raam'],
     
}

more_info = {'state': 'up', 'mathura' :['niranjan', 'reading', 'python']}
# ye line mai apne dic me add krna chahta hu 
# sbse pahle jis dic me aaapko data ko  add krna hain uska naam likhiye phir .update

user_info.update(more_info)
print(user_info)


