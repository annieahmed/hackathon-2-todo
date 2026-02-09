// frontend/src/lib/api/api-client.ts

import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';

// Create the base API client instance
const createApiClient = (): AxiosInstance => {
  const apiClient = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
    timeout: 10000, // 10 seconds timeout
    headers: {
      'Content-Type': 'application/json',
    },
  });

  // Request interceptor to add JWT token to requests
  apiClient.interceptors.request.use(
    (config: AxiosRequestConfig) => {
      const token = localStorage.getItem('jwt_token');
      if (token && config.headers) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  // Response interceptor to handle responses globally
  apiClient.interceptors.response.use(
    (response: AxiosResponse) => {
      return response;
    },
    (error) => {
      // Handle specific error cases
      if (error.response?.status === 401) {
        // Token might be expired, redirect to login
        localStorage.removeItem('jwt_token');
        window.location.href = '/login'; // Force redirect to login
      }
      return Promise.reject(error);
    }
  );

  return apiClient;
};

// Export the configured API client instance
export const apiClient = createApiClient();

// Export a function to allow re-initializing the client if needed
export const resetApiClient = () => {
  // In case we need to reset the client with new configuration
  return createApiClient();
};