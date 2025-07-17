import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        status = "Done" if task['done'] else "Not Done"
        print(f"{idx + 1}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        tasks[task_num]['done'] = True
        print("Task marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        tasks.pop(task_num)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def edit_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to edit: ")) - 1
        new_task = input("Enter new task description: ")
        tasks[task_num]['task'] = new_task
        print("Task updated!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
