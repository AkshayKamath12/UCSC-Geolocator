import ImageDisplay from './ImageDisplay';
import MapDisplay from './mapDisplay';
import { useState } from 'react';

function App() {
  const [coordinates, setCoordinates] = useState([]);  

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
        <ImageDisplay setCoordinates={setCoordinates}/>
        <MapDisplay coordinates={coordinates}/>
      </header>
    </div>
  );
}

export default App;