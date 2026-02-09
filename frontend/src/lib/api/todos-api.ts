// frontend/src/lib/api/todos-api.ts

import { Todo, CreateTodoData, UpdateTodoData } from '@/types/todo';
import { apiClient } from './api-client';

/**
 * Fetch all todos for the authenticated user
 * @returns Promise resolving to an array of Todo objects
 */
export const fetchTodos = async (): Promise<Todo[]> => {
  const response = await apiClient.get<Todo[]>('/api/tasks');
  return response.data;
};

/**
 * Create a new todo
 * @param todoData The data for the new todo
 * @returns Promise resolving to the created Todo object
 */
export const createTodo = async (todoData: CreateTodoData): Promise<Todo> => {
  const response = await apiClient.post<Todo>('/api/tasks', todoData);
  return response.data;
};

/**
 * Update an existing todo
 * @param id The ID of the todo to update
 * @param todoData The updated data
 * @returns Promise resolving to the updated Todo object
 */
export const updateTodo = async (id: string, todoData: UpdateTodoData): Promise<Todo> => {
  const response = await apiClient.put<Todo>(`/api/tasks/${id}`, todoData);
  return response.data;
};

/**
 * Delete a todo
 * @param id The ID of the todo to delete
 * @returns Promise resolving when deletion is complete
 */
export const deleteTodo = async (id: string): Promise<void> => {
  await apiClient.delete(`/api/tasks/${id}`);
};

/**
 * Toggle the completion status of a todo
 * @param id The ID of the todo to toggle
 * @returns Promise resolving to the updated Todo object
 */
export const toggleTodoCompletion = async (id: string): Promise<Todo> => {
  const response = await apiClient.patch<Todo>(`/api/tasks/${id}/complete`);
  return response.data;
};