# importing libraries
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os


try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")


def detect(image):

    faces = face_cascade.detectMultiScale(
        image=image, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img=image, pt1=(x, y), pt2=(
            x + w, y + h), color=(255, 0, 0), thickness=2)

    # Returning the image with bounding boxes drawn on it (in case of detected objects), and faces array
    return image, faces


# Here is the function for UI
def main():
    st.title("Face Detection App")
    st.write("**Using the Haar cascade Classifiers**")
    st.write("--Use operations in the side bar")

    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("**These are the functions by the our application : ** ")
    st.sidebar.write("")

    activities = ["Home", "Upload and display pic",
                  "Face detection in pic", "Face detection cam"]
    choice = st.sidebar.selectbox("select an option", activities)

    if choice == "Home":
        image = Image.open('DP.png')
        image = image.resize((400, 400))
        st.image(image, caption='an application by Gunashekar.CH')

    if choice == "Upload and display pic":
        image_file = st.file_uploader(
            "Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

        if image_file is not None:

            image = Image.open(image_file)
            if st.button("Process"):
               # image = image.resize((500,500))
                st.image(image, use_column_width="auto")

    if choice == "Face detection in pic":
        image_file = st.file_uploader(
            "Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

        if image_file:

            image = Image.open(image_file)

            if st.button("Process"):

                # result_img is the image with rectangle drawn on it (in case there are faces detected)
                # result_faces is the array with co-ordinates of bounding box(es)
                image = np.array(image.convert('RGB'))
                result_img, result_faces = detect(image=image)
                st.image(result_img, use_column_width=True)
                st.success("Found {} faces\n".format(len(result_faces)))

    if choice == "Face detection cam":

        st.header("Webcam Live Feed")
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)
        while run:
            # Reading image from video stream
            _, img = camera.read()
            # Call method we defined above
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img, a = detect(img)
           # st.image(img, use_column_width=True)
            FRAME_WINDOW.image(img)
        else:
            st.write('Stopped')


if __name__ == "__main__":
    main()
