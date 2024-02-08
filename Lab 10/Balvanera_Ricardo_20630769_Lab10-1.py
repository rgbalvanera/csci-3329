#import any libraries necessary 
import random

#initiate loop controller & while loop 
continue_game = True
while continue_game:
#output game rules
    print("Start Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
#input message
    choice = int(input("What do you want to throw?"))\
#generate random number
    computer_move = random.randint(1,3)

#output versus message 
    print(f"Computer: {['Rock', 'Paper', 'Scissors'][computer_move - 1]} vs You: {['Rock', 'Paper', 'Scissors'][choice - 1]}")
#shout outs to my cousin fernando who tought me how to do the previous output in only one line and not 4

#calculate and print result
    result = choice - computer_move
    if(result == 0):
        print("It's a tie!")
    elif(result == 1 or result == -2):
        print("You win!")
    elif(result == -1 or result == 2):
        print("You lose! :(")
    
    #ask the user if they want to continue playing
    keep_playing = input("Do you want to play again? (y/n)")
    if(keep_playing == "n" or keep_playing == "N"):
        print("Thank you !!!")
        continue_game = False
