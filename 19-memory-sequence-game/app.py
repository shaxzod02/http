import random
import time
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

print("\n=== Memory Sequence Game ===\n")
print(" Remember the sequence and type it back")
print("\nRules:")
print("- Watch as numbers appear one by one.")
print("- After the sequence is shown, type the numbers in order.")
print("- Each round adds one more number to remember.")
print("- How far can you go?\n")

input("Press Enter to start the game...")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))  # Add a new random number to the sequence
    clear_screen()
    print(f"\nRound", {current_round})
    print("Remember this sequence of {len(sequence)} numbers:")

    for number in sequence:
        time.sleep(0.5)  # Pause for half a second
        print(f"\n{number}")
        time.sleep(0.7)
        clear_screen()

    print("\n Now type the sequence back:")
    player_answer = input("Your answer: ")


    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        game_over = True
        continue    

    if player_sequence == sequence:
        print("\nCorrect! Moving to the next {len(sequence)} numbers...")
        current_round += 1
        time.sleep(2)
    else:
        print("\nWrong! Game Over.")
        print(f"The correct sequence was: {' '.join(map(str, sequence))}")

    if game_over:
        player_again = input("Do you want to play again? (y/n): ").lower()
        if player_again.startswith('y'):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing!")
                   