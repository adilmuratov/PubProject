import { delay, getPostsData, setPostsData } from './storage';

export const getPosts = async (page = 1, limit = 10, username = null) => {
  await delay(300);
  const allPosts = getPostsData();
  
  let posts = allPosts;
  if (username) {
    posts = allPosts.filter(p => p.author?.username === username);
  }
  
  // Sort posts by date descending
  posts.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
  
  // Basic pagination
  const startIndex = (page - 1) * limit;
  const paginatedPosts = posts.slice(startIndex, startIndex + limit);
  
  return {
    posts: paginatedPosts,
    total: posts.length,
    page,
    limit
  };
};

export const createPost = async (postData) => {
  await delay(300);
  const posts = getPostsData();
  
  const newPost = {
    id: Date.now().toString(),
    content: postData.content,
    author: postData.author, // assuming UI sends author object for simplicity in mock
    createdAt: new Date().toISOString(),
    likes: 0,
    likedBy: [],
    comments: 0,
    shares: 0,
  };
  
  posts.push(newPost);
  setPostsData(posts);
  return newPost;
};

export const likePost = async (postId, username) => {
  await delay(300);
  const posts = getPostsData();
  const postIndex = posts.findIndex(p => p.id === postId);
  
  if (postIndex === -1) {
    throw new Error('Post not found');
  }
  
  const post = posts[postIndex];
  post.likedBy = post.likedBy || [];
  
  const userLikedIndex = post.likedBy.indexOf(username);
  let isLiked = false;
  
  if (userLikedIndex > -1) {
    // Unlike
    post.likedBy.splice(userLikedIndex, 1);
    post.likes = Math.max(0, post.likes - 1);
  } else {
    // Like
    post.likedBy.push(username);
    post.likes += 1;
    isLiked = true;
  }
  
  posts[postIndex] = post;
  setPostsData(posts);
  
  return { ...post, isLiked };
};

export const addComment = async (postId, commentData) => {
  await delay(300);
  const posts = getPostsData();
  const postIndex = posts.findIndex(p => p.id === postId);
  
  if (postIndex === -1) {
    throw new Error('Post not found');
  }
  
  const post = posts[postIndex];
  post.comments += 1;
  
  posts[postIndex] = post;
  setPostsData(posts);
  
  return { success: true };
};
