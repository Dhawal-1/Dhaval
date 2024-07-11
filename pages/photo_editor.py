import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.page_link("./main.py",label="Go to Back")

st.write("###")

file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'],accept_multiple_files=False)

if file is not None:
    image = Image.open(file)
    st.write("###")

    image = np.array(image)

    blur_intensity = st.slider("Blur",1,99,3,2)

    if st.checkbox("Gray"):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
    if st.checkbox("Edge Detection"):
        image = cv2.Canny(image,100,100)
    
    if st.checkbox("Invert Colors"):
        image = cv2.bitwise_not(image)

    image = cv2.GaussianBlur(image,(blur_intensity,blur_intensity),0)

    st.image(image,caption="Image",use_column_width=True)
