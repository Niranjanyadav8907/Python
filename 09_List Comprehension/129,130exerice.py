#define a function that take list of strings
# list containing reverse of every string

#NOTE USE LIST COMPREHENSION because we already did this exercise
# using normal method

# example
#1 = ['abc', 'tuv', 'xyz']
# reverse_string(1) ----> ['bac', 'vut', 'zyx']

#  ek function difine krna tha jisme bahut sare string hain or hmme output  me hrr string ka  reverse chahiye 

#COMPREHENSION use krke

def reverse_strings(l):
    return[name[:: -1] for name in l]
print(reverse_strings(['Niranjan',  'Arjun', 'Chitranjan']))


# noraml  me  hmm aise krte the 

def reverse_str(l):
    new_list =[]
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_str(['Niranjan',  'Arjun', 'Chitranjan']))


        
 

