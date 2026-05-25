import { delay, getUsers, setUsers } from './storage';

export const getUserProfile = async (username) => {
  await delay(300);
  const users = getUsers();
  
  let user = users.find(u => u.username === username);
  if (!user) {
    user = {
      id: Date.now().toString(),
      username: username,
      displayName: username,
      avatarUrl: `https://ui-avatars.com/api/?name=${username}&background=random`,
      coverUrl: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop',
      bio: `This is a dynamically generated profile for ${username}. They are a new user to the platform.`,
      location: 'Internet',
      website: `https://${username}.com`,
      joinedAt: new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' }),
      followers: Math.floor(Math.random() * 1000),
      following: Math.floor(Math.random() * 500)
    };
    users.push(user);
    setUsers(users);
  }
  
  return user;
};

export const updateProfile = async (profileData) => {
  await delay(300);
  const users = getUsers();
  const userIndex = users.findIndex(u => u.username === profileData.username);
  
  if (userIndex === -1) {
    throw new Error('User not found');
  }
  
  users[userIndex] = { ...users[userIndex], ...profileData };
  setUsers(users);
  return users[userIndex];
};

export const followUser = async (username) => {
  await delay(300);
  return { success: true };
};

export const unfollowUser = async (username) => {
  await delay(300);
  return { success: true };
};
