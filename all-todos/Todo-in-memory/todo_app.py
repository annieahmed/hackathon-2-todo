"""
Console Todo Application
An in-memory, console-based todo application implemented in Python.
"""

class Task:
    """
    Represents a single todo task with an ID, title, and completion status.
    """
    
    def __init__(self, task_id, title):
        """
        Initialize a new Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Description of the task
        """
        self.id = task_id
        self.title = title
        self.completed = False
    
    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
    
    def mark_pending(self):
        """Mark the task as pending (not completed)."""
        self.completed = False
    
    def __str__(self):
        """Return a string representation of the task."""
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.title}"


class TaskManager:
    """
    Manages all operations on tasks including adding, viewing, updating, 
    deleting, and marking tasks as completed.
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title):
        """
        Add a new task to the list.
        
        Args:
            title (str): The title/description of the task
            
        Returns:
            Task: The newly created task object
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(self.next_id, title.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_all_tasks(self):
        """
        Get all tasks in the list.
        
        Returns:
            list: List of all Task objects
        """
        return self.tasks
    
    def get_task_by_id(self, task_id):
        """
        Get a specific task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Task: The task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id, new_title):
        """
        Update the title of an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            new_title (str): The new title for the task
            
        Returns:
            bool: True if the task was updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            if not new_title or not new_title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = new_title.strip()
            return True
        return False
    
    def delete_task(self, task_id):
        """
        Delete a task from the list.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def mark_task_completed(self, task_id):
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The ID of the task to mark as completed
            
        Returns:
            bool: True if the task was marked as completed, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_completed()
            return True
        return False
    
    def mark_task_pending(self, task_id):
        """
        Mark a task as pending (not completed).
        
        Args:
            task_id (int): The ID of the task to mark as pending
            
        Returns:
            bool: True if the task was marked as pending, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_pending()
            return True
        return False


class ConsoleInterface:
    """
    Provides the console-based user interface for interacting with the todo application.
    """
    
    def __init__(self):
        """Initialize the console interface with a task manager."""
        self.task_manager = TaskManager()
    
    def display_menu(self):
        """Display the main menu options to the user."""
        print("\n" + "="*40)
        print("Welcome to the Todo Application!")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        print("="*40)
    
    def get_user_choice(self):
        """
        Get and validate the user's menu choice.
        
        Returns:
            int: The user's menu choice (1-6)
        """
        while True:
            try:
                choice = int(input("Choose an option (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
    
    def add_task_ui(self):
        """Handle the UI for adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task description: ").strip()
        
        if not title:
            print("Task description cannot be empty.")
            return
        
        try:
            task = self.task_manager.add_task(title)
            print(f"Task '{task.title}' added successfully with ID {task.id}!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def view_tasks_ui(self):
        """Handle the UI for viewing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)
    
    def update_task_ui(self):
        """Handle the UI for updating an existing task."""
        print("\n--- Update Task ---")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks to update.")
            return
        
        self.view_tasks_ui()
        
        try:
            task_id = int(input("Enter the ID of the task to update: "))
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return
        
        new_title = input(f"Enter new description for task '{task.title}': ").strip()
        
        if not new_title:
            print("Task description cannot be empty.")
            return
        
        try:
            if self.task_manager.update_task(task_id, new_title):
                print(f"Task ID {task_id} updated successfully!")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def mark_task_completed_ui(self):
        """Handle the UI for marking a task as completed."""
        print("\n--- Mark Task as Completed ---")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks to mark as completed.")
            return
        
        self.view_tasks_ui()
        
        try:
            task_id = int(input("Enter the ID of the task to mark as completed: "))
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return
        
        if self.task_manager.mark_task_completed(task_id):
            print(f"Task ID {task_id} marked as completed!")
        else:
            print(f"No task found with ID {task_id}.")
    
    def delete_task_ui(self):
        """Handle the UI for deleting a task."""
        print("\n--- Delete Task ---")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks to delete.")
            return
        
        self.view_tasks_ui()
        
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return
        
        if self.task_manager.delete_task(task_id):
            print(f"Task ID {task_id} deleted successfully!")
        else:
            print(f"No task found with ID {task_id}.")
    
    def run(self):
        """Run the main application loop."""
        print("Starting the Todo Application...")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 1:
                self.add_task_ui()
            elif choice == 2:
                self.view_tasks_ui()
            elif choice == 3:
                self.update_task_ui()
            elif choice == 4:
                self.mark_task_completed_ui()
            elif choice == 5:
                self.delete_task_ui()
            elif choice == 6:
                print("\nThank you for using the Todo Application. Goodbye!")
                break


def main():
    """Main entry point for the application."""
    app = ConsoleInterface()
    app.run()


if __name__ == "__main__":
    main()