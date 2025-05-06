import streamlit as st
from gtts import gTTS
from PIL import Image

st.set_page_config(page_title="Voz para Meditar", page_icon="🧘", layout="centered")

st.title("🧘 Voz para Meditar")
st.write("Escribe una frase de afirmación o guía de meditación, y escúchala con calma.")

# Mostrar la imagen
imagen = Image.open("yoga.jpeg")
st.image(imagen, caption="Encuentra tu centro 🕊️", use_column_width=True)

# Entrada de texto
texto = st.text_area("💭 Escribe tu afirmación positiva o guía de meditación aquí:", 
                     placeholder="Ejemplo: Inspiro calma, exhalo tensión...")

# Opción para voz lenta
voz_lenta = st.checkbox("¿Quieres que se escuche más lento?", value=True)

# Botón para generar el audio
if st.button("🎧 Escuchar mi meditación"):
    if texto.strip() == "":
        st.warning("Por favor, escribe una frase primero.")
    else:
        tts = gTTS(text=texto, lang='es', slow=voz_lenta)
        tts.save("meditacion.mp3")
        audio_file = open("meditacion.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        st.success("Respira profundo y escucha...")
