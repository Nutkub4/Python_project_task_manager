# Python Task Manager

A simple command-line task management application built with Python that helps you organize and track your daily tasks.

## Description

This Task Manager allows you to easily manage your daily tasks through a simple command-line interface. You can add tasks with descriptions and due dates, mark them as complete, delete them, and search through your task list. All tasks are automatically saved to a JSON file so your data persists between sessions.

## Features

- ✅ **Add Tasks**: Create new tasks with title, description, and due date
- 📋 **View Tasks**: Display all tasks organized by pending and completed status
- ✔️ **Mark Complete**: Mark tasks as done using their unique ID
- 🗑️ **Delete Tasks**: Remove tasks you no longer need
- 🔍 **Search**: Find tasks by keywords or due date
- 💾 **Auto-Save**: Tasks are automatically saved to a JSON file
- 🆔 **Unique IDs**: Each task gets a unique identifier for easy management

## Installation

### Clone the repository:
```bash
git clone https://github.com/Nutkub4/Python_project_task_manager
cd Python_project_task_manager
```

### Requirements:
- Python 3.6 or higher
- No additional packages required (uses only standard library)

## How to Run

### Navigate to the project directory:
```bash
cd python-task-manager
```

### Run the program:
```bash
python task_manager.py
```

### Follow the on-screen menu to manage your tasks!

## Usage Examples

### Adding a Task
```
Enter your choice (1-7): 1
Enter task title: Complete Python Project
Enter task description: Finish the task manager with all features
Enter due date (YYYY-MM-DD): 2025-11-20
Task added successfully! (ID: 1)
```

### Viewing Tasks
```
Enter your choice (1-7): 2

==================================================
PENDING TASKS
==================================================

[○] ID: 1
    Title: Complete Python Project
    Description: Finish the task manager with all features
    Due Date: 2025-11-20
```

### Marking a Task as Complete
```
Enter your choice (1-7): 3
Enter task ID to mark as complete: 1
Task 1 marked as complete!
```

### Deleting a Task
```
Enter your choice (1-7): 4
Enter task ID to delete: 1
Are you sure you want to delete task 1? (yes/no): yes
Task 1 deleted successfully!
```

### Save and Load Tasks
```
Enter your choice (1-7): 5
Save and Load Options:
1. Save tasks manually
2. Reload tasks from file
Enter choice (1-2): 1
Tasks saved successfully!
```

### Searching Tasks
```
Enter your choice (1-7): 6
Enter keyword or date to search: Python
Found 1 task(s):
[✓] ID: 1
    Title: Complete Python Project
```

## File Structure

```
python-task-manager/
│
├── task_manager.py    # Main application file
├── tasks.json         # Auto-generated file storing all tasks
└── README.md          # This file
```

## Data Storage

Tasks are stored in `tasks.json` in the following format:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "This is a sample task",
      "due_date": "2025-11-20",
      "completed": false
    }
  ],
  "next_id": 2
}
```

## Input Validation

The application includes validation for:
- Non-empty task titles and descriptions
- Proper date format (YYYY-MM-DD)
- Valid numeric input for task IDs
- Confirmation before deleting tasks

## Author

Created as part of a Practical Software Engineering project.