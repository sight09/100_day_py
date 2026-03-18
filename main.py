








# odd or even

# number = int(input("what number do u weant to check ?"))

# if number % 2==0:
#     print("it is even")
# else:
#     print("it is odd")    











# print ("welcome to python pizza delivary")

# size = input("what size pizza do u wanna S, L or M ")
# add_pepp = input("do u need pepperoni  Y or N ? ")
# extra_chess = input("do u need extra chess Y or N? ")


# S = 15
# L = 25
# M = 20
# pepp_small = 2
# pepp_med_and_larg = 3
# ext_ch = 1

# if size == "S":
#     if add_pepp == "Y":
#         if extra_chess == "Y":
#             print (f"ur total bill is {S + pepp_small + ext_ch}")
#         else:
#             print (f"ur total bill is {S + pepp_small}")
#     else:
#         print (f"ur total bill is {S}")

# elif size == "L":
#     if add_pepp == "Y":
#         if extra_chess == "Y":
#             print (f"ur total bill is {L + pepp_med_and_larg + ext_ch}")
#         else:
#             print (f"ur total bill is {L + pepp_med_and_larg}")
#     else:
#         print (f"ur total bill is {L}")

# elif size == "M":
#     if add_pepp == "Y":
#         if extra_chess == "Y":
#             print (f"ur total bill is {M + pepp_med_and_larg + ext_ch}")
            
#         else:
#             print (f"ur total bill is {M + pepp_med_and_larg}")
#     else:
#         print (f"ur total bill is {M}")



# bill but left with the chess code is not working

# bill =0

# if size == "S":
#     bill+=15
    
# elif size =="M":
#     bill+=20
    
# else:
#     bill+= 25
    
# if add_pepp == "Y" :
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
            

# if ext_ch == "Y":
#     bill += 1
# else:
#     bill
        


# print (f"ur final bill is {bill}")



# hight = float(input("enter ur hight in cm "))

# if hight >= 120:
#     print("you can ride the rollercoaster")
#     age = int (input("what is your age "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif age >= 45 and age <= 55:
#         print("free")
#     else:
#         bill = 12
#         print("Adult ticket are $12 ")


# want_photo = input("do u wanna photo taken Y OR N")
# if want_photo == "Y":
#     bill = bill + 3
#     print(f"your total bill is {bill}")




# print ("Welcome to the love calculator")
# name1 =input("what is the name of ur \n")
# name2 =input("what is the name of here \n")


# n1 = name1.lower
# n2= name2.lower 









# import random

# random_num = random.randint(0, 10)

# print(random_num)

# random_float = random.random()

# rand = random_float*5
# print(rand)















# #------avg of heghit in loop------------ 

# student_heghit = input("enter the list of the student heghit ").split()
# a = 0
# for n in range(0, len (student_heghit)):
#     student_heghit[n] = int (student_heghit[n])
# print(student_heghit)
# for m in student_heghit:
#     a += m
# print(a/len(student_heghit))




# #----------highest score-------------- 

# score = input("input the list of the student ").split()

# for n in range(0, len(score)):
#     score[n] = int(score[n])
# print(score)
# highest_score = 0
# for n in score:
#     if n > highest_score:
#         highest_score = n
# print(f"the highest score is  {highest_score}")




# #----------adding even number---------

# total = 0

# for n in range(2,101,2):
#     total += n
# print(total)

# #----------OR----------#

# total2 = 0
# for n in range(1, 101):
#     if n % 2 == 0:
#         total2 += n
# print(total2)










   
        
        
        
        
        
        
# def greet():
#     print("hellow")
#     print("welcome to my consule")
#     print("thanks")


# greet()  


  

## with input

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}")
    

# greet_with_name("aman")



# def greet_with (name,location):
#     print(f"hello {name}")
#     print(f"What is it like in {location}")
    
    
# greet_with("aman","agaro")


# import math


