import React from 'react';

// uses leaflet to display coordinates on a map
function LandmarkDisplay({ landmarks, setCenter }) {
  const tableDataClass = "p-2 border border-black";
  const tableHeadClass = "bg-blue-100 border border-black text-center p-2";
  if (landmarks.length > 0) {
    console.log(landmarks[0][1]);
    return (
      <div className='flex flex-col justify-center h-full p-4'>
        <h2 className='text-4xl font-bold mb-[2vh] text-center'>Nearby Landmarks</h2>
        <table className='shadow-lg bg-white'>
          <thead>
            <tr>
              <td key='coordinates' className={tableHeadClass}>Coordinates</td>
              {Object.keys(landmarks[0][1]).map((col_name) => (
                  <td key={col_name} className={tableHeadClass}>{col_name}</td>
              ))}
              <td key='setCenter' className={tableHeadClass}>Button</td> 
            </tr>
          </thead>
          <tbody>
            {Object.entries(landmarks).map(([id, marker]) => (
              <tr key={id}>
                <td key='coordinates' className={tableDataClass}>{marker[0][0]}, {marker[0][1]}</td>
                {Object.entries(marker[1]).map(([id, col_name]) => (
                  <td key={id} className={tableDataClass}>{col_name}</td>
                ))}
                <td key='setCenter' className={tableDataClass}>
                  <button onClick={()=>setCenter(marker[0])} className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>
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