import random
import time

word_pairs = {
    "sky": ["blue", "cloud", "sun"],
    "water": ["drink", "flow", "ocean"],
    "food": ["eat", "meal", "snack"],
    "music": ["song", "dance", "beat"],
    "book": ["read", "story", "library"],
    "tree": ["leaf", "wood", "forest"],
    "car": ["drive", "road", "engine"],
    "dog": ["bark", "pet", "tail"],
}

print("\n=== Word Association Game ===")
print(" Respond with a word related to the given word.")

score = 0
rounds = 5

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]

    print(f"\n Prompt: {prompt.upper()}")
    print(" Type 'exit' to quit the game.")

    start_time = time.time()
    response = input(">").lower().split()
    response_time = time.time() - start_time

    print("response:", response_time)

    if response in related_words:
        points = max(1, 5 - int(response_time))
        score += points
        print(f" Correct! You earned {points} points.")
    else:
        print(" Incorrect! No points earned.")
        print(f" Related words were: {', '.join(related_words)}")

    rounds += 1
    print(f" Your current score is: {score} points.")
    if input("\n Play again? (y/n): ").lower() != 'y':
        print(" Thanks for playing!")
        break