# def paint_calc(hight , width , cover):
#     area = (hight* width)
#     num_of_cans = math.ceil (area / cover)
#     print(f"You will need {num_of_cans} cans of paint")
    
    


# test_h = int (input("Hight of wall: "))
# test_w = int (input("Width of the wall: "))
# coverage = 5

    
# paint_calc(hight=test_h, width=test_w, cover=coverage)


















# #--------dictionary-----------

# student_scores = {
#     "Harry" : 81,
#     "Ron" : 78,
#     'Hermione' :99,
#     'Draco' : 74,
#     'Neville ' : 62,
# }


# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = 'Outstanding'
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptabel"
#     else:
#         student_grades[student] = "Fail"


# print(student_grades)        








# #-------dictionary in list--------



# travel_log =[
    
#     {
#         "country": "France",
#         "visits": 12,
#         "cities":["Paris","Lille", "Dijon"]
        
#     },
    
#     {
#         "country": "Germany",
#         "vitis" : 5,
#         "cities" : ["Berline", "Hamburg", "Stuttgart"]
        
#     },
            
            
            
# ]




# def add_new_country(country_visited, time_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = time_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)



# add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg', ])

# print(travel_log)






#-----------bidder-----------



# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner =bidder
#     print(f"the winner is {winner} with a bid of $ {highest_bid}")

# while not bidding_finished:
#     name = input("Enter your name:  ")
#     price = int(input("Enter your bid:  $ " ))
#     bids[name] = price
#     should_continue = input("Are there any bidders? Type 'yes' or 'no'. ")

#     if should_continue == 'no':
#         bidding_finished = True
#         find_highest_bidder(bids)


    # count = input("is there other bid yes or no")
    # if count == 'no' :
    #         go =False
            
        
        
        





#-----title case----------


# def format_name (f_name, l_name, g_name):
#     """Take a first, last and grand pa  name and format it to return the title case version of the name."""
#     if f_name == "" or l_name == "" or g_name == "":
#         return "you didin't provide all valid inputs"
    
#     foramated_f_name = f_name.title()
#     foramted_l_name = l_name.title()
#     foramted_g_name = g_name.title()
#     return f"{foramated_f_name} {foramted_l_name} {foramted_g_name}"
    



# print(format_name(input("What is your name? "), input("What is your father's name "), input("What about your grand pa? ")))







# #----------CALCULATOR-----------

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2



# operations = {
#     "*" : multiply,
#     "/" : divide,
#     "+" : add,
#     "-" : subtract
    
# }

# def calculator():

#     num1 = float(input("what's the 1st number?: "))

#     for sign in operations:
#         print(sign)
        
#     should_continue = True
#     while should_continue:
                
#         op_sign = input("Pick an opration from the line above: ")
#         num2 = float(input("what is the 2nd number?: "))

#         calculation_function = operations[op_sign]
#         answer = calculation_function(num1, num2)


#         print(f"{num1} {op_sign} {num2} = {answer}")    

#         if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start new calculation  ") == "y":
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()
# calculator()







# #---------BLACK JACK-----------

# import random

# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
#     card = random.choice(cards)
#     return card


# def calculate_score (cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards) 

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Draw :("
#     elif computer_score == 0:
#         return "Lose, opponent has Blackjack :() "
#     elif user_score == 0:
#         return "Win, with a Blackjack"
#     elif user_score > 21:
#         return "You went over. You lose"
#     elif computer_score < 21:
#         return "Opponen went over. you win :) "
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose"
# def play_game():
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card() )



#     while not is_game_over:

#         user_score = calculate_score(user_cards)    
#         computer_score = calculate_score(computer_cards)

#         print(f"Your card: {user_cards}, current score: {user_score} ")
#         print(f"Computer's card: {user_cards[0]} ")
            
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == 'y':
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True    

#     while computer_score != 0 and computer_score <17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
        
#     print(f" Your final hand: {user_cards}, final score: {user_score} ")
#     print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")    
#     print(compare(user_score, computer_score))
    
    
# while input("Do you want to paly a game of Blackjack Type 'y' or 'n' ") == "y":
#     play_game() 



