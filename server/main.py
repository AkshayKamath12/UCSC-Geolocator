from flask import Flask, jsonify, request
from flask_cors import CORS
from model import predict_coordinates
import os

app = Flask(__name__)
CORS(app)
allowed_extensions = {"png", "jpg"}

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files or file and len(file.filename) == 0:
        return jsonify({'error': 'No file'}), 400

    file = request.files['file']

    if file and allowed(file.filename):
        filename = file.filename
        file.save(os.path.join('upload', filename))
        return jsonify({'message': 'File uploaded'}), 200
    else:
        return jsonify({'error': 'Invalid file'}), 400
    
def allowed(file_name):
    res = file_name.split('.')
    return True if len(res == 2) and res[1] in allowed_extensions else False

if __name__ == "__main__":
    app.run(debug=True, port=8080)