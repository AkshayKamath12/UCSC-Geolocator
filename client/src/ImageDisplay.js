import React, { useState } from 'react';

function ImageDisplay({setCoordinates}) {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    console.log(file)
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const uploadImage = async () => {
    if (image){
      console.log(image)
      const imageData = new FormData();
      imageData.append('image', image)

      try {
        await fetch("/upload", {
            method: 'POST',
            body: imageData
        }).then(
            res => res.json()
        ).then(
            data =>{
              if(data.prediction){
                console.log(data.prediction);
                setCoordinates(data.prediction);
              }
                
            }
        )
      } catch(err){
          console.log(err)
      }
    }    
  };

  return (
    <div className="ImageDisplay">
      <h1>Upload and Display Image</h1>
      
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
      />
    
      <button onClick = {uploadImage}>
        Upload Image
      </button>

      {preview && (
        <div className="image-preview">
          <h2>Image Preview:</h2>
          <img src={preview} alt="Preview" style={{ maxWidth: '300px', marginTop: '10px' }} />
        </div>
      )}
    </div>
  );
}

export default ImageDisplay;