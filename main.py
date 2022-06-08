from faulthandler import disable
from pickletools import string1
import streamlit as st
from PIL import Image

from processing import detect_color

st.title('Simple image product !')

img_file_buffer = st.camera_input("Take a picture")

check_red = st.checkbox('Red filter only')
str = ''
if check_red:
    str = 'Select a lower RED color range values; Hue (0 - 10)'
else:
    str = 'Select a color range of H(hue)'

h_range = st.slider(str, 0, 179, (0, 10))
h_min = h_range[0]
h_max = h_range[1]
# st.write('H range :', h_range)

h_red_range = st.slider('Select a upper RED color range values; Hue (160 - 179)', 0, 179, (160, 179), disabled = not check_red)
h_red_min = h_red_range[0]
h_red_max = h_red_range[1]
# st.write('H range :', h_red_range)

s_min = st.slider('Select a range of S(saturation)', 0, 255, 0)
# st.write('S :', s_min)

v_min = st.slider('Select a range of V(value)', 0, 255, 0)
# st.write('V :', v_min)

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    
    img, res = detect_color(bytes_data, h_min, h_max, s_min, v_min, h_red_min, h_red_max, check_red) 
    
    image_mask = Image.open('mask.jpg')
    # st.image(image_mask, 'Color Masking')

    image_res = Image.open('res.jpg')
    # st.image(image_res, 'Color Result')

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Color Masking')
        st.image(image_mask)

    with col2:
        st.header('Color Result')
        st.image(image_res)
