import ImageDisplay from './ImageDisplay';
import { useState } from 'react';

function App() {
  const [coordinates, setCoordinates] = useState([]);
  
  if(coordinates.length > 0){
    console.log(coordinates);
  }
  

  return (
    <div className="App">
      <header className="App-header">
        <ImageDisplay setCoordinates={setCoordinates}/>
      </header>
    </div>
  );
}

export default App;