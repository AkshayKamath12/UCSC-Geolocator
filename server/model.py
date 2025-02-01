import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np

directory = "/images"

def load_images_coordinates(directory):
    imageFilePaths = []
    #note: file names should be in this format latitude_longitude.jpg
    imageCoordinates = []
    for file in os.listdir(directory):
        imageFilePaths.append(os.path.join(directory, file))
        coordinates = file.split('_') #split into array with latitude and longitude
        imageCoordinates.append([coordinates[0], coordinates[1]])
    return imageFilePaths, np.array(imageCoordinates)  #tensorflow wants data as an np array

training_directory = os.path.join(directory, "train")
test_directory = os.path.join(directory, "test")

train_paths, train_coordinates = load_images_coordinates(training_directory)
test_paths, test_coordinates = load_images_coordinates(test_directory)

def data_generator(image_paths, coordinates, batch_image_size, target_img_size=(224, 224)):
    while True:
        for i in range(0, len(image_paths), batch_image_size):
            batch_paths = image_paths[i:i + batch_image_size]
            batch_coords = coordinates[i:i + batch_image_size]
            images = []
            for path in batch_paths:
                image = tf.keras.utils.load_img(path, target_size=target_img_size)
                image = tf.keras.utils.img_to_array(image) / 255.0
                images.append(image)
            yield np.array(images), np.array(batch_coords)

train_generator = data_generator(train_paths, train_coordinates, 20) #setting images per batch to 20
val_generator = data_generator(test_paths, test_coordinates, 20)


base_model = tf.keras.applications.EfficientNetB0(
    include_top=False,
    input_shape=(224, 224, 3),
    weights='imagenet'
)

base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(128, activation='relu'),
    layers.Dense(2)  #outputs latitude and longitude
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',  # mean squared Error
    metrics=['mae']  # mean absolute error
)

# 4. Train the model
steps_per_epoch = len(train_paths) // 20
validation_steps = len(test_paths) // 20

history = model.fit(
    train_generator,
    validation_data=val_generator,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    epochs=10,
    verbose=1
)

model.save("geolocator.h5")

#main function
def predict_coordinates(image_path):
    image = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    image_array = tf.keras.utils.img_to_array(image) / 255.0
    image_array = tf.expand_dims(image_array, axis=0)  
    predictions = model.predict(image_array)
    return predictions[0]  #latitude, longitude pair