import random
import time

def display_welcome():
    print("\n" + "=" * 50)
    print("Welcome to the Quiz Game!")
    print("=" * 50)
    print("\n Instructions:")
    print("1. Choose a category from the list.")
    print("2. Answer the questions by typing the number of your choice.")
    print("3. You will have 10 seconds to answer each question.")
    print("4. At the end of the quiz, your score will be displayed.")
    print("- Have fun and good luck! -")

def display_categories():
    print("\n Quiz Categories:")
    print("1. General Knowledge")
    print("2. Science")
    print("3. History")
    print("4. Geography")
    print("5. Sports")

def get_user_choice():
    while True:
        try:
            choice = input("\nPlease select a category (1-5): ")
            if 1<= choice <= 5:
                return choice
            else:
                print(f"Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the category.")
        
def load_questions():
    general_knowledge = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
            "answer": 3
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["1. Mark Twain", "2. William Shakespeare", "3. Charles Dickens", "4. Jane Austen"],
            "answer": 2
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["1. Earth", "2. Jupiter", "3. Saturn", "4. Mars"],
            "answer": 2
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["1. Au", "2. Ag", "3. Pb", "4. Fe"],
            "answer": 1
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"],
            "answer": 3
        },
    ]
    movies_tv = [
        {
            "question": "Who directed 'Inception'?",
            "options": ["1. Christopher Nolan", "2. Steven Spielberg", "3. Quentin Tarantino", "4. Martin Scorsese"],
            "answer": 1
        },
        {
            "question": "What is the highest-grossing film of all time?",
            "options": ["1. Avatar", "2. Titanic", "3. Star Wars: The Force Awakens", "4. Avengers: Endgame"],
            "answer": 4
        },
        {
            "question": "Who played Jack Dawson in 'Titanic'?",
            "options": ["1. Brad Pitt", "2. Leonardo DiCaprio", "3. Johnny Depp", "4. Tom Cruise"],
            "answer": 2
        },
        {
            "question": "'Breaking Bad' is set in which US state?",
            "options": ["1. California", "2. Texas", "3. New Mexico", "4. Arizona"],
            "answer": 3
        },
        {
            "question": "'Game of Thrones' is based on which book series?",
            "options": ["1. The Lord of the Rings", "2. A Song of Ice and Fire", "3. The Chronicles of Narnia", "4. Harry Potter"],
            "answer": 2
        },
    ]
    science_nature = [
        {
            "question": "What is the chemical formula for water?",
            "options": ["1. H2O", "2. CO2", "3. O2", "4. NaCl"],
            "answer": 1
        },
        {
             "question": "What planet is known as the Red Planet?",
                "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
                "answer": 2
        },
        {
            "question": "What is the speed of light?",
            "options": ["1. 300,000 km/s", "2. 150,000 km/s", "3. 450,000 km/s", "4. 600,000 km/s"],
            "answer": 1
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["1. Nucleus", "2. Mitochondria", "3. Ribosome", "4. Endoplasmic Reticulum"],
            "answer": 2
        },
        {
            "question": "What is the most abundant gas in the Earth's atmosphere?",
            "options": ["1. Oxygen", "2. Nitrogen", "3. Carbon Dioxide", "4. Hydrogen"],
            "answer": 2
            
        },
    ]
    video_games = [
        {
            "question": "What is the best-selling video game of all time?",
            "options": ["1. Minecraft", "2. Tetris", "3. Grand Theft Auto V", "4. Wii Sports"],
            "answer": 1
        },
        {
            "question": "In which game do players compete to be the last one standing on an island?",
            "options": ["1. Fortnite", "2. Call of Duty", "3. PUBG", "4. Apex Legends"],
            "answer": 1
        },
        {
            "question": "What is the name of the main character in 'The Legend of Zelda' series?",
            "options": ["1. Link", "2. Zelda", "3. Ganon", "4. Navi"],
            "answer": 1
        },
        {
            "question": "'Super Mario Bros.' was released in which year?",
            "options": ["1. 1985", "2. 1990", "3. 1995", "4. 2000"],
            "answer": 1
        },
        {
            "question": "'The Last of Us' is set in a post-apocalyptic world caused by what?",
            "options": ["1. Zombies", "2. Aliens", "3. Robots", "4. Fungi"],
            "answer": 4
        },
    ]

    return {
       {"name": "General Knowledge", "questions": general_knowledge},
        {"name": "Movies & TV", "questions": movies_tv},
        {"name": "Science & Nature", "questions": science_nature},
        {"name": "Video Games", "questions": video_games},
        {"name": "Random", "questions": random.sample(general_knowledge + movies_tv + science_nature + video_games, 5)}

    }

def run_quiz(category_data):
    category_name = category_data["name"]
    questions = category_data["questions"]

    random.shuffle(questions)

    print(f"\nStarting the quiz in the '{category_name}' category...\n")
    print("Answer the questions within 10 seconds!")
    score = 0
    correct_answers = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        print(f"? {q["question"]}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("\nYour answer (1-4): ").upper()
            if user_answer not in ["1", "2", "3", "4"]:
                print("Invalid input. Please enter a number between 1 and 4.")
            else:
                break
        correct = user_answer == q["answer"]

        if correct:
            score += 10
            correct_answers += 1
            print(f"Correct! You earned 10 points.")
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.")
        
        if i < len(questions) - 1:
            print("Next question coming up...")
            time.sleep(2)
    print(f"\n" + "=" * 50)
    print(" Quiz Over!".center(50))
    print("=" * 50)
    print(f"Category: {category_name}")
    print(f"Your score: {score} points")
    print(f"Correct answers: {correct_answers}/{len(questions)}")

    percentage = (score / (len(questions) * 10)) * 100

    if percentage == 100:
        print("Perfect score! You're a quiz master!")
    elif percentage >= 80:
        print("Great job! You're a quiz whiz!")
    elif percentage >= 60:
        print("Good effort! You know your stuff!")
    elif percentage >= 40:
        print("Not bad! Keep practicing!")
    else:
        print("Better luck next time! Don't give up!")

    return score                        

def main():
    display_welcome()

    total_score = 0
    play_again = True

    while play_again:
        display_categories()

        category_choice = get_user_choice()

        all_categories = load_questions()
        score = run_quiz(all_categories[category_choice - 1])

        total_score += score

        again = input("\nDo you want to play again? (yes/no): ").lower()

        while not (again in ["yes", "no"]):
            print("Invalid input. Please enter 'yes' or 'no'.")
            again = input("Do you want to play again? (yes/no): ").lower()

        play_again = again.startswith("y")

    print("\nThank you for playing the Quiz Game!")        


    

main()