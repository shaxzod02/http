def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("\nEnter choice (1-4): ")
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        else:
            break
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if choice == '1':
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")  

    again = input("\nDo you want to perform another calculation? (yes/no): ")
    if not again.startswith('y'):
        print("Goodbye!")
        return
    else:
        main()            


        