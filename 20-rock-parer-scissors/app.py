import random
import time

def display_welcome():
    print("\n==== Rock, Paper, Scissors ====")
    print("You will play ")
    print("\n Rules:")
    print("- Rock crushes Scissors")
    print("- Scissors cuts Paper")
    print("- Paper covers Rock")
    print("\n The first to reach 3 points wins the game!")
    print("\n Good luck!")

def display_welcome():
    pass
def get_user_choice():
    while True:
        print("\nMake your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue 

def get_computer_choice():
    return random.randint(1, 3)

def convert_choice_to_text(choice):
    options = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    return options[choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif ((user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2)):
        return "user"
    else:
        return 'computer'
    

def display_round_result(user_choice, computer_choice, result):
    user_text = convert_choice_to_text(user_choice)
    computer_text = convert_choice_to_text(computer_choice)
    print(f"\nYou chose: {user_text}")
    print(f"Computer is chose:")
    for i in range(3):
        print("...")
        time.sleep(0.5)

    print(f"Computer chose: {computer_text}")

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")        
    


def play_game():
    display_welcome()

    user_score = 0
    computer_score = 0
    target_score = 3
    round_num = 1
    

    while user_score < target_score and computer_score < target_score:
        print(f"\n===Round {round_num}===")
        print(f"Score: You {user_score} - Computer {computer_score}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_round_result(user_choice, computer_choice, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        round_num += 1 

    print("\n=== Game Over ===")
    print(f"Final Score: You {user_score} - Computer {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the champion!")
    else:
        print("Computer is the champion this time!")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again.startswith('y'):
        play_game
    else:
        print("Thanks for playing! Goodbye!")                


play_game()
