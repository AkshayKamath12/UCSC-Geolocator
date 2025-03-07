import React from 'react';
import Header from './Header';
import styles from './BuildingBlocksContent.module.css';

const BuildingBlocksContent = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.container}>
        <Header />
      </div>
    </div>
  );
};

export default BuildingBlocksContent;