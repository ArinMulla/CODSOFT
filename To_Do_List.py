tasks = []

def show_menu():
    print("Todo List Menu:")
    print("1. Add your Task")
    print("2. View your Tasks")
    print("3. Remove Task")
    print("4. Exit:)")

def add_task():
    task = input("Enter your task plz: \n")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the Todo List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
