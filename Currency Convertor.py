n = float(input("Enter a Amount : "))

choice = ('USD','EUR','CAD')

user_choice = input("Source Currency (USD/EUR/CAD): ").upper()
if user_choice not in choice:
    print("Invalid Choice")
    exit()

user_choices1 = input("Target Currency (USD/EUR/CAD): ").upper()
if user_choices1 not in choice:
    print("Invalid Traget Currency")
    exit()

if "USD" == user_choice:
    if "EUR" == user_choices1:
        eur = n * .92
        print("Converted Amount:", eur)

if "USD" == user_choice:
    if "CAD" == user_choices1:
        cad = n * 1.35 
        print("Converted Amount:", cad)

if "EUR" == user_choice:
    if "USD" == user_choices1:
        usd = n * 1.09
        print("Converted Amount:", usd)

if "EUR" == user_choice:
    if "CAD" == user_choices1:
        cad = n * 1.47
        print("Converted Amount:", cad)

if "CAD" == user_choice:
    if "USD" == user_choices1:
        usd = n * 0.74
        print("Converted Amount:", usd)
        
if "CAD" == user_choice:
    if "EUR" == user_choices1:
        eur = n * 0.68   
        print("Converted Amount:", eur)