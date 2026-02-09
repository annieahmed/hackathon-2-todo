import axios, { AxiosResponse } from 'axios';
import { LoginCredentials, RegisterCredentials, User, ApiResponse } from '@/src/utils/types';

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

export const authService = {
  // Register a new user
  register: async (credentials: RegisterCredentials): Promise<AxiosResponse<ApiResponse<User>>> => {
    try {
      const formData = new FormData();
      formData.append('email', credentials.email);
      formData.append('password', credentials.password);
      
      const response = await apiClient.post<ApiResponse<User>>('/auth/register', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Store token in localStorage
      if (response.data.success && response.data.data?.token) {
        localStorage.setItem('jwt_token', response.data.data.token);
      }
      return response;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Registration failed');
    }
  },

  // Login user
  login: async (credentials: LoginCredentials): Promise<AxiosResponse<ApiResponse<User>>> => {
    try {
      const formData = new FormData();
      formData.append('email', credentials.email);
      formData.append('password', credentials.password);
      
      const response = await apiClient.post<ApiResponse<User>>('/auth/login', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Store token in localStorage
      if (response.data.success && response.data.data?.token) {
        localStorage.setItem('jwt_token', response.data.data.token);
      }
      return response;
    } catch (error: any) {
      throw new Error(error.response?.data?.message || 'Login failed');
    }
  },

  // Logout user
  logout: async (): Promise<AxiosResponse<ApiResponse<void>>> => {
    try {
      const response = await apiClient.post<ApiResponse<void>>('/auth/logout');
      // Remove token from localStorage
      localStorage.removeItem('jwt_token');
      return response;
    } catch (error: any) {
      // Even if logout fails on the server, remove token locally
      localStorage.removeItem('jwt_token');
      throw new Error(error.response?.data?.message || 'Logout failed');
    }
  },

  // Get current user info
  getCurrentUser: async (): Promise<User | null> => {
    try {
      const token = localStorage.getItem('jwt_token');
      if (!token) {
        return null;
      }

      const response = await apiClient.get<ApiResponse<User>>('/auth/me');
      return response.data.data?.user || null;
    } catch (error) {
      console.error('Error getting current user:', error);
      return null;
    }
  },

  // Check if user is authenticated
  isAuthenticated: (): boolean => {
    const token = localStorage.getItem('jwt_token');
    if (!token) {
      return false;
    }

    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      const exp = payload.exp;
      // Check if token is expired
      if (exp && Date.now() >= exp * 1000) {
        localStorage.removeItem('jwt_token');
        return false;
      }
      return true;
    } catch (error) {
      localStorage.removeItem('token');
      return false;
    }
  }
};