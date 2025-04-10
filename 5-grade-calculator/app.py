print(" Grade Calculator ")
scores = []

while True:
    scores = input(" Enter a test scors (or 'done': )")
    if scores.lower() == 'done':
        print("Goodbye")
        break

    scores.append(float(scores))
    average = sum(scores) / len(scores)
    print(f"Average scorg: {average:.1f}")
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Gradc: C")
    else:
        print("GRade: D or F")    
