import React from 'react';

// uses leaflet to display coordinates on a map
function LandmarkDisplay({ landmarks, setCenter }) {
  const tableDataClass = "p-2 border border-black";
  const tableHeadClass = "bg-blue-100 border border-black text-center p-2";
  const tailwindColorClasses = ["bg-yellow-400 hover:bg-yellow-300", "bg-green-600 hover:bg-green-400", "bg-gray-400 hover:bg-gray-300", "bg-yellow-700 hover:bg-yellow-400", "bg-red-600 hover:bg-red-400"]
  if (landmarks.length > 0) {
    console.log(landmarks[0][1]);
    return (
      <div className='flex flex-col justify-center h-full p-4' style={{ borderTop: '1px solid #ccc' }}>
        <h2 className='text-4xl font-bold mb-[2vh] text-center' style={{color: '#000000'}}>Nearby Landmarks</h2>
        <table className='shadow-lg bg-white'>
          <thead>
            <tr>
              <td key='coordinates' className={tableHeadClass}>Coordinates</td>
              <td key='name' className={tableDataClass}>Name</td>
              <td key='description' className={tableDataClass}>Description</td>
              <td key='distance' className={tableDataClass}>Distance</td>
              <td key='setCenter' className={tableHeadClass}>Button</td> 
            </tr>
          </thead>
          <tbody>
            {Object.entries(landmarks).map(([id, marker], index) => (
              <tr key={id}>
                <td key='coordinates' className={tableDataClass}>{marker[0][0]}, {marker[0][1]}</td>
                <td key='name' className={tableDataClass}>{marker[1]['name']}</td>
                <td key='description' className={tableDataClass}>{marker[1]['description']}</td>
                <td key='distance' className={tableDataClass}>{marker[1]['distance']}</td>
                <td key='setCenter' className={tableDataClass}>
                  <button onClick={()=>setCenter(marker[0])} className={'text-white font-bold py-2 px-4 rounded' + ' ' + tailwindColorClasses[index]}>
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