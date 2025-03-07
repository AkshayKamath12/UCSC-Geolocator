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
  setCoordinates,
  setFile,
  file // Add file prop
}) {
  const [preview, setPreview] = useState(null);
  const [isDragOver, setIsDragOver] = useState(false);

  const handleImageChange = async (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = () => {
    setIsDragOver(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragOver(false);
    const selectedFile = e.dataTransfer.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  const handleImageSubmit = async () => {
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
  };

  return (
    <div
      className={`${styles.heroActions} ${isDragOver ? styles.dragover : ''}`}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
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
        <div className={styles.previewContainer} id="submit">
          <img src={preview} alt="Preview" className={styles.previewImage} />
          <div className={`${styles.buttonGroup} ${buttonGroupAlign}`}>
            <button
              className={`${styles.button} ${buttonGroupButtonClassName} ${buttonGroupButtonClassNameOverride}`}
              onClick={handleImageSubmit}
            >
              Submit Image
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default HeroActions;
