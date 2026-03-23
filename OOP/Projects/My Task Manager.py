from datetime import datetime


class Task:
    def __init__(self, id, name, description="", priority="Low", due_date=None, status="pending"):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority.capitalize()
        self.due_date = due_date  
        self.status = status

    def mark_complete(self):
        self.status = "completed"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No date"
        return f"[{self.id} {self.name} | {self.priority} | {due} | {self.status}]"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        self.tasks.append(task)
        self.next_id += 1

    def list_tasks(self, status=None, priority=None):
        tasks = self.tasks
        if status:
            tasks = [t for t in tasks if t.status.lower() == status.lower()]
        if priority:
            tasks = [t for t in tasks if t.priority.lower() == priority.lower()]
        return tasks
    
    def update_task(self, task_id, **kwargs):
        task = self.find_task(task_id)
        if task:
            task.update(**kwargs)
            return True
        return False

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False
    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def find_task(self, task_id):
        return next(task for task in self.tasks if task.id == task_id)

def run_cli():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Task name: ")
            description = input("Description (optional): ")
            priority = input("Priority (Low/Medium/High): ").capitalize()
            due_input = input("Due date (YYYY-MM-DD) or leave blank: ")
            due_date = None
            if due_date:
                try:
                    due_date = datetime.strptime(due_input, "%Y-%m-%d")
                except ValueError:
                    print("Invaild date format. Skipping due date.")
            
            task = Task(manager.next_id, name, description, priority, due_date)
            manager.add_task(task)
            print("Task added!")

        elif choice == "2":
            status_filter = input("Filter by status (pending/completed or leave blank): ")
            priority_filter = input("Filter by priority (Low/Medium/High or leave blank): ")
            tasks = manager.list_tasks(status_filter or None, priority_filter or None)
            if tasks:
                print("\nTasks:")
                for t in tasks:
                    print(t)
            else:
                print("No tasks found")

        elif choice == "3":
            try:
                task_id = int(input("Task ID to update: "))
            except ValueError:
                print("Invaild ID")
                continue
            
            task = manager.find_task(task_id)
            if not task:
                print("Task not found")
                continue
                
            name = input(f"New name (leave blank to keep '{task.name}'): ")
            description = input(f"New description (leave blank to keep current): ")
            priority = input(f"New priority (Low/Medium/High or leave blank to keep '{task.priority}'): ")
            due_input = input("New due date (YYYY-MM-DD or leave blank): ")

            updates = {}
            if name: updates["name"] = name
            if description: updates["description"] = description
            if priority: updates["priority"] = priority.capitalize()
            if due_input:
                try:
                    updates["due_date"] = datetime.strptime(due_input, "%Y-%m-%d")
                except ValueError:
                    print("Invaild date format. Skipping due date update")

                if manager.update_task(task_id, **updates):
                    print("Task updated")
                else:
                    print("Updated failed")

        elif choice == "4":
            try:
                task_id = int(input("Task ID to complete"))
            except ValueError:
                print("Invalid ID")
                continue
            if manager.complete_task(task_id):
                print("Task marked as completed")
            else:
                print("Task not found")

        elif choice == "5":
            try:
                task_id = int(input("Task ID tp complete"))
            except ValueError:
                print("Invalid value")
            if manager.delete_task(task_id):
                print("Task deleted")
            else:
                print("Task not found")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    run_cli()