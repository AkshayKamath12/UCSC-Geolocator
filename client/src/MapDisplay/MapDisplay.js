import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import styles from './MapDisplay.module.css';
import { blueIcon } from './leaflet-color-markers-master/js/leaflet-color-markers';
import { goldIcon, greenIcon, greyIcon, orangeIcon, redIcon } from './leaflet-color-markers-master/js/leaflet-color-markers';

// uses leaflet to display coordinates on a map
function MapDisplay({ coordinates, landmarks, center }) {
  const mapRef = useRef(null);
  const LANDMARK_ICONS = [goldIcon, greenIcon, greyIcon, orangeIcon, redIcon];

  useEffect(() => {
    if (mapRef.current) {
      mapRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [coordinates, center]);

  if (coordinates.length > 0 && center.length > 0) {
    return (
      <div className={styles.mapDisplay} id="map" ref={mapRef}>
        <h2 className='text-4xl font-bold'>You Are Here:</h2>
        <div>At: {coordinates[0]} N, {Math.abs(coordinates[1])} W</div>
        <MapContainer
          key={center}
          center={center}
          zoom={17}
          className={styles.mapContainer}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          <Marker position={coordinates} icon={blueIcon}>
            <Popup>coordinates: {coordinates[0]}, {coordinates[1]}</Popup>
          </Marker>
          {Object.entries(landmarks).map(([id, marker], index) => (
            <Marker key={id} position={marker[0]} icon={LANDMARK_ICONS[index]}>
              <Popup>{marker[1].name}</Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>
    );
  } else {
    return (
      <div className={styles.mapDisplay}>
        <div className={styles.noCoordinates}>No coordinates</div>
      </div>
    );
  }
}

export default MapDisplay;