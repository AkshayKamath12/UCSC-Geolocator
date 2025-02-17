import React from 'react';
import styles from './HeroActions.module.css';

function HeroActions({
  buttonGroupAlign,
  buttonGroupButtonClassName,
  buttonGroupButtonClassNameOverride,
  buttonGroupText,
  platform,
  textContentTitleSubtitle,
  textContentTitleTitle
}) {
  return (
    <div className={styles.heroActions}>
      <div className={styles.textContentTitle}>
        <h1 className={styles.title}>{textContentTitleTitle}</h1>
        <p className={styles.subtitle}>{textContentTitleSubtitle}</p>
      </div>
      <div className={`${styles.buttonGroup} ${buttonGroupAlign}`}>
        <button className={`${styles.button} ${buttonGroupButtonClassName} ${buttonGroupButtonClassNameOverride}`}>
          {buttonGroupText}
        </button>
      </div>
    </div>
  );
}

export default HeroActions;
