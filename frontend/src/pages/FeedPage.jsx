import React, { useState, useEffect } from 'react';
import CreatePost from '../components/shared/CreatePost';
import PostCard from '../components/shared/PostCard';
import { getPosts } from '../api/posts';

const FeedPage = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchPosts = async () => {
    try {
      const data = await getPosts();
      setPosts(data.posts);
    } catch (error) {
      console.error('Failed to fetch posts:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="w-full h-full">
      {/* Header */}
      <div className="sticky top-0 z-10 bg-white/80 dark:bg-background-dark/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800">
        <h1 className="text-xl font-bold p-4 text-gray-900 dark:text-gray-100">Home</h1>
      </div>
      
      <CreatePost onPostCreated={fetchPosts} />
      
      {/* Feed */}
      <div className="divide-y divide-gray-200 dark:divide-gray-800 pb-20">
        {loading ? (
          <div className="p-8 text-center text-gray-500">Loading posts...</div>
        ) : posts.length === 0 ? (
          <div className="p-8 text-center text-gray-500">No posts yet.</div>
        ) : (
          posts.map(post => (
            <PostCard key={post.id} post={post} onLike={fetchPosts} />
          ))
        )}
      </div>
    </div>
  );
};

export default FeedPage;
