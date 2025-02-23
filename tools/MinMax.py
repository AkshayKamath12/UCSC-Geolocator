import os
import re
import numpy as np

def extract_coordinates(filename):
    """Extract latitude and longitude from the filename."""
    match = re.search(r'([-+]?\d*\.\d+|\d+)_([-+]?\d*\.\d+|\d+)', filename)
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon
    return None, None

def find_min_max_coordinates(directory):
    coordinates = []
    min_lat, max_lat = float('inf'), float('-inf')
    min_lon, max_lon = float('inf'), float('-inf')
    min_lat_file, max_lat_file = None, None
    min_lon_file, max_lon_file = None, None

    print(f"Searching directory: {directory}")  # Debug print

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                print(f"Processing file: {file}")  # Debug print
                lat, lon = extract_coordinates(file)
                if lat is not None and lon is not None:
                    coordinates.append((lat, lon, file))
                    if lat < min_lat:
                        min_lat = lat
                        min_lat_file = file
                    if lat > max_lat:
                        max_lat = lat
                        max_lat_file = file
                    if lon < min_lon:
                        min_lon = lon
                        min_lon_file = file
                    if lon > max_lon:
                        max_lon = lon
                        max_lon_file = file

    return min_lat, max_lat, min_lon, max_lon, min_lat_file, max_lat_file, min_lon_file, max_lon_file, coordinates

def find_outliers(coordinates, threshold=3):
    lats = np.array([coord[0] for coord in coordinates])
    lons = np.array([coord[1] for coord in coordinates])
    
    lat_mean = np.mean(lats)
    lon_mean = np.mean(lons)
    lat_std = np.std(lats)
    lon_std = np.std(lons)
    
    outliers = []
    for lat, lon, file in coordinates:
        lat_z = (lat - lat_mean) / lat_std
        lon_z = (lon - lon_mean) / lon_std
        if abs(lat_z) > threshold or abs(lon_z) > threshold:
            outliers.append((lat, lon, file, lat_z, lon_z))
    
    return outliers

def calculate_min_max(coordinates):
    min_lat, max_lat = float('inf'), float('-inf')
    min_lon, max_lon = float('inf'), float('-inf')
    min_lat_file, max_lat_file = None, None
    min_lon_file, max_lon_file = None, None

    for lat, lon, file in coordinates:
        if lat < min_lat:
            min_lat = lat
            min_lat_file = file
        if lat > max_lat:
            max_lat = lat
            max_lat_file = file
        if lon < min_lon:
            min_lon = lon
            min_lon_file = file
        if lon > max_lon:
            max_lon = lon
            max_lon_file = file

    return min_lat, max_lat, min_lon, max_lon, min_lat_file, max_lat_file, min_lon_file, max_lon_file

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'server', 'images', 'train')
    min_lat, max_lat, min_lon, max_lon, min_lat_file, max_lat_file, min_lon_file, max_lon_file, coordinates = find_min_max_coordinates(output_dir)
    
    print("With outliers:")
    print(f"Min Latitude: {min_lat} (from file: {min_lat_file})")
    print(f"Max Latitude: {max_lat} (from file: {max_lat_file})")
    print(f"Min Longitude: {min_lon} (from file: {min_lon_file})")
    print(f"Max Longitude: {max_lon} (from file: {max_lon_file})")
    
    outliers = find_outliers(coordinates)
    if outliers:
        print("\nOutliers detected:")
        for lat, lon, file, lat_z, lon_z in outliers:
            print(f"File: {file}, Latitude: {lat} (Z-score: {lat_z}), Longitude: {lon} (Z-score: {lon_z})")
    else:
        print("\nNo outliers detected.")
    
    # Remove outliers from coordinates
    coordinates_without_outliers = [coord for coord in coordinates if coord not in [(lat, lon, file) for lat, lon, file, lat_z, lon_z in outliers]]
    
    min_lat_wo, max_lat_wo, min_lon_wo, max_lon_wo, min_lat_file_wo, max_lat_file_wo, min_lon_file_wo, max_lon_file_wo = calculate_min_max(coordinates_without_outliers)
    
    print("\nWithout outliers:")
    print(f"Min Latitude: {min_lat_wo} (from file: {min_lat_file_wo})")
    print(f"Max Latitude: {max_lat_wo} (from file: {max_lat_file_wo})")
    print(f"Min Longitude: {min_lon_wo} (from file: {min_lon_file_wo})")
    print(f"Max Longitude: {max_lon_wo} (from file: {max_lon_file_wo})")