print(" Reverse name Generator ")

while True:
    name = input("\nEnter a name: ")

    reversed_name = name[::-1]
    print(f"Your reversed name is: {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name.title()}")

    answer = input("\nTry another name? (y/n): ")
    if answer != "y":
        break