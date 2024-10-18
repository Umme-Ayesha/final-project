import json
from datetime import datetime

class Task:
    def __init__(self, title, description, category, completed=False, created_at=None):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed,
            'created_at': self.created_at
        }

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description (e.g., 'Do Mathematics homework'): ")
    category = input("Enter task category (e.g., 'School'): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task.completed else "Pending"
        print(f"{i}. [{status}] {task.title} ({task.category})")
        print(f"   Description: {task.description}")
        print(f"   Created: {task.created_at}")
        print()

def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to edit: ")) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            print(f"\nEditing task: {task.title}")
            task.title = input(f"Enter new title (or press Enter to keep '{task.title}'): ") or task.title
            task.description = input(f"Enter new description (or press Enter to keep '{task.description}'): ") or task.description
            task.category = input(f"Enter new category (or press Enter to keep '{task.category}'): ") or task.category
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== Personal To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
