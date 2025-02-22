from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import tempfile
import tensorflow as tf
from tensorflow import keras
import numpy as np
from model import Geolocator

app = Flask(__name__)
CORS(app)
allowed_extensions = {"png", "jpg"}
min_lat = 36.999301
max_lat = 37.000198
min_lon = -122.064474
max_lon = -122.061568

model = Geolocator(use_trained=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    
    if 'image' not in request.files:
        return jsonify({'error': 'No file'}), 400
    
    file = request.files['image']
    
    if file and allowed(file.filename):
        filename, extension = file.filename.split('.')
        new_filename = generate_temp_upload_filename(filename, "." + extension)  
        print(new_filename)
        file.save(os.path.join('images/upload', new_filename))
        predict_coords, _ = model.predict(new_filename, 1)
        os.remove(new_filename)
        return jsonify({'prediction': predict_coords[0].tolist()}), 200
    else:
        return jsonify({'error': 'Invalid file'}), 400
    
def allowed(file_name):
    res = file_name.split('.')
    return True if len(res) == 2 and res[1] in allowed_extensions else False

def generate_temp_upload_filename(filename, extension):
    tmp_file = tempfile.NamedTemporaryFile(delete=False, dir="images/upload", prefix=filename, suffix=extension)
    return tmp_file.name

def denormalize_predicted_coordinates(coords, min_latitude, max_latitude, min_longitude, max_longitude):
    lat = coords[:, 0] * (max_latitude - min_latitude) + min_latitude
    lon = coords[:, 1] * (max_longitude - min_longitude) + min_longitude
    return np.stack([lat, lon], axis=1)

if __name__ == "__main__":
    app.run(debug=True, port=8080)