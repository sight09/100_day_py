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






print ("welcome to python pizza delivary")

size = input("what size pizza do u wanna S, L or M ")
add_pepp = input("do u need pepperoni  Y or N ? ")
extra_chess = input("do u need extra chess Y or N? ")


S = 15
L = 25
M = 20
pepp_small = 2
pepp_med_and_larg = 3
ext_ch = 1

if size == "S":
    if add_pepp == "Y":
        if extra_chess == "Y":
            print (f"ur total bill is {S + pepp_small + ext_ch}")
        else:
            print (f"ur total bill is {S + pepp_small}")
    else:
        print (f"ur total bill is {S}")

elif size == "L":
    if add_pepp == "Y":
        if extra_chess == "Y":
            print (f"ur total bill is {L + pepp_med_and_larg + ext_ch}")
        else:
            print (f"ur total bill is {L + pepp_med_and_larg}")
    else:
        print (f"ur total bill is {L}")

elif size == "M":
    if add_pepp == "Y":
        if extra_chess == "Y":
            print (f"ur total bill is {M + pepp_med_and_larg + ext_ch}")
        else:
            print (f"ur total bill is {M + pepp_med_and_larg}")
    else:
        print (f"ur total bill is {M}")

























