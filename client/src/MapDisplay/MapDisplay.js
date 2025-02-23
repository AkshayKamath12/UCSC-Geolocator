import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIconPng from "leaflet/dist/images/marker-icon.png";
import styles from './MapDisplay.module.css';

// uses leaflet to display coordinates on a map
function MapDisplay({ coordinates }) {
  // marker icon parameters
  const icon = new Icon({
    iconUrl: markerIconPng,
    iconSize: [17, 30],
    iconAnchor: [12, 30]
  });

  if (coordinates.length > 0) {
    return (
      <div className={styles.mapDisplay}>
        <h2>Map Preview:</h2>
        <div>coordinates: {coordinates[0]}, {coordinates[1]}</div>
        <MapContainer
          key={coordinates}
          center={coordinates}
          zoom={17}
          className={styles.mapContainer}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          <Marker
            position={coordinates}
            icon={icon}
          >
            <Popup>coordinates: {coordinates[0]}, {coordinates[1]}</Popup>
          </Marker>
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