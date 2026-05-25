import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import RightSidebar from './RightSidebar';
import Navbar from './Navbar';

const MainLayout = () => {
  return (
    <div className="min-h-screen bg-white dark:bg-background-dark max-w-7xl mx-auto flex justify-center w-full">
      <Sidebar />
      <main className="flex-1 min-w-0 sm:border-r border-gray-100 dark:border-gray-800 pb-16 sm:pb-0 max-w-[600px] w-full">
        <Outlet />
      </main>
      <RightSidebar />
      <Navbar />
    </div>
  );
};

export default MainLayout;
