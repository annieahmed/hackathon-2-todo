// frontend/src/components/todos/TodoItem.tsx

import React from 'react';
import { Todo } from '@/types/todo';
import Button from '@/components/ui/Button';

interface TodoItemProps {
  todo: Todo;
  onToggle: () => void;
  onDelete: () => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <li className="flex items-center justify-between p-4 bg-white border border-gray-200 rounded-lg shadow-sm">
      <div className="flex items-center">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={onToggle}
          className="h-4 w-4 text-blue-600 rounded focus:ring-blue-500"
        />
        <span className={`ml-3 text-gray-700 ${todo.completed ? 'line-through text-gray-400' : ''}`}>
          {todo.title}
        </span>
      </div>
      <div className="flex space-x-2">
        <Button variant="ghost" size="sm" onClick={onDelete}>
          Delete
        </Button>
      </div>
    </li>
  );
};

export default TodoItem;