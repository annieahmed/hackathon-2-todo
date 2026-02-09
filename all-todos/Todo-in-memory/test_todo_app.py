"""
Test script for the console todo application.
This script tests all the core functionality without requiring user input.
"""

from todo_app import Task, TaskManager, ConsoleInterface

def test_task_creation():
    """Test creating a task."""
    print("Testing Task Creation...")
    task = Task(1, "Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False
    print("PASS: Task creation works correctly")


def test_task_completion():
    """Test marking a task as completed."""
    print("\nTesting Task Completion...")
    task = Task(1, "Test task")
    assert task.completed == False
    task.mark_completed()
    assert task.completed == True
    task.mark_pending()
    assert task.completed == False
    print("PASS: Task completion toggling works correctly")


def test_task_manager_add():
    """Test adding tasks to the manager."""
    print("\nTesting Task Manager Add...")
    tm = TaskManager()
    task = tm.add_task("First task")
    assert len(tm.get_all_tasks()) == 1
    assert task.id == 1
    assert task.title == "First task"

    task2 = tm.add_task("Second task")
    assert len(tm.get_all_tasks()) == 2
    assert task2.id == 2
    assert task2.title == "Second task"
    print("PASS: Task addition works correctly")


def test_task_manager_update():
    """Test updating tasks."""
    print("\nTesting Task Manager Update...")
    tm = TaskManager()
    task = tm.add_task("Original task")

    success = tm.update_task(1, "Updated task")
    assert success == True
    assert task.title == "Updated task"

    # Try to update a non-existent task
    success = tm.update_task(99, "Non-existent task")
    assert success == False
    print("PASS: Task update works correctly")


def test_task_manager_delete():
    """Test deleting tasks."""
    print("\nTesting Task Manager Delete...")
    tm = TaskManager()
    tm.add_task("First task")
    tm.add_task("Second task")
    assert len(tm.get_all_tasks()) == 2

    success = tm.delete_task(1)
    assert success == True
    assert len(tm.get_all_tasks()) == 1

    # Try to delete a non-existent task
    success = tm.delete_task(99)
    assert success == False
    print("PASS: Task deletion works correctly")


def test_task_manager_completion():
    """Test marking tasks as completed."""
    print("\nTesting Task Manager Completion...")
    tm = TaskManager()
    task = tm.add_task("Test task")
    assert task.completed == False

    success = tm.mark_task_completed(1)
    assert success == True
    assert task.completed == True

    success = tm.mark_task_pending(1)
    assert success == True
    assert task.completed == False

    # Try to mark a non-existent task
    success = tm.mark_task_completed(99)
    assert success == False
    print("PASS: Task completion marking works correctly")


def test_error_handling():
    """Test error handling for invalid inputs."""
    print("\nTesting Error Handling...")
    tm = TaskManager()

    # Try to add an empty task
    try:
        tm.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Try to add a task with only spaces
    try:
        tm.add_task("   ")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Try to update a task with empty title
    tm.add_task("Valid task")
    try:
        tm.update_task(1, "")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    print("PASS: Error handling works correctly")


def run_all_tests():
    """Run all tests."""
    print("Running tests for the Todo Application...\n")
    
    test_task_creation()
    test_task_completion()
    test_task_manager_add()
    test_task_manager_update()
    test_task_manager_delete()
    test_task_manager_completion()
    test_error_handling()
    
    print("\n" + "="*50)
    print("SUCCESS: All tests passed! The Todo Application is working correctly.")
    print("="*50)


if __name__ == "__main__":
    run_all_tests()