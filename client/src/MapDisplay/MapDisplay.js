import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIconPng from "leaflet/dist/images/marker-icon.png";
import styles from './MapDisplay.module.css';

function MapDisplay({ coordinates }) {
  useEffect(() => {
    console.log('MapDisplay coordinates:', coordinates);
  }, [coordinates]);

  if (!coordinates || coordinates.length < 2) {
    return <div>No coordinates available</div>;
  }

  const [lat, lng] = coordinates;

  // marker icon parameters
  const icon = new Icon({
    iconUrl: markerIconPng,
    iconSize: [17, 30],
    iconAnchor: [12, 30]
  });

  return (
    <div className={styles.mapDisplay}>
      <h2>Map Display</h2>
      <p>Latitude: {lat}</p>
      <p>Longitude: {lng}</p>
      <MapContainer
        key={`${lat}-${lng}`}
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
}

export default MapDisplay;