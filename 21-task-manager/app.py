tasks = []


def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")
    print("=====================")


def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added.")


def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n=== my Tasks ===:")
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. {task['title']} [{status}]")

    print("=====================\n")


def complete_task():
    view_tasks()

    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to complete: ")) 
        if 0 <= task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        
        task_to_complete = tasks[task_number - 1]
        task_to_complete["completed"] = True
        print(f"Task '{task_to_complete['title']}' completed.")
    except ValueError:
        print("Invalid input. Please enter a number.")
           


def delete_task():
    view_tasks()

    if not tasks:
        return
    try:
        task_number = int(input('Enter task number to delete: '))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        

   

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '0':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")