# main.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
import csv
from model import create_model, predict_coordinates

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load image paths and coordinates from CSV
def load_image_paths_and_coordinates(csv_file_path):
    image_paths = []
    coordinates = []

    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_paths.append(row['image_path'])
            coordinates.append((float(row['latitude']), float(row['longitude'])))

    return image_paths, coordinates

csv_file_path = 'image_coordinates.csv'
image_paths, coordinates = load_image_paths_and_coordinates(csv_file_path)

# Initialize model
model = create_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        coordinates = predict_coordinates(model, filepath)
        return jsonify({'message': 'File uploaded successfully', 'file_path': filepath, 'coordinates': coordinates})

@app.route('/api/images', methods=['POST'])
def receive_and_process_images():
    # Here you can add any additional processing logic for the uploaded images
    return jsonify({'message': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
