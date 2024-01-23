# dictionary comprehension ----- dictionary Mein key value pair hote hain

# square = {1:1, 2:4, 3:9}

#dictionary me comprehension use krke square kaise nikal skte hain
square = {num:num**2 for num in range(1,11)}
print(square)
# 1 :1
# 2: 4
# 3: 9... abhi to aise square print ho rha hain


#but ab aise krke dekhte hain ...( 1 is square 1, 2 square 4 )
square = {f"square of {num} is":num**2 for num in range(1,11)}
print(square)

## agr aap alg alg line me print krana chahte hain to foor loop use kr skte hain
square = {f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")


## example 2  (aapko count karna hai kisi string me koi chr kitne baar hain
    
string = "Niranjan"
word_count = {char:string.count(char) for char in string}
print(word_count)

#alg alg line me print krane keliye 
string = "Niranjan"
for i in string:
    print(i)
