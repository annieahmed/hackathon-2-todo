// frontend/src/lib/utils/loading-state.ts

/**
 * Loading state type for consistent loading state management
 */
export type LoadingState = 'idle' | 'loading' | 'success' | 'error';

/**
 * Loading state with data and error information
 */
export interface LoadingStateWithDetails<T = any> {
  state: LoadingState;
  data?: T;
  error?: any;
  message?: string;
}

/**
 * Create initial loading state
 * @returns Initial loading state
 */
export const initialLoadingState = <T = any>(): LoadingStateWithDetails<T> => ({
  state: 'idle',
});

/**
 * Create loading state
 * @returns Loading state
 */
export const loadingState = <T = any>(): LoadingStateWithDetails<T> => ({
  state: 'loading',
});

/**
 * Create success state
 * @param data The data to include in the success state
 * @returns Success state with data
 */
export const successState = <T = any>(data: T): LoadingStateWithDetails<T> => ({
  state: 'success',
  data,
});

/**
 * Create error state
 * @param error The error to include in the error state
 * @param message Optional error message
 * @returns Error state with error details
 */
export const errorState = <T = any>(error: any, message?: string): LoadingStateWithDetails<T> => ({
  state: 'error',
  error,
  message: message || (typeof error === 'string' ? error : error.message),
});