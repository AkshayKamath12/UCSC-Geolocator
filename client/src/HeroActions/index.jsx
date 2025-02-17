import React, { useState } from 'react';
import styles from './HeroActions.module.css';

function HeroActions({
  buttonGroupAlign,
  buttonGroupButtonClassName,
  buttonGroupButtonClassNameOverride,
  buttonGroupText,
  platform,
  textContentTitleSubtitle,
  textContentTitleTitle,
  setCoordinates
}) {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleImageChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
      
      const imageData = new FormData();
      imageData.append('image', file);

      try {
        const response = await fetch("/upload", {
          method: 'POST',
          body: imageData
        });
        const data = await response.json();
        if (data.prediction) {
          console.log(data.prediction);
          setCoordinates(data.prediction);
        }
      } catch (err) {
        console.log(err);
      }
    }
  };

  return (
    <div className={styles.heroActions}>
      <div className={styles.textContentTitle}>
        <h1 className={styles.title}>{textContentTitleTitle}</h1>
        <p className={styles.subtitle}>{textContentTitleSubtitle}</p>
      </div>
      <div className={`${styles.buttonGroup} ${buttonGroupAlign}`}>
        <label className={`${styles.button} ${buttonGroupButtonClassName} ${buttonGroupButtonClassNameOverride}`}>
          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            style={{ display: 'none' }}
          />
          {buttonGroupText}
        </label>
      </div>
      {preview && (
        <div className={styles.previewContainer}>
          <img src={preview} alt="Preview" className={styles.previewImage} />
        </div>
      )}
    </div>
  );
}

export default HeroActions;
