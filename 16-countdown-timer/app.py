import time

print("\n=== Countdown time ===")
print(" Count down from your chosen seconds")

while True:
 try:  
    seconds = int(input("\n Enter seconds to countdown from: "))

    if seconds <= 0:
        print(" please")
        continue

    print(f" Staring countdown from {seconds} seconds")

    for i in range(seconds,0-1):
        print(f"{i} seconds remaining...")
        time.sleep(1)

    print("\n Countdown Complete")

    again = input("\n Start another countdown? (yes/no):").lower()
    if not again.startswith("y"):
        print("Goodbye")
        break    
 except ValueError:
    print("plese")
