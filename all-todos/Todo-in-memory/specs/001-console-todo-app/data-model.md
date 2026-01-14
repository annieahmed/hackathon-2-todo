# Data Model: Console Todo Application

## Task Entity

### Properties
- **id** (int): Unique identifier for the task, automatically assigned
- **title** (str): Description/text of the task, required
- **completed** (bool): Status indicating if the task is completed, default False

### Relationships
- None (standalone entity)

### Validation Rules
- id: Must be unique within the application session
- title: Cannot be empty or None
- completed: Must be boolean value (True/False)

### State Transitions
- Pending (completed=False) → Completed (completed=True): When user marks task as completed
- Completed (completed=True) → Pending (completed=False): When user unmarks task as completed

## Task List Container

### Properties
- **tasks** (list): Collection of Task entities stored in memory
- **next_id** (int): Counter for assigning unique IDs to new tasks

### Operations
- Add Task: Creates new Task entity and adds to tasks list
- Get All Tasks: Returns all Task entities in the list
- Get Task by ID: Returns specific Task entity by its ID
- Update Task: Modifies properties of an existing Task entity
- Delete Task: Removes Task entity from the list
- Mark Complete: Updates completed status of a Task entity