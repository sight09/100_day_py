#BMI formula

# h = input ("enter  ur hight in meter")
# w = input("enter ur wight in kg")


# bmi = int (w)/float(h)**2
# bmis = int (bmi)
# print (bmis)


#f function

# sco = 0
# hi = 3
# win = 4

# print(f"ur scoree is {sco} ur hiig id {hi} and ur win is {win}")



# age reamaining calculator

# age =input("what is ur current age ")

# month_left =90 - int(age)
# week_left =90 - int(age)
# day_left =90 - int(age)



# day = (day_left)*365
# week = (week_left)*56
# month = (month_left)*12

# print(f"if u live for 90 years you left with {day} days, {week} weeks, and {month}months")










#bill calculater

# print("welcome to tip calcualater")

# amount = input("enter the amount of the bill ?")

# tip_perc = input("what parcentage tip u would like to give ? 10 ,12 or 15")
# perc = input("enter the amount of person it shoul dived")

# p =int( tip_perc)/100 

# tip = int (amount) * p

# total = int(amount) + tip
# in_person = total/int(perc)

# print(f"all should pay {in_person}")




# odd or even

# number = int(input("what number do u weant to check ?"))

# if number % 2==0:
#     print("it is even")
# else:
#     print("it is odd")    



# h = float(input("enter ur hight in meter "))
# w = float(input("enter ur wight in kg "))


# bmi = w / h**2

# if bmi < 18.5:
#     print ("ur underweghit")

# elif bmi > 18.5 :
#         print ("ur normal wight")
        
# elif bmi > 25 :
#         print("ur over wight")
        
# elif bmi > 30:
#         print("ur obese")
# else:
#     print("clinically obes")                






# leao or not

# leap = int(input("enter the year u wanna to check"))

# if leap % 4 == 0:
#     if leap % 100 == 0:
#         if  leap % 400 == 0:
#             print("leap")
#         else:
#             print("not")    
#     else:
#         print("leap")
# else:
#     print("not ") 






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




# print ("welcome to Trueasure Island")
# print ("Your mission is to find the treasure")

# go =input("you are at a cross road, where do u wanna go ? left or right \n")
# if (go == "left"):
#     swim = input("you come to a lake, there is an island in the middle of the lake, what do u wanna do ? swim or wait \n")
#     if (swim == "wait"):
#         door = input("you arrive at the island unharmed, there is a house with 3 doors. one red, one yellow and one blue. which colour do u choose ? \n")
#         if (door == "yellow"):
#             print("you win")
#         elif (door == "red"):
#             print("burned by fire. game over")
#         elif (door == "blue"):
#             print("eaten by beasts. game over")
#         else:
#             print("game over")
#     else:
#         print("attacked by trout. game over")





# import random

# random_num = random.randint(0, 10)

# print(random_num)

# random_float = random.random()

# rand = random_float*5
# print(rand)




# #random H or T

# import random

# random_side = random.randint(0, 1)

# if random_side == 1:
#     print("head")
# else:
#     print("tails")


# #random bill payer

# import random
# name_string = input("Give me everybody's name, saparated by a comma and space ")

# names = name_string.split(",")


# random_name = random.choice(names)

# print(f"today's bill is going to {random_name} 🫣")




# #---------replacing by X-----------

# row1 = ["⏹️","⏹️","⏹️"]
# row2 = ["⏹️","⏹️","⏹️"]
# row3 = ["⏹️","⏹️","⏹️"]

# map = [row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = input("wwhere do you need to put the treasure ?")

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")





#------paper sesor and rock---------

# import random

# user =  input("what do you weant for rock type 1 for scessorice type 2 for paper type 3")
# print(user)

# # user.lower()

# game = ["scissors", "rock", "paper",]

# computer = random.randint(0,2)
# print(f"computer{computer}")

# if user == 0 and computer == 2:
#     print(f"u win")
# if computer == 0 and user == 2:
#     print(f"u lose")
# elif computer > user:
#     print("you lose")
# elif computer == user:
#     print("draw")

# print(f"you chose {user} and computer chose {computer} so ")
# if computer == "scissors" and user =="papare" :
#     print("computer")
# elif computer == "papare" and user == "scissors":
#     print("user")
# elif computer == "scissors" and user == "rock" :
#     print("user")
# elif computer == "rock" and user == "scissors" :
#     print("comp")
# elif computer =="rock" and user == "papare":
#     print("user")
# elif computer=="papare" and user == "rock":
#     print("computer")
# elif str(computer) == str(user) :
#     print("defalut")
# else :
#     print("noo")
# if user == "scissors" and computer == "papare":
#     print("user win")
# elif user == "rock" and computer == "sicissors" :
#     print("user win")
# elif user == "paper" and computer =="rock" :
#     print("user win")
# else:
#     print("computer win")





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



# #----------FizzBuzz game--------

# for n in range(1,101):
#     if (n % 3 == 0 and n % 5 == 0):
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizze")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)






#--------password generator-------------


# import random

# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",  "M", "N", "O",  "P", "Q", "R",  "S", "T", "U",  "V", "W", "X",  "Y", "Z" , "a", "b", "c",   "d", "e", "f",  "g", "h", "i",  "j", "k", "l",  "m", "n", "o",  "p", "q", "r",  "s", "t", "u",  "v", "w", "x",  "y", "z",]
# numbers = ["0", "1", "2", "3",   "4", "5", "6",  "7", "8", "9",]

# symbols = ["!" ,"@", "$", "#", "%", "^", "&", "*", "(", ")", "+", "="]

#---------password in easy mode----------

# print("welcome to PyPassword generator")

# nr_letter = int(input("enter the number of letter you need in your password \n"))

# nr_number = int(input("enter the number of numabers you need in your password \n"))

# nr_symbols = int(input("enter the numbe of symboles you like in your password"))


# password = " "
# for char in range(1, nr_letter + 1):
#     password += random.choice(letters)

# for num in range(1, nr_number + 1):
#     password += random.choice(numbers)

# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# print (f"your password in essy mode is : {password}")





#-------password in hard mode--------


# print("welcome to PyPassword generator")

# nr_letter = int(input("enter the number of letter you need in your password \n"))

# nr_number = int(input("enter the number of numabers you need in your password \n"))

# nr_symbols = int(input("enter the numbe of symboles you like in your password \n"))


# password_list = []
# for char in range(1, nr_letter + 1):
#     password_list.append (random.choice(letters))

# for num in range(1, nr_number + 1):
#     password_list += random.choice(numbers)

# for sym in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
    
# random.shuffle(password_list)


# password = " "
# for char in password_list:
#     password += char  
    
# print (f"your password in hard mode is : {password}")




#--------HANGMAN GAME ------------

import random
word_list = ["ardvark", "baboon", "camel"]

rn_word = random.choice(word_list)
print(rn_word)

gusse = input("gusse the letter ").lower()


display = []



for word in rn_word:
    display.append("_")
    
    if gusse == word:
        display.append(gusse)
    
        
        
print(display)
    # print(word)
    # if word == gusse:
    #     print("ur right")
    # else:
    #     print("WRONG")


