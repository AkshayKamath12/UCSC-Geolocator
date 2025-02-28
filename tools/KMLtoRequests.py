import xml.etree.ElementTree as ET
import os

def extract_coordinates_from_kml(kml_path):
    """Extract coordinates from KML file and return list of (lat, lon) pairs"""
    tree = ET.parse(kml_path)
    root = tree.getroot()
    
    # KML uses namespace, need to handle in finding elements
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
    
    # Find all coordinate elements
    coord_elements = root.findall('.//kml:coordinates', namespace)
    
    coordinates = []
    for element in coord_elements:
        # Split coordinates string into individual points
        points = element.text.strip().split()
        for point in points:
            # KML format is longitude,latitude,altitude
            # We need latitude,longitude
            lon, lat, *_ = point.split(',')
            coordinates.append(f"{lat},{lon}")
    
    return coordinates

def append_to_requests(coordinates, requests_path):
    """Append coordinates to Requests.txt file with proper formatting"""
    # Ensure we're not adding duplicates
    existing_coords = set()
    if os.path.exists(requests_path):
        with open(requests_path, 'r') as f:
            existing_coords = set(f.read().splitlines())
    
    # Only add new coordinates
    new_coords = set(coordinates) - existing_coords
    
    if new_coords:
        # Check if file exists and has content
        needs_newline = False
        if os.path.exists(requests_path) and os.path.getsize(requests_path) > 0:
            with open(requests_path, 'rb') as f:
                f.seek(0, 2)  # Go to end of file
                if f.tell() > 0:  # If file is not empty
                    f.seek(-1, 2)  # Go to last character
                    needs_newline = f.read(1) != b'\n'
        
        # Append the new coordinates
        with open(requests_path, 'a') as f:
            if needs_newline:
                f.write('\n')
            for coord in new_coords:
                f.write(f"{coord}\n")
        print(f"Added {len(new_coords)} new coordinates to Requests.txt")
    else:
        print("No new coordinates to add")

def process_kml_files():
    """Process all KML files in the input directory"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    requests_path = os.path.join(script_dir, 'Requests.txt')
    
    # Create input directory if it doesn't exist
    os.makedirs(input_dir, exist_ok=True)
    
    # Process all KML files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.kml'):
            kml_path = os.path.join(input_dir, filename)
            coordinates = extract_coordinates_from_kml(kml_path)
            append_to_requests(coordinates, requests_path)

if __name__ == '__main__':
    process_kml_files()