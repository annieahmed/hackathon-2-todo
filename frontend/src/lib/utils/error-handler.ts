// frontend/src/lib/utils/error-handler.ts

/**
 * Standardized error type for the application
 */
export interface AppError {
  message: string;
  code?: string;
  status?: number;
  details?: any;
}

/**
 * Generic error handler that formats errors consistently
 * @param error The error to handle
 * @returns A standardized AppError object
 */
export const handleError = (error: any): AppError => {
  // If it's already an AppError, return as is
  if (isAppError(error)) {
    return error;
  }

  // Handle fetch/axios errors
  if (error.response) {
    // Server responded with error status
    return {
      message: error.response.data?.message || `Server error: ${error.response.status}`,
      status: error.response.status,
      code: error.code,
      details: error.response.data,
    };
  } else if (error.request) {
    // Request was made but no response received
    return {
      message: 'Network error: Unable to reach the server',
      code: 'NETWORK_ERROR',
    };
  } else {
    // Something else happened
    return {
      message: error.message || 'An unexpected error occurred',
      code: error.code,
    };
  }
};

/**
 * Type guard to check if an error is an AppError
 * @param error The error to check
 * @returns True if the error is an AppError, false otherwise
 */
export const isAppError = (error: any): error is AppError => {
  return error && typeof error.message === 'string';
};

/**
 * Log error with consistent format
 * @param error The error to log
 * @param context Optional context information
 */
export const logError = (error: any, context?: string): void => {
  const appError = handleError(error);
  console.error(`[${context || 'APP'}] Error:`, {
    message: appError.message,
    status: appError.status,
    code: appError.code,
    details: appError.details,
    stack: error.stack,
  });
};