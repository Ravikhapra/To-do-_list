class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        """Add a new task to the list"""
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added successfully.")
        else:
            print(f"Task '{task_name}' already exists.")

    def remove_task(self, task_name):
        """Remove a task from the list"""
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully.")
        else:
            print(f"Task '{task_name}' not found.")

    def mark_completed(self, task_name):
        """Mark a task as completed"""
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")

    def display_tasks(self):
        """Display all tasks in the list"""
        print("To-Do List:")
        for task, completed in self.tasks.items():
            status = "Completed" if completed else "Not Completed"
            print(f"{task}: {status}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            todo_list.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            todo_list.mark_completed(task_name)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()