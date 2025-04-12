import random

print(" Cion Flip Game ")
print("Guess heads or tails ")

while True:
    guess = input("\nEnter your guess (heads/taila): ").lower()

    if guess != "heads" and guess != "tails":
        print(" Please enter 'heads" or 'tails')
        continue

    flip = random.choice(["heads", "tails"])

    print(f"\nCoin shows {flip}")

    if guess == flip:
        print(" You won! You guessed correctly. ")
    else:
        print(" Sorry, wrong Guess. Try again! ") 

    again = input("\n Play again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye")
        break       