import redis
from dotenv import load_dotenv
import json
import os
import heapq

load_dotenv()

r = redis.Redis(host=os.getenv('HOST'), port=int(os.getenv('DATABASE_PORT')), db=int(os.getenv('DATABASE_NUM')))

#each JSON stores the coordinate and additional information about the building/landmark
#we need to properly fill this out

json_data = [
    {
        'coordinate': (36.9979, -122.0612),
        'description': "test descr 1"
    },

    {
        'coordinate': (36.9996, -121.9731),
        'description': "test descr 2"
    },

    {
        'coordinate': (37.0010, -122.0305),
        'description': "test descr 3"
    },
]

#parses JSON data above, stores data in Redis, and returns an array of all the coordinates as tuples
def set_data():
    arr = []
    for json_location in json_data:
        key = json_location['coordinate']
        arr.append(key)
        val_description = json_location['description']
        store_data = {
            "description": val_description
        }
        r.set(str(key), json.dumps(store_data))
    return arr

#uses a minheap to store and return the "coordinates_requested" closest coordinates to the predicted coordinate
def find_closest_coordinates(coordinate, coordinates, coordinates_requested=10):
    heap = []

    for coordinate2 in coordinates:
        dist = calculate_distance(coordinate, coordinate2)
        heapq.heappush(heap, (dist, coordinate2))

    res = []

    for _ in range(coordinates_requested):
        res.append(heapq.heappop(heap))

    return res

#simple helper function to get the distance between coordinates
def calculate_distance(coordinate, coordinate2):
    return (coordinate[0] - coordinate2[0]) ** 2 + (coordinate[1] - coordinate2[1]) ** 2

#gets the JSON data for a given building/landmark coordinate
def get_data_from_redis(coordinate):
    return json.loads(r.get(str(coordinate)))

#simple test to see if redis is properly configured and methods are working for you
if __name__ == "__main__":
    res = set_data()
    print(f'coordinates = {res}')
    coordinateInp = (36.9978, -121.9729)
    res2 = find_closest_coordinates(coordinateInp, res, 1)
    print(f"closest coordinate to {coordinateInp} is {res2[0][1]}")
    res3 = get_data_from_redis(res2[0][1])
    print(f"data for {coordinateInp} = {res3}")