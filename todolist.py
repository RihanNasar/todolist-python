tasks = []

def main():
    print("Welcome to the To-Do List App!")
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_completed()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            save_and_exit()
            break
        else:
            print("Invalid choice!")
def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Save and Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")

def view_tasks():
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['task']}")

def save_and_exit():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")
    print("Tasks saved. Goodbye!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append({"task": task, "completed": completed == "True"})
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    load_tasks()
    main()
