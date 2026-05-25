import { delay, getUsers, setUsers } from './storage';

export const login = async (credentials) => {
  await delay(300);
  
  const users = getUsers();
  // Assume email or username can be passed
  const identifier = credentials.email || credentials.username || 'mock_user';
  const baseUsername = identifier.includes('@') ? identifier.split('@')[0] : identifier;
  
  let user = users.find(u => u.username === baseUsername);
  
  if (!user) {
    user = {
      id: Date.now().toString(),
      username: baseUsername,
      displayName: baseUsername,
      avatarUrl: null,
      bio: 'New user.',
      followers: 0,
      following: 0,
      joinedAt: new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' })
    };
    // Don't save auto-created users on login, just return them to simulate success.
  }

  return {
    user,
    token: 'mock-jwt-token-' + Date.now()
  };
};

export const register = async (userData) => {
  await delay(300);
  
  const users = getUsers();
  
  const identifier = userData.email || userData.username || 'new_user';
  const baseUsername = identifier.includes('@') ? identifier.split('@')[0] : identifier;
  
  const existingUser = users.find(u => u.username === baseUsername);
  if (existingUser) {
    throw new Error('User already exists');
  }

  const newUser = {
    id: Date.now().toString(),
    username: baseUsername,
    displayName: userData.name || baseUsername,
    avatarUrl: null,
    bio: 'No bio yet.',
    followers: 0,
    following: 0,
    joinedAt: new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' })
  };

  users.push(newUser);
  setUsers(users);

  return {
    user: newUser,
    token: 'mock-jwt-token-' + Date.now()
  };
};

export const getMe = async () => {
  await delay(300);
  return { user: null };
};
