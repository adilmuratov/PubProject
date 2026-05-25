import React, { useState } from 'react';
import { Image, Smile, Calendar, MapPin } from 'lucide-react';
import Avatar from '../ui/Avatar';
import Button from '../ui/Button';
import useAuthStore from '../../context/useAuthStore';
import { createPost } from '../../api/posts';

const CreatePost = ({ onPostCreated }) => {
  const { user } = useAuthStore();
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!content.trim() || loading) return;
    
    setLoading(true);
    try {
      await createPost({
        content,
        author: {
          username: user?.username || 'unknown',
          displayName: user?.displayName || 'Unknown User',
          avatarUrl: user?.avatarUrl
        }
      });
      setContent('');
      if (onPostCreated) {
        onPostCreated();
      }
    } catch (error) {
      console.error('Failed to create post:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white dark:bg-surface-dark border-b border-gray-200 dark:border-gray-800 p-4">
      <div className="flex gap-3">
        <div className="flex-shrink-0">
          <Avatar src={user?.avatarUrl} alt={user?.displayName} size="md" />
        </div>
        
        <div className="flex-1">
          <form onSubmit={handleSubmit}>
            <textarea
              className="w-full bg-transparent text-gray-900 dark:text-gray-100 text-xl placeholder-gray-500 dark:placeholder-gray-400 resize-none outline-none border-none focus:ring-0 min-h-[60px] py-2"
              placeholder="What is happening?!"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              rows={Math.max(2, content.split('\n').length)}
              disabled={loading}
            />
            
            <div className="border-t border-gray-100 dark:border-gray-800 pt-3 mt-2 flex items-center justify-between">
              <div className="flex items-center gap-1 text-primary">
                <button type="button" className="p-2 rounded-full hover:bg-primary/10 transition-colors">
                  <Image size={20} />
                </button>
                <button type="button" className="p-2 rounded-full hover:bg-primary/10 transition-colors hidden sm:block">
                  <Smile size={20} />
                </button>
                <button type="button" className="p-2 rounded-full hover:bg-primary/10 transition-colors hidden sm:block">
                  <Calendar size={20} />
                </button>
                <button type="button" className="p-2 rounded-full hover:bg-primary/10 transition-colors hidden sm:block">
                  <MapPin size={20} />
                </button>
              </div>
              
              <Button 
                type="submit" 
                disabled={!content.trim() || loading}
                isLoading={loading}
                className="rounded-full px-5 py-1.5 font-bold"
              >
                Post
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default CreatePost;
