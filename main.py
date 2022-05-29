import streamlit as st
from PIL import Image

from processing import detect_yellow

st.title('Simple image product !')

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    
    img = detect_yellow(bytes_data)
    
    
    image_yellow = Image.open('yellow.jpg')
    st.image(image_yellow, 'is detected yellow')
    
    
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(img))