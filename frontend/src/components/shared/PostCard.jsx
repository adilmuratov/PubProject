import React, { useState } from 'react';
import { Heart, MessageCircle, Share2, MoreHorizontal } from 'lucide-react';
import Avatar from '../ui/Avatar';
import { likePost } from '../../api/posts';
import useAuthStore from '../../context/useAuthStore';

const PostCard = ({ post, onLike }) => {
  const { user } = useAuthStore();
  const [isLiked, setIsLiked] = useState(post?.likedBy?.includes(user?.username) || post?.isLiked || false);
  const [likesCount, setLikesCount] = useState(post?.likes || 0);
  const [loading, setLoading] = useState(false);

  // Update local state if props change (e.g. from parent fetch)
  React.useEffect(() => {
    setIsLiked(post?.likedBy?.includes(user?.username) || post?.isLiked || false);
    setLikesCount(post?.likes || 0);
  }, [post, user]);

  const handleLike = async () => {
    if (loading) return;
    setLoading(true);
    
    // Optimistic UI update
    setIsLiked(!isLiked);
    setLikesCount(isLiked ? likesCount - 1 : likesCount + 1);
    
    try {
      await likePost(post.id, user?.username || 'unknown');
      if (onLike) {
        onLike();
      }
    } catch (error) {
      console.error('Failed to like post:', error);
      // Revert optimistic update
      setIsLiked(isLiked);
      setLikesCount(likesCount);
    } finally {
      setLoading(false);
    }
  };

  // Format date safely
  const formattedDate = React.useMemo(() => {
    if (!post?.createdAt) return 'Just now';
    try {
      const date = new Date(post.createdAt);
      // Simple relative time format
      const now = new Date();
      const diffMs = now - date;
      const diffMins = Math.round(diffMs / 60000);
      const diffHours = Math.round(diffMs / 3600000);
      const diffDays = Math.round(diffMs / 86400000);
      
      if (diffMins < 60) return `${diffMins}m`;
      if (diffHours < 24) return `${diffHours}h`;
      return `${diffDays}d`;
    } catch (e) {
      return post.createdAt;
    }
  }, [post?.createdAt]);

  return (
    <div className="bg-white dark:bg-surface-dark border-b border-gray-200 dark:border-gray-800 p-4 transition-colors hover:bg-gray-50 dark:hover:bg-gray-800/50">
      <div className="flex gap-3">
        <div className="flex-shrink-0">
          <Avatar src={post?.author?.avatarUrl} alt={post?.author?.displayName} size="md" />
        </div>
        
        <div className="flex-1 min-w-0">
          {/* Header */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-1.5 truncate">
              <span className="font-bold text-gray-900 dark:text-gray-100 truncate hover:underline cursor-pointer">
                {post?.author?.displayName || 'Unknown User'}
              </span>
              <span className="text-gray-500 dark:text-gray-400 text-sm truncate">
                @{post?.author?.username || 'unknown'}
              </span>
              <span className="text-gray-500 dark:text-gray-400 text-sm">·</span>
              <span className="text-gray-500 dark:text-gray-400 text-sm hover:underline cursor-pointer">
                {formattedDate}
              </span>
            </div>
            
            <button className="text-gray-500 hover:text-primary dark:text-gray-400 dark:hover:text-primary transition-colors p-2 -mr-2 rounded-full hover:bg-primary/10">
              <MoreHorizontal size={18} />
            </button>
          </div>
          
          {/* Content */}
          <div className="mt-1 text-gray-900 dark:text-gray-100 whitespace-pre-wrap break-words">
            {post?.content || 'No content provided.'}
          </div>
          
          {/* Actions */}
          <div className="flex items-center justify-between mt-3 max-w-md">
            <button className="flex items-center gap-2 text-gray-500 dark:text-gray-400 hover:text-blue-500 transition-colors group">
              <div className="p-2 rounded-full group-hover:bg-blue-500/10 transition-colors">
                <MessageCircle size={18} />
              </div>
              <span className="text-sm">{post?.comments || 0}</span>
            </button>
            
            <button 
              onClick={handleLike}
              disabled={loading}
              className={`flex items-center gap-2 transition-colors group ${isLiked ? 'text-pink-500' : 'text-gray-500 dark:text-gray-400 hover:text-pink-500'}`}
            >
              <div className="p-2 rounded-full group-hover:bg-pink-500/10 transition-colors">
                <Heart size={18} className={isLiked ? 'fill-current' : ''} />
              </div>
              <span className="text-sm">{likesCount}</span>
            </button>
            
            <button className="flex items-center gap-2 text-gray-500 dark:text-gray-400 hover:text-green-500 transition-colors group">
              <div className="p-2 rounded-full group-hover:bg-green-500/10 transition-colors">
                <Share2 size={18} />
              </div>
              <span className="text-sm">{post?.shares || 0}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PostCard;
