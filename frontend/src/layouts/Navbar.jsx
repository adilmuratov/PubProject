import React from 'react';
import { NavLink } from 'react-router-dom';
import { Home, Search, Bell, User } from 'lucide-react';
import useAuthStore from '../context/useAuthStore';

const Navbar = () => {
  const { user } = useAuthStore();

  const navItems = [
    { name: 'Home', path: '/', icon: Home },
    { name: 'Explore', path: '/explore', icon: Search },
    { name: 'Notifications', path: '/notifications', icon: Bell },
    { name: 'Profile', path: `/profile/${user?.username || 'me'}`, icon: User },
  ];

  return (
    <nav className="sm:hidden fixed bottom-0 left-0 right-0 bg-white dark:bg-background-dark border-t border-gray-200 dark:border-gray-800 flex justify-around items-center h-14 z-50">
      {navItems.map((item) => (
        <NavLink
          key={item.name}
          to={item.path}
          className={({ isActive }) =>
            `flex flex-col items-center justify-center w-full h-full text-gray-500 hover:text-primary transition-colors ${
              isActive ? 'text-primary' : 'dark:text-gray-400'
            }`
          }
        >
          <item.icon className="w-6 h-6" />
        </NavLink>
      ))}
    </nav>
  );
};

export default Navbar;
