import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import useAuthStore from '../context/useAuthStore';

const ProtectedRoute = () => {
  // For demo purposes, we can bypass this or mock it.
  // Currently, the user will be forced to login.
  const { isAuthenticated } = useAuthStore();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
};

export default ProtectedRoute;
