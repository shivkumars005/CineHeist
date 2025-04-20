import streamlit as st
import base64

st.set_page_config(page_title="About | CineHeist",page_icon="Images/favicon.ico", layout="wide")
st.title("About This App")

st.markdown("""
    This Movie Recommendation System is a multipage app built with **Streamlit**. 
    It uses **TF-IDF Vectorization** and **Cosine Similarity** to recommend movies based on user input.
    
    ### Features
    - Plot-based movie recommendations.
    - Movie title based movie recommendations.
    - Dataset exploration.
    - Links to IMDb for detailed movie information.

    ### Credits
    - Built with ❤️ using Python and Streamlit.

    ### Links
    - [GitHub Repository](https://github.com/shivkumars005/moviesrecommend)
""")
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