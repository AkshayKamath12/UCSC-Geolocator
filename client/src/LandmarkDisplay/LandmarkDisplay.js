import React, { useState } from 'react';
import styles from './LandmarkDisplay.module.css';

function LandmarkDisplay({ landmarks, setCenter }) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const colorClasses = [styles.buttonYellow, styles.buttonGreen, styles.buttonGray, styles.buttonGold, styles.buttonRed];

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % landmarks.length);
  };

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + landmarks.length) % landmarks.length);
  };

  if (landmarks.length > 0) {
    const marker = Object.entries(landmarks)[currentIndex];
    return (
      <div className={styles.container}>
        <div className={styles.header}>
          <h2 className={styles.title}>Near To You</h2>
          <p className={styles.subtitle}>Check these places out!</p>
        </div>
        <div className={styles.card} style={{
          minWidth: "25vw", 
          minHeight: "45vh",
          width: "100%",
          maxWidth: "25vw",
          padding: "1.5rem",
          display: "flex",          
          flexDirection: "column",  
          justifyContent: "space-between" 
        }}>
          <div>
            <h2 className={styles.cardTitle}>{marker[1][1].name}</h2>
            <p className={styles.description}>{marker[1][1].description}</p>
          </div>
          
          <div className={styles.buttonGroup} style={{ marginTop: "auto" }}>
            <div style={{ 
              display: 'flex', 
              justifyContent: 'center', 
              marginBottom: '0.5rem',
              width: '100%'
            }}>
              <button 
                onClick={handlePrevious} 
                className={`${styles.button} ${styles.buttonBlue}`}
                style={{ width: '30%', margin: '0 5px' }}>
                Previous
              </button>
              <button 
                onClick={handleNext} 
                className={`${styles.button} ${styles.buttonBlue}`}
                style={{ width: '30%', margin: '0 5px' }}>
                Next
              </button>
            </div>
            <button 
              onClick={() => setCenter(marker[1][0])} 
              className={`${styles.button} ${colorClasses[currentIndex % colorClasses.length]}`}
              style={{ minWidth: '30%' }}>
              Find Landmark
            </button>
          </div>
        </div>
      </div>
    );
  }

  return null;
}

export default LandmarkDisplay;