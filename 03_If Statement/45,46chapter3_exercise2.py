#EXERCISE WATCH COCO
#Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
#Print you can watch coco movie
#Else print 'sorry, you cannot watch coco


#SOLUTIONE .= 10 ....10 se bdhe age vale dekh skte hai or 10 chhote nhi

user_name = input("enter your name please :")
user_age = input("enter your age please :")
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='a'  or user_name[0] =='A'):  # and isliye kyu dono condtion true hona chahiye name and age
 print("you can watch coco") 
else:
    print(" you cannot wath coco")
