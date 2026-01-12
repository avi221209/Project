def quiz():
   score = 0

   print("Question 1: What us the Capital of France ? ")
   print("a) Paris")
   print("b) London")
   print("c) Rome")
   answer1 = input("Your answer: ").lower()

   if  answer1 == "a":
      print("Correct Answer!")
      score+=1  
   else:
      print("Incorrect Answer!")

   print("What is the largest planet in our solar system? ")
   print("a) Earth")
   print("b) Jupiter")
   print("c) Mars")
   answer2 = input("Your answer: ").lower()

   if  answer2 =="b":
      print("Correct Answer!")
      score+=1
   else:
      print("Incorrect Answer!")

   print(f"Your final Score: {score}/2")  

quiz()