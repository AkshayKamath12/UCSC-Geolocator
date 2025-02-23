import os
import re

def extract_coordinates(filename):
    """Extract latitude and longitude from the filename."""
    match = re.search(r'([-+]?\d*\.\d+|\d+)_([-+]?\d*\.\d+|\d+)', filename)
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon
    return None, None

def find_min_max_coordinates(directory):
    min_lat, max_lat = float('inf'), float('-inf')
    min_lon, max_lon = float('inf'), float('-inf')
    min_lat_file, max_lat_file = None, None
    min_lon_file, max_lon_file = None, None

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                lat, lon = extract_coordinates(file)
                if lat is not None and lon is not None:
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
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    min_lat, max_lat, min_lon, max_lon, min_lat_file, max_lat_file, min_lon_file, max_lon_file = find_min_max_coordinates(output_dir)
    
    print(f"Min Latitude: {min_lat} (from file: {min_lat_file})")
    print(f"Max Latitude: {max_lat} (from file: {max_lat_file})")
    print(f"Min Longitude: {min_lon} (from file: {min_lon_file})")
    print(f"Max Longitude: {max_lon} (from file: {max_lon_file})")