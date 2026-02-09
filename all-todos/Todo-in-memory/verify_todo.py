import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import todo_app

# Create a simple test to verify all functionality
def test_application_logic():
    print("Testing the Todo Application Logic...")
    
    # Create a fresh task manager for testing
    tm = todo_app.TaskManager()
    
    # Test 1: Add a task
    print("\n1. Testing Add Task:")
    task = tm.add_task("Buy groceries")
    print(f"   Added task: {task}")
    assert task.title == "Buy groceries"
    assert task.id == 1
    assert task.completed == False
    
    # Test 2: Add another task
    task2 = tm.add_task("Walk the dog")
    print(f"   Added task: {task2}")
    assert task2.id == 2
    assert task2.title == "Walk the dog"
    
    # Test 3: View all tasks
    print("\n2. Testing View All Tasks:")
    all_tasks = tm.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    assert len(all_tasks) == 2
    
    # Test 4: Mark a task as completed
    print("\n3. Testing Mark Task as Completed:")
    success = tm.mark_task_completed(1)
    print(f"   Marked task 1 as completed: {success}")
    assert success == True
    assert all_tasks[0].completed == True  # First task should now be completed
    
    # Test 5: Update a task
    print("\n4. Testing Update Task:")
    success = tm.update_task(2, "Walk the cat")
    print(f"   Updated task 2: {success}")
    assert success == True
    assert all_tasks[1].title == "Walk the cat"
    
    # Test 6: Get task by ID
    print("\n5. Testing Get Task by ID:")
    retrieved_task = tm.get_task_by_id(1)
    print(f"   Retrieved task 1: {retrieved_task}")
    assert retrieved_task is not None
    assert retrieved_task.id == 1
    
    # Test 7: Delete a task
    print("\n6. Testing Delete Task:")
    initial_count = len(tm.get_all_tasks())
    success = tm.delete_task(2)
    print(f"   Deleted task 2: {success}")
    assert success == True
    assert len(tm.get_all_tasks()) == initial_count - 1
    
    print("\nPASS: All functionality tests passed!")
    
    # Show final state
    print("\nFinal task list:")
    for task in tm.get_all_tasks():
        print(f"  {task}")

if __name__ == "__main__":
    test_application_logic()