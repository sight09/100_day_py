
#--------HANGMAN GAME ------------

import random

        
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
rn_word = random.choice(word_list)
word_length = len(rn_word) 


lives = 0

print(rn_word)

display = []
for _ in range(word_length):
    display+= "_"



while not end_of_game:
    gusse = input("gusse a letter ").lower()
    
    
    if gusse in display:
        print (f"You have already gussed {gusse}")
        
    
    
    for position in range(len(rn_word)):
        letter = rn_word[position]
        if letter == gusse:
            display[position] = letter               


                
                
                                
    if gusse not in rn_word:
        print(f"You guessed {gusse},that's not in the word.You lose a life.")
        lives += 1
        if lives == 6:
            end_of_game = True
            print("You lose.")
        
    print(f"{' '.join(display)}")

        
        
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    
    
    
    print(HANGMANPICS[lives])    
        
        