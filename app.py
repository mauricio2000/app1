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
  modo = st.radio("¿Que prefieres?",('Hamburguesa','Changua','Pizza'))
  if modo == 'Hamburguesa':
    st.write("Excelente esa es mi favorita, voy a pedir un par de domicilio")
  elif modo == 'Changua':
    st.write("Ahí esta la puerta")
  elif modo == 'Pizza':
    st.write("Si si bastante bien, ven vamos por una Pizza")

if st.button("Dale aqui"):
  st.write("Eso es, muy bien")
else:
  st.write("Dale pues pai")
