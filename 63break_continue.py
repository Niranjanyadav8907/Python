# break and continue keyword

# break keyword ka hmm use loop ko rokne keliye krte hain (loop ko khtm krne keliye bol skye hain )

#1 se 10 tk print 
for i in range(1, 11):
   print(i)   # aise likhne pr 1 se 10 tk asani se print ho jayga but hmme 5 tk hi print krana ho to dekhte useke liye kya krte hain


for i in range(1, 11):
  if i == 5: # condtion lgaa kr check kr liya 
   break
  print(i)


# continue keyword
# print 1 to 10 , but not 5
# example aise print krana ho to 1,2,3,4,6,7,8,9,10
  
for i in range(1,11)  :
  if i == 5:
    continue # continue ke baad shide jump krke phir se loop 6 pr chla jata hain
  print(i)
  
    

