import time
import random

player = {
    "name": "",
    "health": 100,
    "gold": 50,
    "items": [],
}

locations = {
    "town": {
        "description": "A bustling town with shops and an inn.",
        "options": {
            "shop": "Visit the shop.",
            "inn": "Rest at the inn.",
            "forest": "Go to the forest.",
        },
    },
    "forest": {
        "description": "A dark and eerie forest.",
        "options": {
            "explore": "Explore the forest.",
            "town": "Return to town.",
        },
    },
    "shop": {
        "description": "A shop filled with various items.",
        "options": {
            "buy": "Buy an item.",
            "sell": "Sell an item.",
            "town": "Return to town.",
        },
    },
}

items = {
    "health potion": {"health": 30, "price": 10},
    "golden apple": {"health": 50, "price": 20},

}

enemies = {
    {"name": "Goblin", "health": 30, "damage": 10},
    {"name": "Wolf", "health": 40, "damage": 15},
    {"name": "Bandit", "health": 50, "damage": 20},
}


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def display_stats():
    print("\n" + "=" * 40)
    print(f"Name: {player['name']} | Health: {player['health']} | Gold: {player['gold']}")

    if player["items"]:
        print("Items: " + ", ".join(player["items"]))

    print("=" * 40)    


def town():
    slow_print("\n You are in the town.")
    slow_print(locations["town"]["description"])

    while True:
        display_stats()
        slow_print("\nWhat would you like to do?")
        print("1. Go to the shop")
        print("2. Rest at the inn")
        print("3. Go to the forest")
        print("4. Exit game")

        choice = input("Enter your choice (1-4): ")

        if choice == "1" or "shop" in choice:
            shop()
        elif choice == "2" or "forest" in choice:
            forest()
        elif choice == "3" or "rest" in choice:
            rest()
        elif choice == "4" or "quit" in choice:
            slow_print("Thank you for playing! Goodbye!")
            exit()
        else:
            print(" I didn't understand that. Please try again.")

def shop():
    slow_print("\n You are in the shop.")
    slow_print(locations["shop"]["description"])

    while True:
        display_stats()
        print("\nWhat would you like to do?")
        print("1. Buy an item")
        print("2. Sell an item")
        print("3. Return to town")
        choice = input(">").lower()

        if choice == "1" or "health" in choice:
            buy_item("health potion")
        elif choice == "2" or "sword" in choice:
            buy_item("sword")
        elif choice == "3" or "return" in choice or "town" in choice:
            slow_print("Returning to town...")
            return
        else:
            print(" I didn't understand that. Please try again.")

def buy_item(item_name):
    item = items(item_name)

    if item_name in player["items"] and item_name != "health potion":
        slow_print(f"You already have a {item_name}.")
        return
    if player["gold"] >= item["price"]:
        player["gold"] -= item["price"]

        if item_name not in player["items"]:
            player["items"].append(item_name)
            
        if "health" in item:
            slow_print(f"You bought a {item_name} for {item['price']} gold.")
        elif "damage" in item:
            slow_print(f"You bought a {item_name} for {item['price']} gold.")
    else:
        slow_print(f"You don't have enough gold to buy a {item_name}.")
        

def forest():
    slow_print("\n You are in the forest")
    slow_print(locations["forest"]["description"])

    while True:
        display_stats()
        print("\nWhat would you like to do?")
        print("1. Explore the forest")
        print("2. Return to town")
        print("3. Exit game")

        choice = input(">").lower()

        if choice == "1" or "explore" in choice:
            explore()
        elif choice == "2" or "return" in choice or "town" in choice:
            slow_print("Returning to town...")
            return
        elif choice == "3" or "exit" in choice:
            slow_print("Thank you for playing! Goodbye!")
            player["health"] = min(player["health"] + 10, 100)
            slow_print("You have rested and regained some health.")
        else:
            print(" I didn't understand that. Please try again.")    

def explore():
    slow_print("\n You are exploring the forest")
    time.sleep(1)

    encounter = random.choice(["enemy", "treasure", "nothing"], [60, 30, 10])[0]

    if encounter == "enemy":
        enemy_encounter()
    elif encounter == "treasure":
        treasure_encounter()
    else:
        slow_print("You found nothing of ")


def enemy_encounter():
    enemy = random.choice(enemies)
    enemy_health = enemy["health"]

    slow_print(f"A wild {enemy['name']} appears! It has {enemy_health} health.")
    while enemy_health > 0 and player["health"] > 0:
        display_stats()
        slow_print(f"\nYour health: {player['health']} | Enemy health: {enemy_health}")
        print("1. Attack")
        print("2. Use item")
        print("3. Run away")

        choice = input(">").lower()

        if choice == "1" or "attack" in choice:
            player_damage = 5
            if "sword" in player["items"]:
                player_damage += items["sword"]["damage"]
            enemy_health -= player_damage
            slow_print(f"You attacked the {enemy['name']} for {player_damage} damage.")

            if enemy_health <= 0:
                slow_print(f"You defeated the {enemy['name']}!")
                player["gold"] += enemy["gold"]
                slow_print(f"You found {enemy['gold']} gold.")
                return
            
            player["health"] -= enemy["damage"]
            slow_print(f"The {enemy['name']} attacked you for {enemy['damage']} damage.")

            if player["health"] <= 0:
                game_over()

        elif choice == "2" or "use" in choice:
            if "health potion" in player["items"]:
                player["health"] += items["health potion"]["health"]
                player["items"].remove("health potion")
                slow_print("You used a health potion and regained some health.")
            else:
                slow_print("You don't have any items to use.")
                continue

            player["health"] -= enemy["damage"]
            slow_print(f"The {enemy['name']} attacked you for {enemy['damage']} damage.")
            if player["health"] <= 0:
                game_over()
        elif choice == "3" or "run" in choice:
            if random.random() < 0.5:
                slow_print("You successfully ran away!")
                return
            else:
                slow_print("You couldn't escape!")
                player["health"] -= enemy["damage"]
                slow_print(f"The {enemy['name']} attacked you for {enemy['damage']} damage.")
                if player["health"] <= 0:
                    game_over()
        else:
            print(" I didn't understand that. Please try again.")        

def treasure_encounter():
    gold_found = random.randint(10, 50)
    player["gold"] += gold_found

    if random.random() < 0.2 and "health potion" not in player["items"]:
        player["items"].append("health potion")
        slow_print(f"You found a health potion and {gold_found} gold!")
    else:
        slow_print(f"You found {gold_found} gold!")
        slow_print("You found nothing of interest.")

def rest():
    if player["gold"] >= 10:
        player["gold"] -= 10
        player["health"] = 100
        slow_print("You rested at the inn and regained your health.")
        slow_print("You have rested and regained some health.")

def game_over():
    slow_print("\n Your health has dropped to 0.")
    slow_print("Game Over! You have lost the game.")
    print(f"\n Final stats: {player['gold']} gold collected.")

    player_again = input("Would you like to play again? (yes/no): ").lower()

    if player_again.startswith("y"):
        start_game()
    else:
        slow_print("Thank you for playing! Goodbye!")
        exit()

def start_game():
    player["health"] = 100
    player["gold"] = 50
    player["items"] = []
    
    slow_print("\n" + "=" * 60)
    slow_print("Welcome to the Adventure Game!")
    slow_print("=" * 60 + "\n")
    slow_print("Welcome, brave adventurer! What is your name?")
    player["name"] = input("Enter your name: ")
    slow_print(f"Hello, {player['name']}! Your adventure begins now.")

    town()

start_game()