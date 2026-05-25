import React from 'react';
import { cn } from '../../utils/cn';

const Avatar = ({ src, alt, size = 'md', className }) => {
  const sizes = {
    sm: 'w-8 h-8',
    md: 'w-10 h-10',
    lg: 'w-12 h-12',
    xl: 'w-24 h-24',
  };

  return (
    <div className={cn('relative inline-block rounded-full overflow-hidden bg-gray-200 dark:bg-gray-700', sizes[size], className)}>
      {src ? (
        <img src={src} alt={alt || 'Avatar'} className="w-full h-full object-cover" />
      ) : (
        <span className="w-full h-full flex items-center justify-center text-gray-500 dark:text-gray-400 font-semibold uppercase">
          {alt ? alt.charAt(0) : '?'}
        </span>
      )}
    </div>
  );
};

export default Avatar;
