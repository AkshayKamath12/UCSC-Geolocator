import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
import os
import re
import numpy as np
from sklearn.model_selection import train_test_split

directory = "images/images" #directory to read training/test data from
test_size = 0.2 # % of read data reserved for validation

def load_images_coordinates(directory):
    imageFilePaths = []
    imageCoordinates = []

    min_lat, max_lat = float('inf'), float('-inf')
    min_lon, max_lon = float('inf'), float('-inf')

    for file in os.listdir(directory):
        imageFilePaths.append(os.path.join(directory, file))
        match = re.match(r'([-+]?\d*\.\d+)_([-+]?\d*\.\d+)', file)
        if not match:
            print(f"Skipping file {file} due to unexpected format")
            continue
        try:
            lat, lon = float(match.group(1)), float(match.group(2))
        except ValueError:
            print(f"Skipping file {file} due to invalid coordinate format")
            continue
        imageCoordinates.append([lat, lon])

        min_lat, max_lat = min(min_lat, lat), max(max_lat, lat)
        min_lon, max_lon = min(min_lon, lon), max(max_lon, lon)
    return imageFilePaths, np.array(imageCoordinates), (min_lat, max_lat, min_lon, max_lon)

# train_paths, train_coordinates, (min_lat, max_lat, min_lon, max_lon) = load_images_coordinates("images/train")
# test_paths, test_coordinates, _ = load_images_coordinates("images/test")

paths, coordinates, (min_lat, max_lat, min_lon, max_lon) = load_images_coordinates(directory)
train_paths, test_paths, train_coordinates, test_coordinates = train_test_split(paths, coordinates, test_size=test_size, random_state=42)


def normalize_coordinates(coords):
    lat = (coords[:, 0] - min_lat) / (max_lat - min_lat)
    lon = (coords[:, 1] - min_lon) / (max_lon - min_lon)
    return np.stack([lat, lon], axis=1)

def denormalize_coordinates(coords):
    lat = coords[:, 0] * (max_lat - min_lat) + min_lat
    lon = coords[:, 1] * (max_lon - min_lon) + min_lon
    return np.stack([lat, lon], axis=1)

train_coordinates = normalize_coordinates(train_coordinates)
test_coordinates = normalize_coordinates(test_coordinates)

def data_generator(image_paths, coordinates, batch_size, target_size=(224, 224)):
    while True:
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]
            batch_coords = coordinates[i:i + batch_size]
            images = []
            for path in batch_paths:
                image = tf.keras.utils.load_img(path, target_size=target_size)
                image = tf.keras.utils.img_to_array(image) / 255.0  
                images.append(image)
            yield np.array(images), np.array(batch_coords)

batch_size = 32
train_generator = data_generator(train_paths, train_coordinates, batch_size)
val_generator = data_generator(test_paths, test_coordinates, batch_size)

base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3), 
    include_top=False, 
    weights='imagenet'
)

base_model.trainable = True
for layer in base_model.layers[:-50]:
    layer.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.1),
    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(2, activation='sigmoid')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='mse',
    metrics=['mae']
)

epochs = 50
steps_per_epoch = len(train_paths) // batch_size
validation_steps = len(test_paths) // batch_size

history = model.fit(
    train_generator,
    validation_data=val_generator,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    epochs=epochs,
    verbose=1
)

model.save("geolocator.keras")