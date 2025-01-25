from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/api/images", methods=["POST"])

def receive_and_process_images():
    return jsonify({'message': 'success'})

if __name__ == "__main__":
    app.run(debug=True, port=8080)