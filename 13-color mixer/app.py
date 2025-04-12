print(" Color mixer")

color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}

while  True:
    color1 = input("\nEnter first color: ").lower()
    color2 = input("Enter second color: ").lower()

    mix = None

    if (color1,color2) in color_mixes:
        mix = color_mixes[(color1,color2)]


    if mix:
        print(f"When ypu mix {color1} and {color2}, you get {mix}!")
    else:
        print("I don't know what those colors make when mixed.")

    if not input("\nMix more colors? (y/n)").lower().startswith("y"):
        print("Goodbye")
        break            