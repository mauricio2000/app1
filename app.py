import streamlit as st
from PIL import Image

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("data:image/jpeg;base64,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")
    }
   .sidebar .sidebar-content {
        background: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Felpoderdelconsumidor.org%2Fwp-content%2Fuploads%2F2021%2F08%2Fsandia.jpg&tbnid=4QqOeJ57CdH52M&vet=12ahUKEwi3yu_jgLeCAxVwE1kFHV3uBD8QMygAegQIARBv..i&imgrefurl=https%3A%2F%2Felpoderdelconsumidor.org%2F2021%2F08%2Fel-poder-de-la-sandia%2F&docid=4Vo4qa0l6rufbM&w=600&h=375&q=sandia&client=opera&ved=2ahUKEwi3yu_jgLeCAxVwE1kFHV3uBD8QMygAegQIARBv")
    }
    </style>
    """,
    unsafe_allow_html=True
)

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


st.subheader("Selectbox")

inmod= st.selectbox("Selecciona la modalidad",("Audio","Visual","Haptico"))

if inmod == "Audio":
  set_mod = "Repoducir audio"
elif inmod == "Visual":
  set_mod = "Repoducir video"
elif inmod == "Haptico":
  set_mod = "Activar vibración"

st.write(set_mod)


with st.sidebar:
  st.subheader("Configura la modalidad")
  modRadio = st.radio("Escoge la modalidad",("Visual","Audio","Haptica"))
