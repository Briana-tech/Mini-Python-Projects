
def guessANumber():# The computer tries to guess the number the user's thinking of.
    start = 1
    end = 100
    print("Pick a number between " + str(start) + " and " + str(end) + ". ")  # str(variable) converts value to string
    print("I will try to guess it in as few guesses as possible. ") # print(" ") only outputs data
    
    guess = (end + start)//2 # 101 // 2 = 50
    numAttempts = 1 # counts first guess
    response = input("Is " + str(guess) + " too high, too low, or correct? ") #input() gets user input
    response = response.lower()  # Convert response to lowercase to make it easier to compare
    while response != "correct" and response != "stop":
        if response == "too high":
            end = guess - 1
        elif response == "too low":
            start = guess + 1
        else: # If the user inputs something other than too high, too low, or correct
            response = input("Please respond with 'too high', 'too low', or 'correct'. ") #dont use print here bc we still need user input
            response = response.lower()
            continue  # Skip the rest of the loop and ask for input again
        guess = (end + start)//2
        numAttempts = numAttempts + 1 # every time we make a guess, we increase the attempt count by 1
        response = input("Is " + str(guess) + " too high, too low, or correct? ")
        response = response.lower()
      
    print("Your number is " + str(guess) + "!")
    print("I guessed it in " + str(numAttempts) + " attempts.")


def nim(): # Two players take turns nimming (stealing) 1, 2, or 3 stones from the pile.

    print("Welcome to the game of Nim!")
    pile = 15
    print("There are " + str(pile) + " tokens in the pile.")

    winner = ""
    while pile !=0:
        c1Move = p1Move(pile)
        pile = pile - c1Move
        print("Player 1 nims " + str(c1Move) + " tokens. Pile is now " + str(pile) + " .")
        if pile == 0:
            winner = "Player 1"
        else:
            c2Move = p2Move(pile)
            pile = pile - c2Move
            print("Player 2 nims " + str(c2Move) + " tokens. Pile is now " + str(pile) + " .")
            if pile == 0:
                winner = "Player 2"
    print("The winner is " + winner + ". Yay!")
    return 
    

def p1Move(pile): # Player 1's move logic here
    import random
    move = random.randint(1,3)
    if move > pile:
        move = pile

    return move
def p2Move(pile): # Player 2's move logic here
    if pile % 4 != 0: # if the pile is not a multiple of 4
        move = pile % 4 # take the pile divided by 4 remainder
    else:
        move = 1 # otherwise take 1

    return move

    

print("Welcome!")
print("I have two mini-games for you to choose from.")
print("1. Guess A Number")
print("2. Nim")
print("Depending on which game you choose, you may play until you want it to end.")
print("When you're ready to stop playing, say 'stop'. ")
choice = input("Which game would you like to play? (Enter 1 or 2) ")
choice = choice.lower()
while choice != "stop":
    if choice == "1":
        guessANumber()
        choice = input("Which game would you like to play? (Enter 1 or 2) ")
        choice = choice.lower()
    elif choice == "2":
         nim()
         choice = input("Which game would you like to play? (Enter 1 or 2) ")
         choice = choice.lower()
    else:
     choice = input("Invalid choice. Please enter 1 or 2 to select a game. ")
     choice = choice.lower()