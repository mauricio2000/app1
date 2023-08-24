import streamlit as st
from PIL import Image

st.title("Mi primera aplicacion")
st.write("Mauricio Castaño Uribe")

image = Image.open('jojo meme.jpeg')
st.image(image,caption='solo es un meme')

texto = st.text_input('Escribe algo')
st.write('Texto escrito es:',texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la columna número 1")
  resp = st.checkbox("Aja si")
  if resp:
    st.write("no joda mani, pero como asi?")
  else:
    st.write("oie pero ya tu sabe")

with col2:
  st.subheader("Esta es la solumna número 2")
  modo = st.radio("Cual modalidad es su intefaz?",('visual','audio','tactil'))
  if modo == 'visual':
    st.write("es visual")
  elif modo == 'audio':
    st.write("es audio")
  elif modo == 'tactil':
    st.write("es tactil")
