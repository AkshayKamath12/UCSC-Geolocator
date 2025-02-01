import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np

directory = "/images"

def load_images_coordinates(directory):
    imageFilePaths = []
    #note: file names should be in this format latitude$decimal_longitude$decimal.jpg
    imageCoordinates = []
    for file in os.listdir(directory):
        imageFilePaths.append(os.path.join(directory, file))
        coordinates = file.split('.')[0].split('_') #split into array with latitude and longitude
        longitude_str, latitude_str = coordinates[0].replace("$", "."), coordinates[1].replace("$", ".")
        imageCoordinates.append([float(longitude_str), float(latitude_str)])
    return imageFilePaths, np.array(imageCoordinates)  #tensorflow wants data as an np array

training_directory = os.path.join(directory, "train")
test_directory = os.path.join(directory, "test")

train_paths, train_coordinates = load_images_coordinates("./images/test")
test_paths, test_coordinates = load_images_coordinates("./images/train")

print(train_paths)



def data_generator(image_paths, coordinates, batch_image_size, target_img_size=(224, 224)):
    while True:
        for i in range(0, len(image_paths), batch_image_size):
            batch_paths = image_paths[i:i + batch_image_size]
            batch_coords = coordinates[i:i + batch_image_size]
            print(batch_paths)
            print(batch_coords)
            images = []
            for path in batch_paths:
                image = tf.keras.utils.load_img(path, target_size=target_img_size)
                image = tf.keras.utils.img_to_array(image) / 255.0
                images.append(image)
            yield np.array(images), np.array(batch_coords)

batch_img_size = 1
train_generator = data_generator(train_paths, train_coordinates, batch_img_size)
val_generator = data_generator(test_paths, test_coordinates, batch_img_size)


base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3), 
    include_top=False, 
    weights='imagenet'
)

base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(), #used to translate 2-d data into 1-d data
    layers.Dropout(0.2),
    layers.Dense(128, activation='relu'),
    layers.Dense(2)  #outputs latitude and longitude
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',  #mean squared error
    metrics=['mae']  #mean absolute error
)

# 4. Train the model
steps_per_epoch = len(train_paths) // 2
validation_steps = len(test_paths) // 2
print(steps_per_epoch)
print(validation_steps)
history = model.fit(
    train_generator,
    validation_data=val_generator,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    epochs=10,
    verbose=1
)

model.save("geolocator.keras")

test_model_directory = "\\images\\testModel"
#main function
def predict_coordinates(file_name):
    image_path = os.path.join(test_model_directory, file_name)
    image = tf.keras.utils.load_img(file_name, target_size=(224, 224))
    image_array = tf.keras.utils.img_to_array(image) / 255.0
    image_array = tf.expand_dims(image_array, axis=0)  
    predictions = model.predict(image_array)
    return predictions[0]  #latitude, longitude pair

print(predict_coordinates("./images/train\\37$00_-122$06.png"))