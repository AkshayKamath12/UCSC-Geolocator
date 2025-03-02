import tensorflow as tf
import numpy as np
import os
import re
from geopy.distance import geodesic as GD


########
# Parameters to set
keras_file = "geolocator.keras" #name of keras file to read model from
directory = "test" #folder for reading testing data
test_count = 10 # number of images to test, set to None if you want all files
########

min_lat = 36.97721
max_lat = 37.0033005
min_lon = -122.0717714
max_lon = -122.04819

def denormalize_coordinates(coords):
    lat = coords[:, 0] * (max_lat - min_lat) + min_lat
    lon = coords[:, 1] * (max_lon - min_lon) + min_lon
    return np.stack([lat, lon], axis=1)

# parse images and their coords
test_images = []
test_coords = []
for filepath in os.listdir(directory):
  image = tf.keras.utils.load_img(os.path.join(directory, filepath), target_size=(224,224))
  image = tf.keras.utils.img_to_array(image) / 255.0
  name = re.sub(r'[$]', '_', filepath)
  coord = name.split('_')
  lat, lon = float(coord[0]), float(coord[1])
  test_coords.append((lat, lon))
  test_images.append(image)
  if test_count and len(test_images) == test_count:
     break
test_images = np.array(test_images)

# run model with test images
model = tf.keras.models.load_model(keras_file)
predicted_coords = denormalize_coordinates(model.predict(test_images))

# calc and print out error in ft
total_error = sum(GD(predicted_coords[i], test_coords[i]).feet for i in range(len(test_images)))
average_error = total_error / len(test_images)
print(f"Average error for {test_count} images: {average_error} ft")