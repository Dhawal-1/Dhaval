import streamlit as st
import io
from PIL import Image

import requests

API_URL = "https://api-inference.huggingface.co/models/artificialguybr/StickersRedmond"
headers = {"Authorization": f'Bearer {st.secrets["API_KEY"]}'}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def genrate_image(prompt):
    image_bytes = query({
        "inputs": prompt,
        
    })
    return Image.open(io.BytesIO(image_bytes))

prompt = st.text_input("Enter the text to genrate image")

if st.button('Genrate Images'):
      with st.spinner('Wait for it...'):
        st.image(genrate_image(prompt))
             