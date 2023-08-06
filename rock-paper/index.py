import random

def print_option():
    print("welcome to rock paper and sessior game")
    print("options:")
    print("1. Rock")
    print("2. Paper")
    print("3. sessior")


def get_user_choice():
    choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
    while choice<1 or choice>3:
        print("enter a valid choice")
        choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))

    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "user"
    else:
        return "computer"
    

# ... (previous code)

user_wins = 0
computer_wins = 0
draws = 0

# ... (previous code)

while True:
    print_option()
    user_choice = get_user_choice()

    computer_choice = random.randint(1, 3)
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "user":
        print("You win!")
        user_wins += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a draw!")
        draws += 1
    
    print(f"Score: User {user_wins} - Computer {computer_wins} - Draws {draws}")

    play_again = input("Do you want to play another round? (yes/no): ")
    while play_again.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play another round? (yes/no): ")
    
    if play_again.lower() == "no":
        print("Thanks for playing! Goodbye.")
        break
