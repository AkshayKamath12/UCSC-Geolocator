import React, { useState, useEffect } from 'react';

const ImageDisplay = ({ file }) => {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImageUrl(reader.result);
      };
      reader.readAsDataURL(file);
    } else {
      setImageUrl('');
    }
  }, [file]);
 
  return (
    <div>
      {imageUrl ? (
        <img src={imageUrl} alt="Preview" style={{ maxWidth: '100%', height: 'auto' }} />
      ) : (
        <p>No image selected</p>
      )}
    </div>
  );
};

export default ImageDisplay;