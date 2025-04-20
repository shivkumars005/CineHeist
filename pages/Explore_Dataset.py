import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Dataset | CineHeist",page_icon="Images/favicon.ico", layout="wide")
st.title("Explore the Dataset")

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

movies_df = load_data()

st.write("### Dataset Overview")
st.dataframe(movies_df.head(10))

st.write("### Dataset Statistics")
st.write(movies_df.describe())
# Function to encode local image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

def set_background(image_path):
    base64_image = get_base64_image(image_path)
    background_css = f"""
    <style>
    .stApp {{
        background-image: url("{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Main app
set_background("Images/Home_Bg.jpg")