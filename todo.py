tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(i, task)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
elif choice == "4":
    num = int(input("Enter task number to delete: "))
    tasks.pop(num - 1)   # No validation → BUG
