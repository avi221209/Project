import random 
n = random.randint(1,100)
a = 0 

guesses = 0
while(a != n):
    a = int(input("Guess the number:"))
    guesses +=1
    
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
        
    
print(f"You have guessed the number {n} correctly in {guesses} attempt")
