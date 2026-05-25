import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { Home, User, Settings, LogOut, Bell, Search } from 'lucide-react';
import useAuthStore from '../context/useAuthStore';
import Button from '../components/ui/Button';

const Sidebar = () => {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const navItems = [
    { name: 'Home', path: '/', icon: Home },
    { name: 'Explore', path: '/explore', icon: Search },
    { name: 'Notifications', path: '/notifications', icon: Bell },
    { name: 'Profile', path: `/profile/${user?.username || 'me'}`, icon: User },
    { name: 'Settings', path: '/settings', icon: Settings },
  ];

  return (
    <div className="hidden sm:flex flex-col justify-between w-20 xl:w-64 h-screen sticky top-0 py-4 px-2 xl:px-4 border-r border-gray-100 dark:border-gray-800 bg-white dark:bg-background-dark">
      <div>
        <div className="flex items-center justify-center xl:justify-start w-12 h-12 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer transition-colors xl:px-4 mb-4">
          <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold italic">
            X
          </div>
        </div>

        <nav className="space-y-2 mt-4">
          {navItems.map((item) => (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center justify-center xl:justify-start gap-4 p-3 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-xl ${
                  isActive ? 'font-bold' : 'font-medium text-gray-700 dark:text-gray-300'
                }`
              }
            >
              <item.icon className="w-7 h-7" />
              <span className="hidden xl:block">{item.name}</span>
            </NavLink>
          ))}
        </nav>
        
        <div className="mt-6 flex justify-center xl:justify-start px-2">
           <Button className="w-12 h-12 rounded-full xl:w-full xl:rounded-full shadow-md text-lg">
             <span className="hidden xl:block">Post</span>
             <span className="xl:hidden">+</span>
           </Button>
        </div>
      </div>

      <div className="flex items-center justify-center xl:justify-between p-3 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer transition-colors mt-auto" onClick={handleLogout}>
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-gray-300 dark:bg-gray-700 overflow-hidden">
            <img src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${user?.username || 'user'}`} alt="avatar" />
          </div>
          <div className="hidden xl:block text-left">
            <p className="font-bold text-sm leading-tight dark:text-white">{user?.name || 'User'}</p>
            <p className="text-gray-500 text-sm leading-tight">@{user?.username || 'user'}</p>
          </div>
        </div>
        <LogOut className="hidden xl:block w-5 h-5 text-gray-500" />
      </div>
    </div>
  );
};

export default Sidebar;
