import React from 'react';
import styles from './Header.module.css';
import MediaImage from './Media.png';

const Header = () => {
  return (
    <div className={styles.headerContainer}>
      <div className={styles.headerContent}>
        <div className={styles.headerTextContainer}>
          <div className={styles.headerTitle}>Street View Geolocator</div>
          <div className={styles.headerSubtitle}>Powered by Google Maps™</div>
        </div>
      </div>
      <div className={styles.headerImageContainer}>
        <img className={styles.headerImage} src={MediaImage} alt="Logo" />
      </div>
    </div>
  );
};

export default Header;