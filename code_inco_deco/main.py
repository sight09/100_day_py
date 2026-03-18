
##-----code encoder and decoder------

alphabet = ['a', "b", "c", "d", "e", "f", "g",'h',"i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", 'a', "b", "c", "d", "e", "f", "g",'h',"i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



##--------compact version of encode/decode-----------

def ceaser(start_text, shift_amount, cipher_diraction):
    end_text = ""
    if cipher_diraction == "decode" :
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_diraction}d text is {end_text} ")    
        







# -------simpler version of encode/decode----------

def encrypt (plaine_text, shift_amount ) :
    cipher_text = ""
    for letter in plaine_text :
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text} ")
        
def decrypt (plaine_text,shift_amount ) :
    cipher_text =""
    for letter in plaine_text :
        position = alphabet.index( letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"The decoded text is {cipher_text} ")

if direction == "encode" :
    encrypt(plaine_text=text, shift_amount=shift)
    
elif direction == "decode" :
    decrypt(plaine_text=text, shift_amount=shift)
else:
    print("please text the corecet comand")  







should_continue = True
while should_continue:

    direction = input("Type 'encode', to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your messeg: \n").lower()
    shift = int(input("Type the sift number:\n"))

    shift = shift % 26   


    ceaser(start_text=text, shift_amount=shift, cipher_diraction= direction)

    result = input("Type 'yes' if you want to again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

