import streamlit as st
from transformers import pipeline
from PIL import Image

# Set up the pipeline for image-to-text using the BLIP model
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Streamlit app layout
st.title("Image Captioning App")
st.write("Upload an image and get a descriptive caption!")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Generate caption when the button is clicked
    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = pipe(image)
            st.write("**Generated Caption:**", caption[0]['generated_text'])
