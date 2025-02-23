import requests
import numpy as np

# Configuration
API_KEY = 'API_KEY_HERE'  # Replace with your API key
LATITUDE = 37.001726  # Replace with your latitude
LONGITUDE = -122.058163  # Replace with your longitude
RADIUS = 150  # Search radius in meters
OUTPUT_FILE = 'Panoramas.txt'
GRID_SIZE = 3  # Number of grid points in each direction

def get_existing_pano_ids(file_path):
    """Read existing panorama IDs from the file."""
    try:
        with open(file_path, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def get_photo_spheres(lat, lng, radius):
    """Fetch panorama data from Google Street View Metadata API."""
    url = f"https://maps.googleapis.com/maps/api/streetview/metadata?location={lat},{lng}&radius={radius}&key={API_KEY}"
    print(f"Request URL: {url}")  # Debugging line

    try:
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")  # Debugging line
        data = response.json()
        print(f"Response data: {data}")  # Debugging line

        if data.get("status") == "OK" and "pano_id" in data:
            pano_id = data.get("pano_id")
            print(f"Photo Sphere found: {pano_id}")
            return pano_id
        else:
            print("No Photo Sphere found in this area.")
            return None

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def search_grid(lat, lng, radius, grid_size):
    """Search for panorama IDs within a grid."""
    existing_pano_ids = get_existing_pano_ids(OUTPUT_FILE)
    step = radius / grid_size

    for i in range(-grid_size, grid_size + 1):
        for j in range(-grid_size, grid_size + 1):
            new_lat = lat + (i * step / 111320)  # Approximate conversion from meters to degrees
            new_lng = lng + (j * step / (111320 * abs(np.cos(np.radians(lat)))))  # Approximate conversion from meters to degrees
            pano_id = get_photo_spheres(new_lat, new_lng, radius)
            if pano_id and pano_id not in existing_pano_ids:
                with open(OUTPUT_FILE, "a") as file:
                    file.write(pano_id + "\n")
                existing_pano_ids.add(pano_id)
                print(f"Photo Sphere ID {pano_id} added to {OUTPUT_FILE}.")
            elif pano_id:
                print(f"Photo Sphere ID {pano_id} already exists in the file.")

# Run the function
search_grid(LATITUDE, LONGITUDE, RADIUS, GRID_SIZE)
