import React, { useState } from 'react';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';
import ImageDisplay from './ImageDisplay';
import MapDisplay from './MapDisplay';

function App() {
  const [coordinates, setCoordinates] = useState([]);

  return (
    <div className="App">
      <header className="App-header">
        <BuildingBlocksContent />
        <HeroActions
          buttonGroupAlign="center"
          buttonGroupButtonClassName="button1"
          buttonGroupButtonClassNameOverride="button2"
          buttonGroupText="Upload Here"
          platform="desktop"
          textContentTitleSubtitle="or click the button"
          textContentTitleTitle="Drag an image here"
          setCoordinates={setCoordinates}
        />
        <ImageDisplay setCoordinates={setCoordinates} />
        <MapDisplay coordinates={coordinates} />
      </header>
    </div>
  );
}

export default App;