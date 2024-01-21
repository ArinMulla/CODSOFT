import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == 'Rock' and computer_choice == 'Scissors') or \
       (player_choice == 'Paper' and computer_choice == 'Rock') or \
       (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return "Congrats You Win !"
    else:
        return "uppps...Computer wins!"

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']

    while True:
        print("Enter your choice Plz: rock, paper, or scissors (or 'exit' to quit)")
        player_choice = input().lower()

        if player_choice == 'exit':
            print("Exiting the game.")
            break

        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

rock_paper_scissors()
