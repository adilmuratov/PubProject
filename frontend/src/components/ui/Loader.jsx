import React from 'react';
import { Loader2 } from 'lucide-react';

const Loader = ({ className, size = 24 }) => {
  return (
    <div className={`flex items-center justify-center ${className || ''}`}>
      <Loader2 size={size} className="animate-spin text-primary" />
    </div>
  );
};

export default Loader;
