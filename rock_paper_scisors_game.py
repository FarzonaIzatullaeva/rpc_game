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

user_choice_to_conditions = {
    'r': rock_conditions,
    'p': paper_conditions,
    's': scissors_conditions
}

while True:
    random_number = random.randint(1, 3)
    computer_choice_index = random_number-1
    computer_choice = options[computer_choice_index]
    print("Rock, paper, scissors? (r/p/s): ")
    user_choice = input().lower().strip()

    if (user_choice not in ('r', 'p', 's')):
        print("Invalid choice!")
        continue

    decision = user_choice_to_conditions[user_choice][computer_choice_index]
    print(f"Computer chose {computer_choice}")
    print(index_decision[decision])

    print("Continue? (y/n): ")
    continue_game = input().lower()
    if (continue_game == 'n'):
        break
