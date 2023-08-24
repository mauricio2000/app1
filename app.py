import streamlit as st
from PIL import Image

st.title("Mi primera aplicacion")
st.write("Mauricio Castaño Uribe")

image = Image.open('jojo meme.jpeg')
st.image(image,caption='solo es un meme')
