 

def count_words(text):
    words = text.split()
    return len(words) 

def count_characters(text,include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace("", ""))
    

def count_sentences(text):
    sentence_endings = ["." "," ","]
    count = 0

    for char in text:
        if char in sentence_endings:
            count +=1

    if count == 0 and text.strip():
        count = 1        

    return count        
   



def analyze_text(text):
    
    word_count = count_words(text)
    char_count_with_spaces = count_characters(text,True)
    char_count_without_spaces = count_characters(text,False)
    sentence_count = count_sentences(text)

    if sentence_count > 0:
        words_per_sentence = word_count / sentence_count
    else:
        words_per_sentence = 0

    if word_count > 0:
        chars_per_word = char_count_with_spaces / word_count
    else:
        chars_per_word = 0

    print("\n==== Text Anlysis Results ====")
    print(f"Total words: {word_count}")
    print(f"Total characters (with spaces): {char_count_with_spaces}")
    print(f"Total characters (without spaces): {char_count_without_spaces}")
    print(f"Total sentences: {sentence_count}")
    print(f"Average words per sentence: {words_per_sentence:.1f}")
    print(f"Average characters per word: {chars_per_word:.1f}")

    reading_time_minutes = word_count / 225
    if reading_time_minutes < 1:
        reading_time_seconds = reading_time_minutes * 60
        print(f"Estimated reading time: {reading_time_seconds:.0f} seconds")
    else:
        print(f"Estimated reading time: {reading_time_minutes:.1f} minutes")

def main():
    print("\n=== Word Counter ===")
    print("1. Count words")

    while True:
        print("\n choose an option:")
        print("1. Enter text")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            print("\nEnter the text to analyze:")
            lines = []

            while True:
                line = input()
                if line and not lines[-1]:
                    break
                lines.append(line)
            text = "\n".join(lines)

            if not text.strip():
                print("No text entered. Please try again.")
                continue
            analyze_text(text)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice Please enter 1 or 2.")

main()             