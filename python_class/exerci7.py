#exercise, number geussing game
#make a variable , like winning_number and assign any number to it.
#ask user to geuss a number.
#if user geussed correctly then print "you win!!"
#if user didn"t guessed correctly then:
    #if user geussed lower than actual number then print "too low"
    #if user geussed higher than actual number then print "too high"

#google "how to generate random number in python "to generate random 
#winning number
winning_number = 55
user_input = input("geuss a number between 1 to 100:")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN!!!")
else:
    if user_input <winning_number:
        print("too low")
    else:
        print("too high")    
