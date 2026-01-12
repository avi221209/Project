'''
Loops
   Ask roll the dice?
   If users enters y
      Generate two random numbers 
      Print them 
   If users enters n 
       prints thank you message
       Terminate
   Else
      print invalid cho   ice       

'''
import random

guesses = 0
while True:
   choice = input("Roll the Dice Y/N:").lower()
   guesses += 1
   if choice == 'y':
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      print(f'{die1}, {die2}')
   
   elif choice == "n":
      print("Thanks")
      break 
   else:
      print('Invalid Choice')

print(guesses)  