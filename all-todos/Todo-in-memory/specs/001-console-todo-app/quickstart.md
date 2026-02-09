# Quickstart Guide: Console Todo Application

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for dependency management)

## Setup

1. Clone or download the project files
2. Navigate to the project directory in your terminal
3. Install dependencies (if any) using UV:
   ```bash
   uv sync
   ```
   Or simply ensure Python 3.13+ is available in your environment

## Running the Application

Execute the main application file:

```bash
python todo_app.py
```

Or if using UV:

```bash
uv run python todo_app.py
```

## Using the Application

Once the application starts, you'll see a menu with the following options:

1. **Add Task**: Enter a new task description
2. **View Tasks**: Display all current tasks with their status
3. **Update Task**: Modify the description of an existing task
4. **Mark Complete**: Change a task's status to completed
5. **Delete Task**: Remove a task from the list
6. **Exit**: Quit the application

Follow the on-screen prompts to navigate between options. The application will keep running until you choose to exit.

## Example Usage

```
Welcome to the Todo Application!
1. Add Task
2. View Tasks
3. Update Task
4. Mark Complete
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

## Notes

- All tasks are stored in memory only and will be lost when the application exits
- Task IDs are automatically assigned and remain consistent during the session
- Invalid inputs will be handled gracefully with error messages