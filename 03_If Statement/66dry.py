# DRY --dont't repeat yourself mtlb ek hi code ho dobara dobara n likhe same code me 


#winning_number = 43
#guess = 1
#number = int(input ("guess a number between i and 100 : "))
#game_over = False


#while not game_over: # while loop islie chla rha hu kyu ki mujhe nhi pta user kb tk jeet n jaay
    #if number == winning_number:
        #print(f"you win, and you guessed this number in {guess} time ")
        #game_over = True
    #else:
        #if number < winning_number: # if hmm do condtione check krenge ya use jeet gya ya uses low guess kiya ya high
            #print("too low ")
            #guess += 1 .......# same code
            #number = int(input("guess again : "))
        #else :
            #print("too high") 
            #guess += 1 ...... # same code isi ko htane shikhenge DRY principle code me 
            #number = int(input("guess again : "))


winning_number = 43
guess = 1
number = int(input ("guess a number between i and 100 : "))
game_over = False


while not game_over: # while loop islie chla rha hu kyu ki mujhe nhi pta user kb tk jeet n jaay
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} time ")
        game_over = True
    else:
        if number < winning_number: # if hmm do condtione check krenge ya use jeet gya ya uses low guess kiya ya high
            print("too low ")
            
        else :
            print("too high") 
            guess += 1
            number = int(input("guess again : "))

