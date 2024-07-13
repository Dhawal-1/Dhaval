import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np

def load_image(image_file):
    img = Image.open(image_file)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img

def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return Image.fromarray(tensor)

def load_and_process_image(image):
    img = tf.image.convert_image_dtype(image, tf.float32)
    img = tf.image.resize(img, (256, 256))
    img = img[tf.newaxis, :]
    return img

@st.cache_resource()
def load_model():
    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    return model

st.title("Neural Style Transfer")

content_image_file = st.file_uploader("Upload Content Image", type=["jpg", "png"])
style_image_file = st.file_uploader("Upload Style Image", type=["jpg", "png"])

if content_image_file and style_image_file:
    content_image = load_image(content_image_file)
    style_image = load_image(style_image_file)

    model = load_model()

    content_image = load_and_process_image(np.array(content_image))
    style_image = load_and_process_image(np.array(style_image))

    with st.spinner("Analyzing..."):
        stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
        stylized_image = tensor_to_image(stylized_image)

        if st.button("Genrate Image"):
            st.image(stylized_image, caption='Stylized Image', use_column_width=True)
