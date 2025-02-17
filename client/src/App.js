import React, { useState } from 'react';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';

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
        {/* Remove ImageDisplay component since functionality is now in HeroActions */}
      </header>
    </div>
  );
}

export default App;