import streamlit as st
import base64

st.set_page_config(page_title="Home | CineHeist",page_icon="BG_Images/favicon.ico", layout="wide")

st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h1>Welcome to the CineHeist</h1>
            <h3>Your movie matchmaker</h3>
    </div>
""", unsafe_allow_html=True)

st.write("### Navigate to different pages using the sidebar.")
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
set_background("BG_Images\Home_Bg.jpg")