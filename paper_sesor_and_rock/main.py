#------paper sesor and rock---------

import random

user =  input("what do you weant for rock type 1 for scessorice type 2 for paper type 3")
print(user)

user.lower()

game = ["scissors", "rock", "paper",]

computer = random.randint(0,2)
print(f"computer{computer}")

if user == 0 and computer == 2:
    print(f"u win")
if computer == 0 and user == 2:
    print(f"u lose")
elif computer > user:
    print("you lose")
elif computer == user:
    print("draw")

print(f"you chose {user} and computer chose {computer} so ")
if computer == "scissors" and user =="papare" :
    print("computer")
elif computer == "papare" and user == "scissors":
    print("user")
elif computer == "scissors" and user == "rock" :
    print("user")
elif computer == "rock" and user == "scissors" :
    print("comp")
elif computer =="rock" and user == "papare":
    print("user")
elif computer=="papare" and user == "rock":
    print("computer")
elif str(computer) == str(user) :
    print("defalut")
else :
    print("noo")
if user == "scissors" and computer == "papare":
    print("user win")
elif user == "rock" and computer == "sicissors" :
    print("user win")
elif user == "paper" and computer =="rock" :
    print("user win")
else:
    print("computer win")