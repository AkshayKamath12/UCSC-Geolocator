import React, { useState, useRef, useEffect } from 'react';
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
  file
}) {
  const [preview, setPreview] = useState(null);
  const previewRef = useRef(null);

  const handleImageChange = async (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  useEffect(() => {
    if (preview && previewRef.current) {
      const element = previewRef.current;
      const offset = element.getBoundingClientRect().top + window.pageYOffset - (window.innerHeight / 2) + (element.clientHeight / 2);
      window.scrollTo({ top: offset, behavior: 'smooth' });
    }
  }, [preview]);

  const handleImageSubmit = async () => {
    if (file) {
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
        <div className={styles.previewContainer} ref={previewRef}>
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
