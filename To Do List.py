#To Do List
import os
import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """View existing tasks with their completion status."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = 'Done' if task['done'] else 'Not Done'
        print(f"{index + 1}. {task['task']} - {status}")
    print()

def add_task(tasks):
    """Add new task to the list."""
    task = input("Enter the new task: ")
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!\n")

def mark_task(tasks, done=True):
    """Mark a task as done or undone."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to mark: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError
        tasks[task_index]['done'] = done
        save_tasks(tasks)
        status = 'done' if done else 'undone'
        print(f"Task '{tasks[task_index]['task']}' marked as {status}.\n")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.\n")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed successfully!\n")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.\n")

def display_menu():
    """Display the menu for the to-do list application."""
    print("To-Do List 📝")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Mark Task as Undone")
    print("5. Remove Task")
    print("6. Exit")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks, done=True)
        elif choice == '4':
            mark_task(tasks, done=False)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

