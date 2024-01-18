# Q--Ask user to input 3 numbers and you have to print average of three numbers using string formatting.

Bonus :- try to take all three comma separated inputs in one line. In python short and simple code
#num1 = input("enter first number :")
#num2 = input("enter second number:")
#num3 = input("enter third number :")
#(int(num1) + int(num2) +int (num3)) /3

#i line me likhne keliye
num1, num2, num3,= input("enter three numbers comma separted:").split(",")

print(f"average of three numbers : {(int(num1) + int(num2) + int(num3)) / 3}")
