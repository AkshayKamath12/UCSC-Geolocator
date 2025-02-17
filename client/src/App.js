import ImageDisplay from './ImageDisplay';
import MapDisplay from './mapDisplay';
import { useState } from 'react';

function App() {
  const [coordinates, setCoordinates] = useState([]);  

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