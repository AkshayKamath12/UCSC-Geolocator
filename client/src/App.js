import React, { useState } from 'react';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';
import MapDisplay from './MapDisplay/MapDisplay';

function App() {
  const [coordinates, setCoordinates] = useState([]);
  const [file, setFile] = useState(null); // Add state for file

  if(coordinates.length > 0){
    console.log("sending data")
    const getData = async () => {
      try {
        await fetch('/getNearbyLocationData', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(coordinates)
        }).then(
          res =>res.json()
        ).then(
          data =>{
            console.log(data["res"])
          }
        )
      } catch (error) {
        console.error('Error sending coordinates:', error);
      }
    };

    getData()
  }

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