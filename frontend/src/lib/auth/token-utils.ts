// frontend/src/lib/auth/token-utils.ts

/**
 * Store JWT token in localStorage
 * @param token The JWT token to store
 */
export const storeToken = (token: string): void => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('jwt_token', token);
  }
};

/**
 * Retrieve JWT token from localStorage
 * @returns The stored JWT token or null if not found
 */
export const getToken = (): string | null => {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('jwt_token');
  }
  return null;
};

/**
 * Remove JWT token from localStorage
 */
export const removeToken = (): void => {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('jwt_token');
  }
};

/**
 * Decode JWT token payload without verification
 * @param token The JWT token to decode
 * @returns The decoded payload or null if invalid
 */
export const decodeToken = (token: string): any | null => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );
    
    return JSON.parse(jsonPayload);
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};

/**
 * Check if the token is expired
 * @param token The JWT token to check
 * @returns True if the token is expired, false otherwise
 */
export const isTokenExpired = (token: string): boolean => {
  const decoded = decodeToken(token);
  if (!decoded || !decoded.exp) {
    return true; // If there's no exp claim, consider it expired
  }

  const currentTime = Math.floor(Date.now() / 1000);
  return decoded.exp < currentTime;
};

/**
 * Get token expiration time
 * @param token The JWT token to check
 * @returns The expiration timestamp or null if not available
 */
export const getTokenExpiration = (token: string): number | null => {
  const decoded = decodeToken(token);
  return decoded?.exp || null;
};

/**
 * Check if the token is about to expire (within 5 minutes)
 * @param token The JWT token to check
 * @returns True if the token is about to expire, false otherwise
 */
export const isTokenAboutToExpire = (token: string): boolean => {
  const decoded = decodeToken(token);
  if (!decoded || !decoded.exp) {
    return true; // If there's no exp claim, consider it about to expire
  }

  const currentTime = Math.floor(Date.now() / 1000);
  const fiveMinutesInSeconds = 5 * 60;
  return decoded.exp - currentTime < fiveMinutesInSeconds;
};