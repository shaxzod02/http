import random
print(" Word Scrambler ")

while True:
    word = input("\n Enter a word to scrambl (or 'quit'):")
    if word.lower() == "quit":
        print(" Goodbye")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")
