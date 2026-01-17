import random 
import string 

length = int (input("Enter Password Length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower()
use_digits = input("Include Numbers? (y/n): ").lower()
use_special = input("Include Special Characters? (y/n): ").lower()

characters = string.ascii_lowercase

if use_upper == "y":
    characters += string.ascii_lowercase #Here this contain "abcdefghijklmnopqrstuvwxyz"
    # characters = characters + string.ascii_lowercase

if use_upper == "y":
    characters += string.digits #Here digits are "0123456789"
  # characters = characters + string.digits

if use_upper == "y":
    characters += string.punctuation #here punctuation are "!@#$%^&*()_+-=[]{}|;:,.<>?"
  # characters = characters + string.punctuation

password =" "
for i in range(length):
    password += random.choice(characters)
    
# Here we take random.choice(charaters) bcoz we can get passwprd's all characters randomly  

print("Generated Passowrd",password)    


# More about String Library https://docs.python.org/3/library/string.html