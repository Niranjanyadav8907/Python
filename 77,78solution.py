# Define is_palindrome function that take one word in string as input
# and return True if it is palindrome else return False
# palindrome word that reads same backwards as forwards

# example
# is_palindrome("madam")
#---> True

# is_palindrome("naman")
#---> True
# is_palindrome("horse") ---> False
# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string

def is_palindrome(word):
    reversed_word = word[::-1] # string reverse [::-1] se hota hain
    if word == reversed_word:
        return True
    else:
        return False
    
print(is_palindrome("naman"))
print(is_palindrome("horse"))

# ab isko chhota krte hain

def is_palindrome(word): 
    if word == word[::-1]:
        return True
    return False
print(is_palindrome("naman"))
print(is_palindrome("horse"))





    