#bill calculater

print("welcome to tip calcualater")

amount = input("enter the amount of the bill ?")

tip_perc = input("what parcentage tip u would like to give ? 10 ,12 or 15")
perc = input("enter the amount of person it shoul dived")

p =int( tip_perc)/100 

tip = int (amount) * p

total = int(amount) + tip
in_person = total/int(perc)

print(f"all should pay {in_person}")

