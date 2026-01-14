# Console Todo Application

A simple, in-memory, console-based todo application implemented in Python.

## Features

- Add new todo tasks
- View all tasks with completion status
- Update existing task descriptions
- Mark tasks as completed
- Delete tasks
- All data stored in memory only (resets on exit)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation required - uses only Python standard library

## Usage

Run the application:

```bash
python todo_app.py
```

The application will start with a menu offering the following options:
1. Add Task - Enter a new task description
2. View Tasks - Display all current tasks with their status
3. Update Task - Modify the description of an existing task
4. Mark Task as Completed - Change a task's status to completed
5. Delete Task - Remove a task from the list
6. Exit - Quit the application

Follow the on-screen prompts to navigate between options. The application will keep running until you choose to exit.

## Example Usage

```
Welcome to the Todo Application!
1. Add Task
2. View Tasks
3. Update Task
4. Mark Task as Completed
5. Delete Task
6. Exit

Choose an option: 1
Enter task description: Buy groceries
Task added successfully!

Choose an option: 2
Tasks:
1. [ ] Buy groceries

Choose an option: 4
Enter task ID to mark complete: 1
Task marked as complete!

Choose an option: 2
Tasks:
1. [x] Buy groceries

Choose an option: 6
Goodbye!
```

## Architecture

The application follows a layered architecture:

- **Task Model**: Represents individual todo items with id, title, and completion status
- **Task Manager**: Handles all operations on tasks (add, view, update, delete, mark complete)
- **Console Interface**: Provides the menu-driven user interface

## Data Storage

All tasks are stored in memory only and will be lost when the application exits.