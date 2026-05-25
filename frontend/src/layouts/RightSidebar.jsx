import React from 'react';
import { Search } from 'lucide-react';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';

const RightSidebar = () => {
  const trendingTopics = [
    { tag: 'React', posts: '124K' },
    { tag: 'TailwindCSS', posts: '45K' },
    { tag: 'Vite', posts: '12K' },
    { tag: 'Zustand', posts: '8K' },
  ];

  const suggestedUsers = [
    { name: 'John Doe', username: 'johndoe' },
    { name: 'Jane Smith', username: 'janesmith' },
  ];

  return (
    <div className="hidden lg:block w-80 py-4 px-6 h-screen sticky top-0 overflow-y-auto">
      <div className="relative mb-6">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <Search className="h-5 w-5 text-gray-400" />
        </div>
        <Input 
          type="text" 
          placeholder="Search..." 
          className="pl-10 bg-gray-100 border-transparent focus:bg-white dark:bg-gray-800 dark:focus:bg-gray-900 rounded-full" 
        />
      </div>

      <div className="bg-gray-50 dark:bg-surface-dark rounded-2xl mb-6 p-4">
        <h2 className="text-xl font-bold mb-4 dark:text-white">What's happening</h2>
        <div className="space-y-4">
          {trendingTopics.map((topic) => (
            <div key={topic.tag} className="cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 p-2 -mx-2 rounded-xl transition-colors">
              <p className="text-sm text-gray-500">Trending in Tech</p>
              <p className="font-bold dark:text-white">#{topic.tag}</p>
              <p className="text-sm text-gray-500">{topic.posts} posts</p>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-gray-50 dark:bg-surface-dark rounded-2xl p-4">
        <h2 className="text-xl font-bold mb-4 dark:text-white">Who to follow</h2>
        <div className="space-y-4">
          {suggestedUsers.map((user) => (
            <div key={user.username} className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <div className="w-10 h-10 rounded-full bg-gray-300 dark:bg-gray-700 overflow-hidden">
                  <img src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${user.username}`} alt={user.username} />
                </div>
                <div>
                  <p className="font-bold text-sm leading-tight dark:text-white hover:underline cursor-pointer">{user.name}</p>
                  <p className="text-gray-500 text-sm leading-tight">@{user.username}</p>
                </div>
              </div>
              <Button variant="secondary" size="sm" className="rounded-full font-bold">Follow</Button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RightSidebar;
