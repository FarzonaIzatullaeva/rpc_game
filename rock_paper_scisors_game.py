import random
options = ['rock', 'paper', 'scissors']

while True:
    random_number = random.randint(1, 3)
    computer_choice = options[random_number-1]

    print("Rock, paper, scissors? (r/p/s): ")
    user_choice = input().lower().strip()

    if (user_choice not in ('r', 'p', 's')):
        print("Invalid choice!")

    else:
        if (user_choice == 'r'):
            if (computer_choice == 'rock'):
                print(f"Computer chose {computer_choice}")
                print("Tie!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'paper'):
                print(f"Computer chose {computer_choice}")
                print("Computer Wins!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'scissors'):
                print(f"Computer chose {computer_choice}")
                print("You Win!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
        elif (user_choice == 'p'):
            if (computer_choice == 'paper'):
                print(f"Computer chose {computer_choice}")
                print("Tie!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'scissors'):
                print(f"Computer chose {computer_choice}")
                print("Computer Wins!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'rock'):
                print(f"Computer chose {computer_choice}")
                print("You Win!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
        elif (user_choice == 's'):
            if (computer_choice == 'scissors'):
                print(f"Computer chose {computer_choice}")
                print("Tie!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'rock'):
                print(f"Computer chose {computer_choice}")
                print("Computer Wins!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (computer_choice == 'paper'):
                print(f"Computer chose {computer_choice}")
                print("You Win!")
                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
