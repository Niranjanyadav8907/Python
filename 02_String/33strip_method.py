# exercise number 32 me hmm ne dekha tha ki space  problem kr rha tha ...isme hmm (space ko remove) kaise krte hai dekhte hain 

name = "    Niranjan     " # remove for space 
dots = "................."
#lstrip() - method -----apne string ke LEFT side ke space ko remove krne keliye use krte hain

print(name + dots) # right side dots ka use smjhne keliye kiya gta hain kyu ki right side space ka pta nhi chl rtha tha 
print(name.lstrip()+ dots)
print(name.rstrip() +dots) # Right side ke space ko remove krne keliye
print(name.strip() + dots) # Left right side dono ek sath remove krne keliye

print(name.replace(" ","") + dots) # hmm string chr ke bich ke space ko remove krane kelie use krte hai Example= (Niran   jan)---NIranjan
#strip char ke bich ke space ko remove nhi krta ye ps left right space ko remove krta hain
