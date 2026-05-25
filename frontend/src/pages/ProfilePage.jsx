import React, { useState, useEffect } from 'react';
import { Calendar, MapPin, Link as LinkIcon, Mail } from 'lucide-react';
import Avatar from '../components/ui/Avatar';
import Button from '../components/ui/Button';
import PostCard from '../components/shared/PostCard';
import useAuthStore from '../context/useAuthStore';
import { getUserProfile } from '../api/users';
import { getPosts } from '../api/posts';

const ProfilePage = () => {
  const { user: currentUser } = useAuthStore();
  const [activeTab, setActiveTab] = useState('posts');
  const [profile, setProfile] = useState(null);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // If no specific route param, default to current user or a default user
  const profileUsername = currentUser?.username || 'frontend_dev';

  const fetchData = async () => {
    setLoading(true);
    try {
      const [profileData, postsData] = await Promise.all([
        getUserProfile(profileUsername),
        getPosts(1, 10, profileUsername)
      ]);
      setProfile(profileData);
      setPosts(postsData.posts);
    } catch (error) {
      console.error('Failed to fetch profile data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [profileUsername]);

  if (loading || !profile) {
    return <div className="p-8 text-center text-gray-500">Loading profile...</div>;
  }

  const isOwnProfile = currentUser?.username === profile.username;

  return (
    <div className="w-full h-full pb-20 md:pb-0">
      {/* Header / Nav */}
      <div className="sticky top-0 z-10 bg-white/80 dark:bg-background-dark/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800 flex items-center p-2">
        <button className="p-2 mr-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors">
          <svg viewBox="0 0 24 24" aria-hidden="true" className="w-5 h-5 fill-current text-gray-900 dark:text-gray-100">
            <g><path d="M7.414 13l5.043 5.04-1.414 1.42L3.586 12l7.457-7.46 1.414 1.42L7.414 11H21v2H7.414z"></path></g>
          </svg>
        </button>
        <div>
          <h1 className="text-xl font-bold text-gray-900 dark:text-gray-100">{profile.displayName}</h1>
          <p className="text-xs text-gray-500 dark:text-gray-400">{posts.length} posts</p>
        </div>
      </div>

      {/* Cover Photo */}
      <div className="h-48 w-full bg-gray-300 dark:bg-gray-800 relative">
        {profile.coverUrl && (
          <img 
            src={profile.coverUrl} 
            alt="Cover" 
            className="w-full h-full object-cover"
          />
        )}
      </div>

      {/* Profile Info */}
      <div className="px-4 pb-4">
        <div className="flex justify-between items-start relative -mt-16">
          <div className="rounded-full p-1 bg-white dark:bg-background-dark">
            <Avatar src={profile.avatarUrl} alt={profile.displayName} size="xl" />
          </div>
          
          <div className="mt-20">
            {isOwnProfile ? (
              <Button variant="outline" className="rounded-full font-bold">
                Edit Profile
              </Button>
            ) : (
              <div className="flex gap-2">
                <button className="p-2 border border-gray-300 dark:border-gray-700 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                  <Mail size={20} className="text-gray-900 dark:text-gray-100" />
                </button>
                <Button className="rounded-full font-bold px-6">
                  Follow
                </Button>
              </div>
            )}
          </div>
        </div>

        <div className="mt-3">
          <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100">{profile.displayName}</h2>
          <p className="text-gray-500 dark:text-gray-400 text-sm">@{profile.username}</p>
        </div>

        <div className="mt-3 text-gray-900 dark:text-gray-100 whitespace-pre-wrap">
          {profile.bio || 'No bio yet.'}
        </div>

        <div className="flex flex-wrap gap-4 mt-3 text-gray-500 dark:text-gray-400 text-sm">
          {profile.location && (
            <div className="flex items-center gap-1">
              <MapPin size={16} />
              <span>{profile.location}</span>
            </div>
          )}
          {profile.website && (
            <div className="flex items-center gap-1">
              <LinkIcon size={16} />
              <a href={profile.website} target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">
                {profile.website.replace(/^https?:\/\//, '')}
              </a>
            </div>
          )}
          <div className="flex items-center gap-1">
            <Calendar size={16} />
            <span>Joined {profile.joinedAt}</span>
          </div>
        </div>

        <div className="flex gap-4 mt-3">
          <div className="cursor-pointer hover:underline">
            <span className="font-bold text-gray-900 dark:text-gray-100">{profile.following || 0}</span>
            <span className="text-gray-500 dark:text-gray-400 ml-1">Following</span>
          </div>
          <div className="cursor-pointer hover:underline">
            <span className="font-bold text-gray-900 dark:text-gray-100">{profile.followers || 0}</span>
            <span className="text-gray-500 dark:text-gray-400 ml-1">Followers</span>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex border-b border-gray-200 dark:border-gray-800 mt-2">
        {['Posts', 'Replies', 'Media', 'Likes'].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab.toLowerCase())}
            className={`flex-1 font-bold py-4 text-center hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors relative ${
              activeTab === tab.toLowerCase() 
                ? 'text-gray-900 dark:text-gray-100' 
                : 'text-gray-500 dark:text-gray-400'
            }`}
          >
            {tab}
            {activeTab === tab.toLowerCase() && (
              <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-12 h-1 bg-primary rounded-full"></div>
            )}
          </button>
        ))}
      </div>

      {/* Feed Content */}
      <div className="divide-y divide-gray-200 dark:divide-gray-800">
        {activeTab === 'posts' ? (
          posts.length > 0 ? (
            posts.map(post => (
              <PostCard key={post.id} post={post} onLike={fetchData} />
            ))
          ) : (
            <div className="p-8 text-center text-gray-500 dark:text-gray-400">
              No posts yet.
            </div>
          )
        ) : (
          <div className="p-8 text-center text-gray-500 dark:text-gray-400">
            No {activeTab} yet.
          </div>
        )}
      </div>
    </div>
  );
};

export default ProfilePage;
