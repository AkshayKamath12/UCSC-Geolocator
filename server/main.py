from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import tempfile
import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

app = Flask(__name__)
CORS(app)
allowed_extensions = {"jpg"}
min_lat = 36.97721
max_lat = 37.0033005
min_lon = -122.0717714
max_lon = -122.04819

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "geolocator.keras")

# Print the model path to verify it
print(f"Model path: {model_path}")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file'}), 400
    
    file = request.files['image']
    
    if file and allowed(file.filename):
        filename, extension = file.filename.rsplit('.', 1)
        new_filename = generate_temp_upload_filename(filename, "." + extension)  
        print(new_filename)
        file.save(os.path.join('images/upload', new_filename))
        model = keras.models.load_model("geolocator.keras")

        image = tf.keras.utils.load_img(new_filename, target_size=(224, 224))
        image_array = tf.keras.utils.img_to_array(image) / 255.0
        image_array = tf.expand_dims(image_array, axis=0)
        predictions = model.predict(image_array)
        predictions = denormalize_predicted_coordinates(predictions, min_lat, max_lat, min_lon, max_lon)[0]
        os.remove(new_filename)
        print(predictions)
        return jsonify({'prediction': predictions.tolist()}), 200
    else:
        return jsonify({'error': 'Invalid file'}), 400

def allowed(file_name):
    extension = file_name.rsplit('.', 1)[-1].lower()
    return extension in allowed_extensions

def generate_temp_upload_filename(filename, extension):
    tmp_file = tempfile.NamedTemporaryFile(delete=False, dir="images/upload", prefix=filename, suffix=extension)
    return tmp_file.name

def denormalize_predicted_coordinates(coords, min_latitude, max_latitude, min_longitude, max_longitude):
    lat = coords[:, 0] * (max_latitude - min_latitude) + min_latitude
    lon = coords[:, 1] * (max_longitude - min_longitude) + min_longitude
    return np.stack([lat, lon], axis=1)

if __name__ == "__main__":
    app.run(debug=True, port=8080)