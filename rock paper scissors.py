import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def main():
    user_score = 0
    computer_score = 0

    print("=== Welcome to Rock-Paper-Scissors Game ===\n")
    
    while True:
        print("\nChoose: rock, paper, or scissors (or type 'exit' to quit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nCurrent Scores -> You: {user_score} | Computer: {computer_score}")

# Run the game
if __name__ == "__main__":
    main()
