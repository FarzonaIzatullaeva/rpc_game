import random
options = ['rock', 'paper', 'scissors']
'''
rock -> rock = tie
     -> paper = 2
     -> scissors = 1
    [0, 2, 1]

paper -> rock = 1
      -> paper = tie
      -> scissors = 2
    [1, 0, 2]

scissors -> rock = 2
         -> paper = 1
         -> scissors = tie
    [2, 1, 0]
'''
rock_conditions = [0, 2, 1]
paper_conditions = [1, 0, 2]
scissors_conditions = [2, 1, 0]

index_decision = {
    0: "Tie",
    1: 'User Wins',
    2: "Computer Wins"
}


while True:
    random_number = random.randint(1, 3)
    computer_choice_index = random_number-1
    computer_choice = options[computer_choice_index]
    print("Rock, paper, scissors? (r/p/s): ")
    user_choice = input().lower().strip()

    if (user_choice not in ('r', 'p', 's')):
        print("Invalid choice!")

    else:

        if (user_choice == 'r'):
            decision = rock_conditions[computer_choice_index]
            if (decision == 0):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 1):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 2):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
        elif (user_choice == 'p'):
            decision = paper_conditions[computer_choice_index]
            if (decision == 0):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 1):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 2):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
        elif (user_choice == 's'):
            decision = scissors_conditions[computer_choice_index]
            if (decision == 0):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 1):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
            elif (decision == 2):
                print(f"Computer chose {computer_choice}")
                value = index_decision[decision]
                print(value)

                print("Continue? (y/n): ")
                continue_game = input().lower()
                if (continue_game == 'n'):
                    break
