import React, { useState, useEffect } from 'react';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';
import MapDisplay from './MapDisplay/MapDisplay';

function App() {
  const [coordinates, setCoordinates] = useState([]);
  const [file, setFile] = useState(null); // Add state for file

  useEffect(() => {
    console.log('Coordinates updated:', coordinates);
  }, [coordinates]);

  useEffect(() => {
    console.log('File updated:', file);
  }, [file]);

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
          setFile={setFile} // Pass setFile to HeroActions
          file={file} // Pass file to HeroActions
        />
        <MapDisplay coordinates={coordinates} />
      </header>
    </div>
  );
}

export default App;