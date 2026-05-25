const USERS_KEY = 'mock_users';
const POSTS_KEY = 'mock_posts';

export const delay = (ms = 300) => new Promise(resolve => setTimeout(resolve, ms));

const seedUsers = [
  {
    id: 1,
    username: 'frontend_dev',
    displayName: 'Sarah Dev',
    bio: 'Frontend Engineer @TechCorp | React & Vite enthusiast | Building awesome UIs 🎨',
    location: 'San Francisco, CA',
    website: 'https://sarahdev.io',
    joinedAt: 'March 2024',
    followers: 1240,
    following: 385,
    avatarUrl: 'https://i.pravatar.cc/150?u=1',
    coverUrl: 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=1000&auto=format&fit=crop'
  },
  {
    id: 2,
    username: 'ui_designer',
    displayName: 'Alex Chen',
    bio: 'UI/UX Designer. Lover of whitespace and typography.',
    location: 'New York, NY',
    website: 'https://alexchen.design',
    joinedAt: 'January 2025',
    followers: 850,
    following: 210,
    avatarUrl: 'https://i.pravatar.cc/150?u=2',
    coverUrl: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop'
  },
  {
    id: 3,
    username: 'react_guru',
    displayName: 'Mike Johnson',
    bio: 'Open source contributor. React core team member.',
    location: 'London, UK',
    website: 'https://mikejohnson.dev',
    joinedAt: 'May 2023',
    followers: 5400,
    following: 120,
    avatarUrl: 'https://i.pravatar.cc/150?u=3',
    coverUrl: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1000&auto=format&fit=crop'
  }
];

const seedPosts = [
  {
    id: '1',
    content: "Just started learning React and Vite! 🚀 It's amazing how fast the development experience is compared to Create React App. Highly recommend giving it a try if you haven't already.",
    author: seedUsers[0],
    createdAt: new Date(Date.now() - 2 * 3600000).toISOString(),
    likes: 42,
    likedBy: [],
    comments: 5,
    shares: 2,
  },
  {
    id: '2',
    content: "Building a modern social media frontend today. The combination of Tailwind CSS and Lucide icons makes it so easy to create beautiful, responsive UIs quickly. ✨",
    author: seedUsers[1],
    createdAt: new Date(Date.now() - 4 * 3600000).toISOString(),
    likes: 128,
    likedBy: [],
    comments: 12,
    shares: 8,
  },
  {
    id: '3',
    content: "What's everyone's favorite state management library for React in 2026? I've been using Zustand lately and it's incredibly simple and powerful without the boilerplate of Redux.",
    author: seedUsers[2],
    createdAt: new Date(Date.now() - 5 * 3600000).toISOString(),
    likes: 85,
    likedBy: [],
    comments: 34,
    shares: 1,
  }
];

export const initializeStorage = () => {
  if (!localStorage.getItem(USERS_KEY)) {
    localStorage.setItem(USERS_KEY, JSON.stringify(seedUsers));
  }
  if (!localStorage.getItem(POSTS_KEY)) {
    localStorage.setItem(POSTS_KEY, JSON.stringify(seedPosts));
  }
};

export const getStorageData = (key) => {
  const data = localStorage.getItem(key);
  return data ? JSON.parse(data) : [];
};

export const setStorageData = (key, data) => {
  localStorage.setItem(key, JSON.stringify(data));
};

export const getUsers = () => getStorageData(USERS_KEY);
export const setUsers = (users) => setStorageData(USERS_KEY, users);

export const getPostsData = () => getStorageData(POSTS_KEY);
export const setPostsData = (posts) => setStorageData(POSTS_KEY, posts);

// Initialize on import
initializeStorage();
