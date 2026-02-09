// frontend/src/components/providers/ProtectedRoute.tsx

import React, { ReactElement } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';

interface ProtectedRouteProps {
  children: ReactElement;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { loading, isAuthenticated } = useAuth();
  const router = useRouter();
  const [authorized, setAuthorized] = useState(false);

  useEffect(() => {
    // If auth isn't loaded yet, don't render anything
    if (loading) return;

    // If user is not authenticated, redirect to login
    if (!isAuthenticated()) {
      router.push('/login');
    } else {
      setAuthorized(true);
    }
  }, [loading, isAuthenticated, router]);

  // Show nothing while checking authentication status
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  // If authorized, render the child components
  return authorized ? children : null;
};

export default ProtectedRoute;