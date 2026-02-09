// frontend/src/components/todos/TodoList.tsx

'use client';

import React, { useState, useEffect } from 'react';
import { Todo } from '@/types/todo';
import TodoItem from './TodoItem';
import { apiClient } from '@/lib/api/api-client';
import { loadingState, successState, errorState, initialLoadingState } from '@/lib/utils/loading-state';
import { handleError } from '@/lib/utils/error-handler';
import LoadingSpinner from '@/components/ui/LoadingSpinner';
import ErrorDisplay from '@/components/ui/ErrorDisplay';

interface TodoListProps {
  userId: string;
}

const TodoList: React.FC<TodoListProps> = ({ userId }) => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loadingStateValue, setLoadingStateValue] = useState(initialLoadingState<Todo[]>());
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      setLoadingStateValue(loadingState());
      setError(null);

      const response = await apiClient.get<Todo[]>('/api/tasks');
      setTodos(response.data);
      setLoadingStateValue(successState(response.data));
    } catch (err) {
      const appError = handleError(err);
      setError(appError.message);
      setLoadingStateValue(errorState<Todo[]>(err, appError.message));
      console.error('Error fetching todos:', err);
    }
  };

  const handleToggleComplete = async (id: string) => {
    try {
      const response = await apiClient.patch<Todo>(`/api/tasks/${id}/complete`);
      setTodos(todos.map(todo =>
        todo.id === id ? { ...todo, completed: response.data.completed } : todo
      ));
    } catch (err) {
      const appError = handleError(err);
      setError(appError.message);
      console.error('Error toggling todo:', err);
    }
  };

  const handleDelete = async (id: string) => {
    try {
      await apiClient.delete(`/api/tasks/${id}`);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err) {
      const appError = handleError(err);
      setError(appError.message);
      console.error('Error deleting todo:', err);
    }
  };

  if (loadingStateValue.state === 'loading') {
    return (
      <div className="flex justify-center items-center py-10">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  if (loadingStateValue.state === 'error') {
    return (
      <ErrorDisplay
        message={error || 'Error loading todos'}
        onRetry={fetchTodos}
        retryText="Reload Todos"
      />
    );
  }

  return (
    <div className="space-y-4">
      {error && (
        <ErrorDisplay
          message={error}
          onRetry={fetchTodos}
          retryText="Retry"
        />
      )}

      {todos.length === 0 ? (
        <div className="text-center py-10">
          <p className="text-gray-500">No todos yet. Add your first todo!</p>
        </div>
      ) : (
        <ul className="space-y-2">
          {todos.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={() => handleToggleComplete(todo.id)}
              onDelete={() => handleDelete(todo.id)}
            />
          ))}
        </ul>
      )}
    </div>
  );
};

export default TodoList;