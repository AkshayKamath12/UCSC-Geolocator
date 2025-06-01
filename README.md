# How to access the deployed app: 
https://ucsc-geolocator.vercel.app/

# How to use app locally (on windows):

## Set up redis (must do this before starting Flask server)
1) Open windows powershell and do ```wsl --install```
2) For convenience do ```wsl --set-default Ubuntu``` so that you can type wsl to start up the linux environment. Follow the instructions
3) Open a code editor like VSCode and go to the server directory
4) Run ```wsl``` and paste the commands at the following url to install Redis: [Redis community edition for windows](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/)
5) Do ```sudo service redis-server start``` to initialize redis
6) Go to the redisData folder
7) Do ```redis-cli``` and copy the config information into a .env file in this folder. The env file should set HOST to localhost, DATABASE_PORT to the port shown from the command, and DATABASE_NUM to 0
8) Create a file in this folder called \_\_init\_\_.py so that Flask can recognize getNearby.py

## Backend server

1) Open a new terminal and go to the server directory.
2) Do ```python -m venv myenv```
3) Activate the virtual environment through ```myenv/scripts/activate```
4) Install dependencies through ```pip install -r requirements.txt```
5) Run ```python model.py``` and make sure geolocator.keras is created in the server directory
6) Create a folder caled **images** inside server and a folder called **upload** inside images (this is just for temporarily storing uploaded photos)
7) Run Flask server through ```python main.py```

## Frontend server

1) Open a new terminal and go to the client directory
2) Install the latest node version if you haven't already done so
3) Do ```npm install```
4) Do ```npm run start```
5) This should open a new tab in your browser.
6) Add an image and click upload.
