import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="YFPE", page_icon="https://png.pngtree.com/png-vector/20250919/ourmid/pngtree-cheerful-monkey-wearing-hat-taking-picture-with-camera-isolated-on-a-png-image_17472422.webp", layout="wide")

st.title("Your Favourite Photo Editor")
st.write("Put in your image and use all the filters you want!")

st.sidebar.header("Filter settings")

uploaded_file = st.sidebar.file_uploader("Choose your image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original photo")
        st.image(img_array, width="stretch")

    filter_option = st.sidebar.selectbox("Choose your filter", ["Original", "Black-White",
                                                                "Blurred", "Bright",
                                                                "Contrast", "Inversion",
                                                                "Mirror"])

    processed_img = img_array.copy()

    if filter_option == "Black-White":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) 
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    elif filter_option == "Blurred":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)
    elif filter_option == "Bright":
        processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)
    elif filter_option == "Contrast":
            processed_img = cv2.convertScaleAbs(img_array, alpha=1.7, beta=0)
    elif filter_option == "Inversion":
            processed_img = 255 - img_array
    elif filter_option == "Mirror":
            processed_img = cv2.flip(img_array, 1)

    with col2:
         st.subheader("With filter")
         st.image(processed_img, width="stretch")
