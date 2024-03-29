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

    st.sidebar.write("These are the functions by the our application :")

    activities = ["Face detection in pic"]
    choice = st.sidebar.selectbox("select an option", activities)

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


if __name__ == "__main__":
    main()