# #-------gusse the number game ------------

# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5



# def check_answer(gusse, num, turns):
#     if num < gusse:
#         print("it is too high")
#         return turns -1
#     elif num > gusse:
#         print("it's to low")
#         return turns-1    
#     elif num == gusse:
#         print("you got it")


# def set_difficulty():
#     level = input("Choose a difficulty. Type 'essy' or 'hard' : ")
#     if level == "essy":
#         return  EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():

#     print("Welcome to the Number Guessing Game ! ")
#     print("I'm thinking of a number between 1 and 100.")
#     num = randint(1, 100)
#     print(num)


#     turns = set_difficulty()
    

#     gusse = 0
#     while gusse != num:
#         print(f"you have {turns} attempts remaning to guess to the number ")
#         gusse = int(input("gusse a  : "))


#         turns = check_answer(gusse, num, turns)
#         if turns == 0:
#             print("you've run out of gusses, you lose")
#             return
#         elif turns != num:
#             print("GUSSE AGAIN")
            
            
            
# game()





#--day 13 id debuging------




#-----------day 14 is jumped cuz of resours/by data in future--------




# #----------coffe machine-------------

# MENU = {
#     "espresso" : {
#         "ingredient" : {
#         "water" : 58,
#         'coffee': 18
#         },
#         'cost': 1.5,
#     },
#     "latte" : {
#         "ingredient": {
#             "water" : 200,
#             "milk" : 150,
#             "coffee" : 24,
#             },
#         "cost" : 2.5
#     },
#     "capppuccino" : {
#         'ingredient':{
#             "water" : 250,
#             'milk': 100,
#             'coffee':24,
#         },
#         "cost": 3.0
        
#     }
    
# }
# profit = 0
# resources = {
#     "water" : 300,
#     'milk' : 200,
#     "coffee" : 100,
# }


# def is_resoure_sufficient(order_ingredient):
    
#     for item in order_ingredient:
#         if order_ingredient[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}")
#             return False
#     return True


# def process_coins():
#     """returne the total calculated form coins inserted"""
    
#     print("pleas insert coins")
#     total = int(input("how many quarters? ")) * 0.25
#     total += int(input("how many dimes? ")) * 0.1
#     total += int(input("how many nickels? ")) * 0.5
#     total += int(input("how many pennies? ")) * 0.1
#     return total


# def is_transaction_seccesful(mony_recevied, drink_cost):
    
#     if mony_recevied >= drink_cost:
#         change = round(mony_recevied - drink_cost, 2)
#         print(f"here is the cash u inserted ${change}")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("sorrt that is not enough money. ")
#         return False


# def make_coffee(drink_name, order_ingredient):
#     for item in order_ingredient:
#         resources[item] -= order_ingredient[item]
#     print(f"here is ur {drink_name}")        



# is_on =True

# while is_on:
#     choice = input("what u like (capppuccino/latte/espresso) ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#             print(f"water : {resources['water']}ml")
#             print(f"milk :{resources['milk']}ml ")
#             print(f"coffee :{resources['coffee']}g ")
#             print(f"money : {profit}")
#     else:
#         dirnk = MENU[choice]
#         if is_resoure_sufficient(dirnk["ingredient"]):
#             payment = process_coins()
#             if is_transaction_seccesful(payment, dirnk["cost"]):
#                 make_coffee(choice, dirnk["ingredient"])








# #---------turtel is moving----------

# from turtle import Turtle, Screen
# tinny = Turtle()
# print(tinny)
# tinny.shape("turtle")
# tinny.color("red")
# tinny.forward(100)
# tinny.left(120)
# tinny.forward(100)
# tinny.left(120)
# tinny.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()










# #------crate a tabel------



# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("type", ["Electirc", "Water", "Fire"])
# table.align = "r"
# print(table)





#--------coffee machine in oop day 16----------
#----
#-------
#---------







class User:
    
    
    