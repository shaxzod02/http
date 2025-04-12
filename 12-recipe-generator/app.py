import random

print("Random recipe genrator")

proteins = ["chichken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell"]
carbs = ["rice", "pasta"]
methods = ["baked", "grilled"]
flavors = ["garlic", "lemon", "spicy"]


while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(f"\n Your random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another one? (y/n): ").lower().startswith("y"):
        print(" Goodbye")
        break
