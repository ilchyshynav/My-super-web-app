import streamlit as st
import os
from PIL import Image
import requests
from dotenv import load_dotenv
import urllib.parse
from io import BytesIO
import numpy as np
import cv2

load_dotenv()

HF_API_URL = "https://router.huggingface.co/hf-interface/models/black-forest-labs/FLUX.1-schnell"
HF_TOKEN = os.getenv("HF_TOKEN")

st.sidebar.header("Filter settings")

filter_option = st.sidebar.selectbox(
    "Choose your filter",
    ["Original", "Black-White", "Blurred", "Bright",
     "Contrast", "Inversion", "Mirror"]
)

def generate_image_hf(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed=43"

        response = requests.get(url, timeout=45)

        if response.status_code == 200:
            return response.content, None
        else:
            return None, f"Сервіс тимчасово недоступний ({response.status_code})"

    except requests.exceptions.Timeout:
        return None, "Timeout"
    except Exception as e:
        return None, f"Помилка: {e}"

st.title("AI Creative Studio")
st.write("Describe the picture you want to get")

prompt = st.text_area("Describe the picture (prompt)")

if "image_bytes" not in st.session_state:
    st.session_state.image_bytes = None

if st.button("Generate your picture!") and prompt:
    with st.spinner("AI is creating your image!"):
        image_bytes, error = generate_image_hf(prompt)
    
    if error:
        st.error(error)
    elif image_bytes:
        st.session_state.image_bytes = image_bytes

if st.session_state.image_bytes is not None:
    image = Image.open(BytesIO(st.session_state.image_bytes)).convert("RGB")
    img_array = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original photo")
        st.image(img_array, use_container_width=True)

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
        st.image(processed_img, use_container_width=True)