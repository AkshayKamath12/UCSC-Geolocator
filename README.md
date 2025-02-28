# How to use app:


## Backend server:

1) Open one terminal and go to the server directory.
2) Do ```python -m venv myenv```
3) On windows, do ```myenv/scripts/activate```
4) Install dependencies through ```pip install -r requirements.txt```
5) Run ```python model.py``` and make sure geolocator.keras is created in the server directory
6) Create a folder called **upload** in **server/images** (this is just for temporarily storing uploaded photos)
6) Run Flask server through ```python main.py```

## Frontend server:

1) Open a new terminal and go to the client directory
2) Install the latest node version if you haven't already done so
3) Do ```npm install```
4) Do ```npm run start```
5) This should open a new tab in your browser.
6) Add an image and click upload.

**View the predicted coordinates in the terminal for the Flask server or the console window.**