import random
import time


def chatbot():
    greetings = [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",]
    farewells = [
        "Goodbye! Have a great day!",
        "See you later! Take care!",]
    
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call fake spaghetti? An impasta!",]
    
    facts = [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
        "Did you know? Bananas are berries, but strawberries aren't!",
        "Did you know? A group of flamingos is called a 'flamboyance'!",
        "Did you know? Octopuses have three hearts!"]
    
    bot_name = "Chatbot"
    print(f"{bot_name} is starting up...")
    time.sleep(1)

    print(f"""
          Welcome to {bot_name} 
          I can chat about:
          1. 'Jokes'
          2. 'Facts'
          3. 'color'
          4. 'bye
          """)
    
    chatting = True
    user_name = input("What is your name? ").lower()
    print(f"Hello {user_name.capitalize()}! I'm {bot_name}.")

    while chatting:
        user_input = input( "You: ").strip()

        if user_input in ["hi", "hello", "hey"]:
            print(f"{bot_name}: {random.choice(greetings)}")
        elif "joke" in user_input:
            print(f"{bot_name}: {random.choice(jokes)}")
        elif "fact" in user_input:
            print(f"{bot_name}: {random.choice(facts)}")
        elif "color" in user_input:
            print(f"{bot_name}: My favorite color is blue! What's yours?")
            color_input = input("You: ").strip()
            print(f"{bot_name}: {color_input} is a nice color!")
        elif user_input in ["bye", "exit", "quit"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"{bot_name} is shutting down...")
            chatting = False    

        else:
            response = [
                "That's interesting! Tell me more.",
                "I see! What else would you like to share?",
                "Hmm, that's a thought-provoking statement.",
                "Beep boop! I'm a chatbot, not a mind reader!",   
            ]
            print(f"{bot_name}: {random.choice(response)}")

    print("Thank you for chatting with me!")            
    
    
chatbot()    
