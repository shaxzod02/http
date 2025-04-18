import time
import os
import platform

def clear_screen():
    """Clear the console screen based on the operating system."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def format_time(seconds):
    """Format time in seconds to MM:SS format."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def countdown(seconds,label):
    for remaining in range(seconds, 0, -1):
        clear_screen()
        print(f"{label}")
        print(f" Time remaining: {format_time(remaining)}")

        if label == "Work":
            print("Focus on your task!")
        elif label == "Short Break":
            print("Take a short break!")

        time.sleep(1)

    clear_screen()
    print(f"{label} time is up!")

    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500) 

    else:
        print("\a")  # This may not work on all systems
def pomodoro_timer():
    clear_screen()
    print("Pomodoro Timer")

    work_minutes = 25 
    short_break_minutes = 5
    long_break_minutes = 15
    cycles = 4

    customize = input("\n Use default settings (25min work, 5min short break, 15min long break)? (y/n): ").lower()

    if customize != 'yes' and customize != 'y':
        try:
            work_minutes = int(input("Enter work duration in minutes: "))
            short_break_minutes = int(input("Enter short break duration in minutes: "))
            long_break_minutes = int(input("Enter long break duration in minutes: "))
            cycles = int(input("Enter number of cycles before long break: "))
        except ValueError:
            print("Invalid input. Using default settings.")
            time.sleep(2)

    clear_screen()
    print("Pomodoro Timer")
    print(f"Work: {work_minutes} min, Short Break:")
    print(f"{short_break_minutes} min, Long Break:")
    print(f"{long_break_minutes} min, Cycles: {cycles}")
    print(" Press Ctrl+C to stop the timer.")
    input("Press Enter to start...")

    work_seconds = work_minutes * 60
    short_break_seconds = short_break_minutes * 60
    long_break_seconds = long_break_minutes * 60
    
    cpmplete_cycles = 0

    while True:
        countdown(work_seconds, "Work")
        cpmplete_cycles += 1

        if cpmplete_cycles % cycles == 0:
            input("\nTime for a long break! Press Enter to continue...")
            countdown(long_break_seconds, "Long Break")
            input("\nLong break over! Press Enter to continue...")
        else:
            input("\nTime for a short break! Press Enter to continue...")
            countdown(short_break_seconds, "Short Break")
            input("\nShort break over! Press Enter to continue...")    


pomodoro_timer()