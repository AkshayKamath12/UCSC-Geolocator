import requests

# Configuration
API_KEY = 'API_KEY_HERE'  # Replace with your API key
INPUT_FILE = 'Panoramas.txt'
OUTPUT_FILE = 'PanoramaCoordinates.txt'

def get_coordinates(pano_id):
    """Fetch GPS coordinates for a given panorama ID using Google Street View Metadata API."""
    url = f"https://maps.googleapis.com/maps/api/streetview/metadata?pano={pano_id}&key={API_KEY}"
    print(f"Request URL: {url}")  # Debugging line

    try:
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")  # Debugging line
        data = response.json()
        print(f"Response data: {data}")  # Debugging line

        if data.get("status") == "OK" and "location" in data:
            lat = data["location"]["lat"]
            lng = data["location"]["lng"]
            return lat, lng
        else:
            print(f"No coordinates found for panorama ID: {pano_id}")
            return None, None

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None

def extract_coordinates(input_file, output_file):
    """Extract GPS coordinates for panorama IDs in the input file and save them to the output file."""
    min_lat, max_lat = float('inf'), float('-inf')
    min_lon, max_lon = float('inf'), float('-inf')

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            pano_id = line.strip()
            if pano_id:
                lat, lng = get_coordinates(pano_id)
                if lat is not None and lng is not None:
                    outfile.write(f"{pano_id},{lat},{lng}\n")
                    print(f"Panorama ID: {pano_id}, Coordinates: ({lat}, {lng})")

                    # Update min/max latitude and longitude
                    min_lat = min(min_lat, lat)
                    max_lat = max(max_lat, lat)
                    min_lon = min(min_lon, lng)
                    max_lon = max(max_lon, lng)

        # Append min/max latitude and longitude to the file
        outfile.write(f"\nMin Latitude: {min_lat}, Max Latitude: {max_lat}\n")
        outfile.write(f"Min Longitude: {min_lon}, Max Longitude: {max_lon}\n")
        print(f"Min Latitude: {min_lat}, Max Latitude: {max_lat}")
        print(f"Min Longitude: {min_lon}, Max Longitude: {max_lon}")

# Run the function
extract_coordinates(INPUT_FILE, OUTPUT_FILE)