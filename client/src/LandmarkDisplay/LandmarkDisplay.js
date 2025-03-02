import React from 'react';

// uses leaflet to display coordinates on a map
function LandmarkDisplay({ landmarks, setCenter }) {
  if (landmarks.length > 0) {
    console.log(landmarks[0][1]);
    return (
      <div>
        <h2>Nearby Landmarks</h2>
        <table border="1" cellPadding="10">
          <thead>
            <tr>
              <td key='coordinates'>coordinates</td>
              {Object.keys(landmarks[0][1]).map((col_name) => (
                  <td key={col_name}>{col_name}</td>
              ))}
              <td key='setCenter'>button</td> 
            </tr>
          </thead>
          <tbody>
            {Object.entries(landmarks).map(([id, marker]) => (
              <tr key={id}>
                <td key='coordinates'>{marker[0][0]}, {marker[0][1]}</td>
                {Object.entries(marker[1]).map(([id, col_name]) => (
                  <td key={id}>{col_name}</td>
                ))}
                <td key='setCenter'>
                  <button onClick={()=>setCenter(marker[0])}>
                    Find Landmark
                  </button>
                </td> 
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  } else {
    return (
      <div></div>
    );
  }
}

export default LandmarkDisplay;