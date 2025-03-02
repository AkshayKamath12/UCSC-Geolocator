import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIconPng from "leaflet/dist/images/marker-icon.png";
import styles from './MapDisplay.module.css';

// uses leaflet to display coordinates on a map
function MapDisplay({ coordinates, landmarks, center }) {
  
  // predicted coord marker icon parameters
  const location_icon = new Icon({
    iconUrl: markerIconPng,
    iconSize: [17, 30],
    iconAnchor: [9, 30]
  });

  // landmark marker icon parameters
  const landmark_icon = new Icon({
    iconUrl: markerIconPng,
    iconSize: [12, 20],
    iconAnchor: [7, 20]
  });

  if (coordinates.length > 0 && center.length > 0) {
    return (
      <div className={styles.mapDisplay}>
        <h2>Map Preview:</h2>
        <div>coordinates: {coordinates[0]}, {coordinates[1]}</div>
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
          <Marker position={coordinates} icon={location_icon}>
            <Popup>coordinates: {coordinates[0]}, {coordinates[1]}</Popup>
          </Marker>
          {Object.entries(landmarks).map(([id, marker]) => (
            <Marker key={id} position={marker[0]} icon={landmark_icon}>
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