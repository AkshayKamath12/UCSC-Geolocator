import React from 'react';
import Header from './Header';
import styles from './BuildingBlocksContent.module.css';

const BuildingBlocksContent = () => {
  return (
    <div className={styles.container}>
      <Header />
    </div>
  );
};

export default BuildingBlocksContent;