# Face-Detection-streamlit-application

A project on Face Detection in a local image from PC and webcam live feed using Haarcascde frontal face classifier. Used OpenCV library for the over operations on the image data and streamlit for building web application. Deployed at Heroku server but have issues on webcam from the streamlit side(Streamlit doesn’t currently have any browser-based camera support).


## Description:
The app consists of sidebar with dropdown of options such as Home, Upload and Display, Face Detection in pic and Face Detection cam. 
+ Home : Diplays the admin picture and application objective
+ Upload and Display: Asks to upload pic from the local files and display it.
+ Face Detection in pic: Asks to upload pic from local files and display it with bounding box drawn around the face if detected.
+ Face Detection cam: Asks to tick the checkbox run inorder to start the webcam for face detection on live feed. Uncheck the run to stop.

## Website link : [https://fd-live.herokuapp.com/](https://fd-live.herokuapp.com/)

## Demo video : click on the below play image
[![Face detection web  application demo](https://media.istockphoto.com/vectors/play-button-icon-vector-id1194415465?b=1&k=6&m=1194415465&s=612x612&w=0&h=-BvLXebVz1yiyj3f87KVjUNpxFAgMCFt3b-nVEwYqoA=)](https://youtu.be/doxuogSjBqc "Face detection web  application demo")

## Tech Stack:
- Language: Python
- Libraries: OpenCV, PIL
- Back-End: Streamlit
- IDE: Spyder, VS code

## How to run:
- First create a virtual environment by using this command:
- conda create -n myenv python=3.6
- Activate the environment using the below command:
- conda activate myenv
- Then install all the packages by using the following command
- pip install -r requirements.txt
- Now for the final step. Run the app
- streamlit run app.py

