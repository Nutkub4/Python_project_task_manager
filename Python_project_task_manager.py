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