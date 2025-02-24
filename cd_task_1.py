tasks = []

# Main loop
while True:
    # Display menu options
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Display Tasks")
    print("6. Quit")

    # Get user input
    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    # Update task
    elif choice == "2":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            task_index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            tasks[task_index] = new_task
            print(f"Task '{new_task}' updated successfully!")
        else:
            print("No tasks available to update.")

    # Delete task
    elif choice == "3":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            task_index = int(input("Enter task number to delete: ")) - 1
            del tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("No tasks available to delete.")

    # Mark task as completed
    elif choice == "4":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            tasks[task_index] = f"[Completed] {tasks[task_index]}"
            print("Task marked as completed!")
        else:
            print("No tasks available to mark as completed.")

    # Display tasks
    elif choice == "5":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
        else:
            print("No tasks available.")

    # Quit
    elif choice == "6":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")


