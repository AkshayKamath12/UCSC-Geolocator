import React, { useState } from 'react';
import ImageDisplay from './ImageDisplay';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';

function App() {
  const [coordinates, setCoordinates] = useState([]);

  if (coordinates.length > 0) {
    console.log(coordinates);
  }

  return (
    <div className="App">
      <header className="App-header">
        <BuildingBlocksContent />
        <HeroActions
          buttonGroupAlign="center"
          buttonGroupButtonClassName="button1"
          buttonGroupButtonClassNameOverride="button2"
          buttonGroupText="Paste from clipboard"
          platform="desktop"
          textContentTitleSubtitle="or click the button"
          textContentTitleTitle="Drag an image here"
        />
        <ImageDisplay setCoordinates={setCoordinates} />
      </header>
    </div>
  );
}

export default App;