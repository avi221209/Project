import random

player_score = 0
computer_score = 0

while player_score < 100 and computer_score < 100:
    # Player turn
    turn_score = 0
    print("\nYour turn")

    while True:
        choice = input("Roll or Hold? (r/h): ").lower()
        if choice == 'r':
            roll = random.randint(1, 6)
            print("You rolled:", roll)

            if roll == 1:
                turn_score = 0
                print("Turn over!")
                break
            else:
                turn_score += roll
                print("Turn score:", turn_score)
        else:
            player_score += turn_score
            break

    print("Your total score:", player_score)

    # Computer turn
    turn_score = 0
    print("\nComputer turn")

    while turn_score < 20:
        roll = random.randint(1, 6)
        print("Computer rolled:", roll)

        if roll == 1:
            turn_score = 0
            break
        else:
            turn_score += roll

    computer_score += turn_score
    print("Computer score:", computer_score)

if player_score >= 100:
    print("\n🎉 You win!")
else:
    print("\n🤖 Computer wins!")
