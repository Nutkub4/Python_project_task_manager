import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()
    
    def _display_task(self, task):
        """Helper function to display a single task"""
        status = "✓" if task['completed'] else "○"
        print(f"\n[{status}] ID: {task['id']}")
        print(f"    Title: {task['title']}")
        print(f"    Description: {task['description']}")
        print(f"    Due Date: {task['due_date']}")

    def add_task(self, title, description, due_date):
        """Add a new task"""
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task added successfully! (ID: {task['id']})")    

    def view_tasks(self):
        """Display all tasks organized by status"""
        if not self.tasks:
            print("\nNo tasks found!")
            return
        
        pending = [t for t in self.tasks if not t['completed']]
        completed = [t for t in self.tasks if t['completed']]
        
        print("\n" + "="*50)
        print("PENDING TASKS")
        print("="*50)
        if pending:
            for task in pending:
                self._display_task(task)
        else:
            print("No pending tasks.")
        
        print("\n" + "="*50)
        print("COMPLETED TASKS")
        print("="*50)
        if completed:
            for task in completed:
                self._display_task(task)
        else:
            print("No completed tasks.")

    def mark_complete(self, task_id):
        """Mark a task as complete"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        """Delete a task by ID"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                data = {
                    'tasks': self.tasks,
                    'next_id': self.next_id
                }
                json.dump(data, f, indent=2)
            print("Tasks saved successfully!")
        except:
            print("Error saving tasks.")

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = data.get('tasks', [])
                    self.next_id = data.get('next_id', 1)
                print(f"Loaded {len(self.tasks)} tasks.")
            except:
                print("Error loading tasks. Starting fresh.")
        else:
            print("No saved tasks found. Starting fresh.")
                
    def search_tasks(self, keyword):
        """Search tasks by keyword or due date"""
        results = []
        keyword_lower = keyword.lower()
        
        for task in self.tasks:
            if (keyword_lower in task['title'].lower() or 
                keyword_lower in task['description'].lower() or 
                keyword_lower in task['due_date']):
                results.append(task)
        
        if results:
            print(f"\nFound {len(results)} task(s):")
            for task in results:
                self._display_task(task)
        else:
            print("No tasks found matching your search.")

def validate_date(date_string):
    """Validate date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except:
        return False

def main():
    manager = TaskManager()
    
    while True:
        print("\n" + "="*50)
        print("TASK MANAGER MENU")
        print("="*50)
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Load Tasks")
        print("6. Search Tasks")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            # Add new task
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Title cannot be empty!")
                continue
            
            description = input("Enter task description: ").strip()
            if not description:
                print("Error: Description cannot be empty!")
                continue
            
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            if not validate_date(due_date):
                print("Error: Invalid date format! Use YYYY-MM-DD")
                continue
            
            manager.add_task(title, description, due_date)
        
        elif choice == '2':
            # View all tasks
            manager.view_tasks()
        
        elif choice == '3':
            # Mark task as complete
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                manager.mark_complete(task_id)
            except ValueError:
                print("Error: Please enter a valid number!")
        
        elif choice == '4':
            # Delete task
            try:
                task_id = int(input("Enter task ID to delete: "))
                confirm = input(f"Are you sure you want to delete task {task_id}? (yes/no): ")
                if confirm.lower() == 'yes':
                    manager.delete_task(task_id)
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Error: Please enter a valid number!")
        
        elif choice == '5':
            # Save and Load Tasks
            print("\nSave and Load Options:")
            print("1. Save tasks manually")
            print("2. Reload tasks from file")
            sub_choice = input("Enter choice (1-2): ").strip()
            
            if sub_choice == '1':
                manager.save_tasks()
            elif sub_choice == '2':
                manager.load_tasks()
            else:
                print("Invalid choice!")
        
        elif choice == '6':
            # Search tasks
            keyword = input("Enter keyword or date to search: ").strip()
            if keyword:
                manager.search_tasks(keyword)
            else:
                print("Error: Search term cannot be empty!")
        
        elif choice == '7':
            # Exit
            print("\nThank you for using Task Manager!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()