#--------password generator-------------


import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",  "M", "N", "O",  "P", "Q", "R",  "S", "T", "U",  "V", "W", "X",  "Y", "Z" , "a", "b", "c",   "d", "e", "f",  "g", "h", "i",  "j", "k", "l",  "m", "n", "o",  "p", "q", "r",  "s", "t", "u",  "v", "w", "x",  "y", "z",]
numbers = ["0", "1", "2", "3",   "4", "5", "6",  "7", "8", "9",]

symbols = ["!" ,"@", "$", "#", "%", "^", "&", "*", "(", ")", "+", "="]

#--------password in easy mode----------

print("welcome to PyPassword generator")

nr_letter = int(input("enter the number of letter you need in your password \n"))

nr_number = int(input("enter the number of numabers you need in your password \n"))

nr_symbols = int(input("enter the numbe of symboles you like in your password"))


password = " "
for char in range(1, nr_letter + 1):
    password += random.choice(letters)

for num in range(1, nr_number + 1):
    password += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print (f"your password in essy mode is : {password}")





#-------password in hard mode--------


print("welcome to PyPassword generator")

nr_letter = int(input("enter the number of letter you need in your password \n"))

nr_number = int(input("enter the number of numabers you need in your password \n"))

nr_symbols = int(input("enter the numbe of symboles you like in your password \n"))


password_list = []
for char in range(1, nr_letter + 1):
    password_list.append (random.choice(letters))

for num in range(1, nr_number + 1):
    password_list += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
    
random.shuffle(password_list)


password = " "
for char in password_list:
    password += char  
    
print (f"your password in hard mode is : {password}")

