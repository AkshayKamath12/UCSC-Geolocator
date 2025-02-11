import aiohttp
import asyncio
import aiofiles
import os
from urllib.parse import urlencode

async def fetch_image(session, url, output_path):
    """Fetch a single image asynchronously"""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                async with aiofiles.open(output_path, 'wb') as f:
                    await f.write(content)
                print(f'Saved {output_path}')
                return True
            else:
                print(f'Error fetching image: {response.status}')
                return False
    except Exception as e:
        print(f'Error: {str(e)}')
        return False

async def fetch_streetview_images(api_key, size="600x300", fov=90, heading=0, pitch=0):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    requests_file = os.path.join(script_dir, 'Requests.txt')
    base_url = "https://maps.googleapis.com/maps/api/streetview?"

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

    # Read coordinates
    with open(requests_file, 'r') as f:
        locations = f.readlines()

    # Create output directory
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Create tasks list for all requests
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for loc in locations:
            lat, lon = map(float, loc.strip().split(','))
            
            for direction, heading in cardinal_directions.items():
                params = {
                    'size': size,
                    'location': f'{lat},{lon}',
                    'fov': fov,
                    'key': api_key,
                    'heading': heading,
                    'pitch': pitch
                }
                
                url = base_url + urlencode(params)
                filename = os.path.join(output_dir, f'{lat}_{lon}_{direction}.jpg')
                
                # Add task to list
                tasks.append(fetch_image(session, url, filename))
        
        # Execute all tasks concurrently
        results = await asyncio.gather(*tasks)
    
    # Print summary
    successful = sum(1 for r in results if r)
    print(f'\nCompleted: {successful}/{len(tasks)} images downloaded successfully')

if __name__ == '__main__':
    API_KEY = 'API_KEY'
    
    # Run the async function
    asyncio.run(fetch_streetview_images(API_KEY))