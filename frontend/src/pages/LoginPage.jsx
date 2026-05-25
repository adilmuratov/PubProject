import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import useAuthStore from '../context/useAuthStore';
import { login as apiLogin } from '../api/auth';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { login } = useAuthStore();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const data = await apiLogin({ email, password });
      login(data.user, data.token);
      navigate('/');
    } catch (err) {
      setError(err.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-background-dark p-4">
      <div className="w-full max-w-md bg-white dark:bg-surface-dark p-8 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-800">
        <div className="text-center mb-8">
          <div className="w-12 h-12 rounded-full bg-primary flex items-center justify-center text-white font-bold italic mx-auto mb-4 text-xl">
            X
          </div>
          <h1 className="text-2xl font-bold dark:text-white">Sign in to X</h1>
        </div>

        {error && <div className="mb-4 text-red-500 text-sm text-center">{error}</div>}

        <form onSubmit={handleLogin} className="space-y-4">
          <Input 
            type="text" 
            placeholder="Email or username" 
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="p-3 text-base"
          />
          <Input 
            type="password" 
            placeholder="Password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="p-3 text-base"
          />
          
          <Button type="submit" isLoading={loading} className="w-full py-3 text-lg mt-4">
            Sign In
          </Button>
        </form>

        <p className="mt-6 text-center text-gray-500 text-sm">
          Don't have an account? <Link to="/register" className="text-primary hover:underline">Sign up</Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
