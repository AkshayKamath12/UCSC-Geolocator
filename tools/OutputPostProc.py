import os
import re

def load_coordinates(file_path):
    """Load panorama coordinates from the file and return a dictionary mapping pano_id to (lat, lon)."""
    coordinates = {}
    seen_coordinates = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                pano_id, lat, lon = parts[0], parts[1], parts[2]
                coordinates[pano_id] = (lat, lon)
                coord_key = (lat, lon)
                if coord_key in seen_coordinates:
                    seen_coordinates[coord_key].append(pano_id)
                else:
                    seen_coordinates[coord_key] = [pano_id]
    return coordinates, seen_coordinates

def increment_latitude(lat, increment):
    """Increment the least significant digit of the latitude by a given increment."""
    lat_parts = lat.split('.')
    if len(lat_parts) == 2:
        lat_parts[1] = str(int(lat_parts[1]) + increment)
        return '.'.join(lat_parts)
    return lat

def rename_images(output_dir, coordinates, seen_coordinates):
    """Rename images in the output directory based on the coordinates dictionary."""
    original_files = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            parts = filename.rsplit('_', 1)
            if len(parts) == 2:
                pano_id, direction = parts[0], parts[1].replace('.jpg', '')
                if pano_id in coordinates:
                    lat, lon = coordinates[pano_id]
                    coord_key = (lat, lon)
                    increment = seen_coordinates[coord_key].index(pano_id)
                    if increment > 0:
                        lat = increment_latitude(lat, increment)
                    new_filename = f"{lat}_{lon}_{direction}.jpg"
                    old_path = os.path.join(output_dir, filename)
                    new_path = os.path.join(output_dir, new_filename)
                    
                    # Handle file name conflicts by incrementing latitude
                    while os.path.exists(new_path):
                        increment += 1
                        lat = increment_latitude(lat, increment)
                        new_filename = f"{lat}_{lon}_{direction}.jpg"
                        new_path = os.path.join(output_dir, new_filename)
                    
                    os.rename(old_path, new_path)
                    original_files.append(old_path)
                    print(f"Renamed {filename} to {new_filename}")

    # Delete original files after renaming
    for file in original_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted original file {file}")

def check_filenames(output_dir):
    """Check that every file follows the latitude_longitude_direction.jpg format."""
    pattern = re.compile(r'^-?\d+\.\d+_-?\d+\.\d+_[A-Z]+\.jpg$')
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            if not pattern.match(filename):
                print(f"File {filename} does not follow the expected format.")

if __name__ == '__main__':
    # Configuration
    COORDINATES_FILE = 'PanoramaCoordinates.txt'
    OUTPUT_DIR = 'output'

    # Load coordinates
    coordinates, seen_coordinates = load_coordinates(COORDINATES_FILE)

    # Rename images
    rename_images(OUTPUT_DIR, coordinates, seen_coordinates)

    # Check filenames
    check_filenames(OUTPUT_DIR)