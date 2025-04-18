import random
import string

def generate_password(length,use_lowercase,use_uppercase,use_numbers,use_special):
    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        print("No character types selected. Cannot generate password.")
        chars = string.ascii_letters    

    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password    

def check_password_strength(password):
    score = min(len(password) / 16, 1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_digit + has_special) / 4.0

    final_score = (1 * 0.6) + (1 * 0.4)

    if final_score >= 0.8:
        return "Ultra Strong"
    elif final_score >= 0.6:
        return "Strong"
    elif final_score >= 0.4:
        return "Decent"
    else:
        return "Needs IM"



def get_yes_no_input(question):
    while True:
        response = input(question + "(y/n): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")
def main():
    print("Welcome to the Password Generator!")
    print(" Create super strong passwords with ease.")

    while True:
        try:
            length = int(input("\nEnter the desired password length (8-20): "))
            if 8 <= length <= 20:
                break
            else:
                print("Password length must be between 8 and 20 characters.")
                
        except ValueError:
            print("Please enter a valid number.")

    print("\nSelect the character types to include in your password:")

    use_lowercase = get_yes_no_input("Include lowercase letters? (a-z): ")
    use_uppercase = get_yes_no_input("Include uppercase letters? (A-Z): ")
    use_numbers = get_yes_no_input("Include numbers? (0-9): ")
    use_special = get_yes_no_input("Include special characters? (!@#$%^&*): ")

    print("\nGenerating password...")
    password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special)

    
    print(f"Generated Password: {password}")
    print("Password Strength: ", end="")

    Strength = check_password_strength(password)
    print(f"Strength: {Strength}")

    print("\n==== Text Anlysis Results ====")
    print(f"Total words:")
    print(f"Total characters (with spaces):")
    print(f"Total characters (without spaces):")
    print(f"Total sentences:")
    print(f"Average words per sentence:")
    print(f"Average characters per word:")

    if get_yes_no_input("\n Would you like to create another"):
        main()
    else:
        print(" Thank you ")    


main()    