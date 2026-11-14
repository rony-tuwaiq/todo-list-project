
tasks = []


def add_task(task):
    if not task.strip():
        print("Task cannot be empty!")
        return
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def delete_task(number):
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            try:
                number = int(input("Enter task number: "))
                delete_task(number)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
