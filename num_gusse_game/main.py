#-------gusse the number game ------------

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(gusse, num, turns):
    if num < gusse:
        print("it is too high")
        return turns -1
    elif num > gusse:
        print("it's to low")
        return turns-1    
    elif num == gusse:
        print("you got it")


def set_difficulty():
    level = input("Choose a difficulty. Type 'essy' or 'hard' : ")
    if level == "essy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print("Welcome to the Number Guessing Game ! ")
    print("I'm thinking of a number between 1 and 100.")
    num = randint(1, 100)
    print(num)


    turns = set_difficulty()
    

    gusse = 0
    while gusse != num:
        print(f"you have {turns} attempts remaning to guess to the number ")
        gusse = int(input("gusse a  : "))


        turns = check_answer(gusse, num, turns)
        if turns == 0:
            print("you've run out of gusses, you lose")
            return
        elif turns != num:
            print("GUSSE AGAIN")
            
            
            
game()
