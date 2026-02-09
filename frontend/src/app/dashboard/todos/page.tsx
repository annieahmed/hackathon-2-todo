// frontend/src/app/dashboard/todos/page.tsx

'use client';

import React from 'react';
import { useAuth } from '@/contexts/AuthContext';
import ProtectedRoute from '@/components/providers/ProtectedRoute';
import TodoForm from '@/components/todos/TodoForm';
import TodoList from '@/components/todos/TodoList';
import Card from '@/components/ui/Card';

const TodosPage: React.FC = () => {
  const { user } = useAuth();

  const handleTodoAdded = (todo: any) => {
    // Refresh the todo list or update state as needed
    console.log('New todo added:', todo);
  };

  return (
    <ProtectedRoute>
      <div className="container mx-auto py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">My Todos</h1>
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <Card title="Add New Todo">
              <TodoForm onTodoAdded={handleTodoAdded} />
            </Card>
          </div>
          
          <div className="lg:col-span-1">
            <Card title="Todo List">
              {user && <TodoList userId={user.id} />}
            </Card>
          </div>
        </div>
      </div>
    </ProtectedRoute>
  );
};

export default TodosPage;