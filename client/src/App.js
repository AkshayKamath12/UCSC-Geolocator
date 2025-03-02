import React, { useState, useEffect } from 'react';
import BuildingBlocksContent from './BuildingBlocksContent/BuildingBlocksContent';
import HeroActions from './HeroActions';
import MapDisplay from './MapDisplay/MapDisplay';
import LandmarkDisplay from './LandmarkDisplay/LandmarkDisplay'

function App() {
  const [coordinates, setCoordinates] = useState([]);
  const [file, setFile] = useState(null); // Add state for file
  const [landmarks, setLandmarks] = useState([]) // stores info about landmarks
  const [center, setCenter] = useState([]) // coord of center of map

  useEffect(() => {
    const getLandmarkData = async () => {
      try {
        await fetch('/getNearbyLocationData', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(coordinates)
        }).then(
          res => res.json()
        ).then(
          data => {
            setLandmarks(data.res)
          }
        )
      } catch (error) {
        console.error('Error getting landmark data:', error);
      }
    };
    if(coordinates.length > 0){  
      getLandmarkData()
      setCenter(coordinates)
    }
    
  }, [coordinates]);
  

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
        <MapDisplay coordinates={coordinates} landmarks={landmarks} center = {center}/>
        <LandmarkDisplay landmarks={landmarks} setCenter={setCenter}/>
      </header>
    </div>
  );
}
export default App;