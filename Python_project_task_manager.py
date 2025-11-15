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