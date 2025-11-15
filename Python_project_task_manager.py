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