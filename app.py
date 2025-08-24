# Add tasks
# Delete Tasks
# Mark tasks as complete or pending

# Step 1

tasks = []

def display_menu():
    print("\n---------To-Do List Menu---------\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Remove Task")
    print("5. Quit")

def add_task():
    task_name = input("Enter Task Name: ")
    tasks.append({'task_name': task_name, "status": "Pending"})
    print(f"Task '{task_name}' has been added as pending")

def view_tasks():
    if not tasks:
        print("No tasks available.")

    else:
        print("\n--------------All Tasks-------------")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task_name']} - {task['status']}")

def mark_task_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number -1 ]["status"] = "Completed"
            print(f"Task '{tasks[task_number -1]['task_name']}' has been marked as completed")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1) #REmove the task
            print(f"Task '{removed_task['task_name']} has been removed.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("exiting the Task Manager"
                  "\n..............................."
                  "\nGoodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice (1-5).")

if __name__ == "__main__":
    main()