import axios, { AxiosResponse } from 'axios';
import { Task, TaskFormData, ApiResponse } from '@/src/utils/types';

// Base API URL from environment
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

// Create axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to requests if available
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('jwt_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token expiration or invalidation
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Clear token if unauthorized
      localStorage.removeItem('jwt_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const apiService = {
  // Get all tasks for the authenticated user
  getTasks: async (): Promise<AxiosResponse<ApiResponse<{tasks: Task[]}>>> => {
    try {
      const response = await apiClient.get<ApiResponse<{tasks: Task[]}>>('/api/tasks');
      return response;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to fetch tasks');
    }
  },

  // Create a new task
  createTask: async (taskData: TaskFormData): Promise<Task> => {
    try {
      const response = await apiClient.post<ApiResponse<Task>>('/api/tasks', {
        title: taskData.title,
        description: taskData.description,
        completed: taskData.completed
      });
      return response.data.data!.task;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to create task');
    }
  },

  // Get a specific task by ID
  getTaskById: async (taskId: string): Promise<Task> => {
    try {
      const response = await apiClient.get<ApiResponse<Task>>(`/api/tasks/${taskId}`);
      return response.data.data!.task;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to fetch task');
    }
  },

  // Update a task
  updateTask: async (taskId: string, taskData: TaskFormData): Promise<Task> => {
    try {
      const response = await apiClient.put<ApiResponse<Task>>(`/api/tasks/${taskId}`, {
        title: taskData.title,
        description: taskData.description,
        completed: taskData.completed
      });
      return response.data.data!.task;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to update task');
    }
  },

  // Delete a task
  deleteTask: async (taskId: string): Promise<void> => {
    try {
      await apiClient.delete(`/api/tasks/${taskId}`);
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to delete task');
    }
  },

  // Toggle task completion status
  toggleTaskCompletion: async (taskId: string): Promise<Task> => {
    try {
      const response = await apiClient.patch<ApiResponse<Task>>(`/api/tasks/${taskId}/complete`);
      return response.data.data!.task;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Failed to toggle task completion');
    }
  }
};