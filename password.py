# Password Generator Project
from operator import truediv
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for l in range(0, nr_letters):
    randomPostion = random.randint(0, len(letters)-1)
    letter = letters[randomPostion]
    password += letter

for n in range(0, nr_numbers):
    randomPostion = random.randint(0, len(numbers)-1)
    number = numbers[randomPostion]
    password += number

for s in range(0, nr_symbols):
    randomPostion = random.randint(0, len(symbols) - 1)
    symbol = symbols[randomPostion]
    password += symbol

passwordList = [None] * len(password)

for l in password:
    isNone = True 
    while isNone:
        letter = l 
        arrayPostion = random.randint(0, len(password)-1)
        if( passwordList[arrayPostion] == None):
            passwordList[arrayPostion] = letter
            isNone = False 
        
    
print("Original Password: ", password)
print("Random order:", "".join(passwordList))



            


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
