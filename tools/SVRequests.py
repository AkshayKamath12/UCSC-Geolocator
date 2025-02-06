import requests
import os
from urllib.parse import urlencode

def fetch_streetview_images(api_key, size="600x300", fov=90, heading = 0, pitch = 15):
    # Base URL for Street View API
    base_url = "https://maps.googleapis.com/maps/api/streetview?"

    # Define cardinal directions and their degree values
    cardinal_directions = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315
    }
    
    # Read coordinates from file
    with open('Requests.txt', 'r') as f:
        locations = f.readlines()
    
    for loc in locations:
        # Parse lat,long from line
        lat, lon = map(float, loc.strip().split(','))
        
        # For each location, get images for all cardinal directions
        for direction, heading in cardinal_directions.items():
            # Construct parameters
            params = {
                'size': size,
                'location': f'{lat},{lon}',
                'fov': fov,
                'key': api_key,
                'heading': heading,
                'pitch': pitch
            }
            
            # Build full URL
            url = base_url + urlencode(params)
            
            # Send request
            response = requests.get(url)
            
            if response.status_code == 200:
                # Save image with cardinal direction in filename
                filename = f'{lat}_{lon}_{direction}.jpg'
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f'Saved {filename}')
            else:
                print(f'Error fetching image for {lat},{lon} heading {direction}: {response.status_code}')

if __name__ == '__main__':
    API_KEY = 'Your-Api-Key-Here'
    fetch_streetview_images(API_KEY)