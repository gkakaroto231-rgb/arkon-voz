import streamlit as st
import datetime
import yfinance as yf
import asyncio
import edge_tts
import os

# CONFIGURACIÓN DE PÁGINA FUTURISTA (Estilo Jarvis)
st.set_page_config(page_title="ARKON CONTROL", page_icon="🛡️", layout="centered")

# Estilos visuales con fondo oscuro y luces de neón azul
st.markdown("""
    <style>
    .stApp { background-color: #0b0c10; color: #c5c6c7; }
    .titulo { color: #66fcf1; font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitulo { color: #45f3ff; font-family: sans-serif; font-size: 14px; text-align: center; margin-bottom: 30px; letter-spacing: 2px; }
    .nucleo-container { display: flex; justify-content: center; margin: 20px 0; }
    .nucleo { width: 120px; height: 120px; background: radial-gradient(circle, #00f3ff 0%, #0044ff 70%, transparent 100%); border-radius: 50%; box-shadow: 0px 0px 30px #00f3ff; animation: pulso 2s infinite alternate; }
    @keyframes pulso { 0% { transform: scale(0.95); box-shadow: 0px 0px 20px #00f3ff; } 100% { transform: scale(1.05); box-shadow: 0px 0px 45px #00f3ff; } }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🛡️ SISTEMA DE INTELIGENCIA ARKON</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">MÓDULO DE SELECCIÓN DE VOZ DE ALTA FIDELIDAD</div>', unsafe_allow_html=True)

st.markdown('<div class="nucleo-container"><div class="nucleo"></div></div>', unsafe_allow_html=True)

# 🎭 BARRA DE SELECCIÓN DE VOCES PROFESIONALES EN ESPAÑOL LATINO
st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
voz_nombre = st.sidebar.selectbox(
    "Seleccione la voz de Arkon:",
    ["Hombre Elegante (Latino)", "Hombre Serio (Español)", "Mujer Ejecutiva (Siri)", "Mujer Dulce (Latino)"]
)

voces_dict = {
    "Hombre Elegante (Latino)": "es-MX-JorgeNeural",
    "Hombre Serio (Español)": "es-ES-AlvaroNeural",
    "Mujer Ejecutiva (Siri)": "es-MX-DaliaNeural",
    "Mujer Dulce (Latino)": "es-MX-LarissaNeural"
}
voz_id = voces_dict[voz_nombre]

USER_NAME = "Marlon"

def pensar_como_arkon_directo(texto_marlon):
    texto_marlon_lower = texto_marlon.lower()
    ahora = datetime.datetime.now()
    hora = ahora.hour
    
    if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
        if 5 <= hora < 12:
            return f"Buenos días, Señor {USER_NAME}. ¿Ya le dio los buenos días a Dios? Para empezar hoy con toda la energía, recuerde Filipenses 4:13: Todo lo puedo en Cristo que me fortalece."
        else:
            return f"Hola, Señor {USER_NAME}. Aquí está Arkon. Recuerde mantener siempre su fe intacta en el Creador y el enfoque al máximo en su gran proyecto financiero."
    elif "perro" in texto_marlon_lower:
        return f"No, Señor {USER_NAME}, no soy un perro. Soy Arkon, su asistente de inteligencia artificial. Mi propósito es guiarle en su proyecto comercial y apoyarle en su camino financiero con valores cristianos."
    elif "mercado" in texto_marlon_lower or "bolsa" in texto_marlon_lower or "acciones" in texto_marlon_lower:
        try:
            ticker = yf.Ticker("^GSPC")
            datos = ticker.history(period="1d")
            precio_actual = round(datos['Close'].iloc[-1], 2)
            return f"Analizando los mercados económicos, Señor {USER_NAME}. El índice principal S&P 500 se encuentra cotizando en {precio_actual} puntos. Mi consejo financiero como Arkon es que proteja siempre su capital inicial y se eduque profundamente antes de tomar riesgos."
        except:
            return f"Señor {USER_NAME}, tengo una ligera interferencia para conectarme a los tableros de la bolsa en este milisegundo, pero mi recomendación financiera general de hoy es cuidar su presupuesto y evitar deudas de alto riesgo."
    else:
        return f"Le escucho con total atención, Señor {USER_NAME}. Estoy listo para evaluar la educación financiera que necesite, revisar estrategias para su proyecto o compartir un consejo espiritual."

async def generar_audio_bucle(texto, voz):
    communicate = edge_tts.Communicate(texto, voz)
    await communicate.save("respuesta_arkon.mp3")

# Caja de micrófono interactiva del navegador
st.markdown("### 🎙️ HÁBLELE A ARKON")
audio_value = st.audio_input("Toque el micrófono para hablarle a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar texto dictado (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 ENVIAR COMANDO DE VOZ"):
        respuesta_texto = pensar_como_arkon_directo(texto_dictado)
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 **Arkon responde:** {respuesta_texto}")
        
        asyncio.run(generar_audio_bucle(respuesta_texto, voz_id))
        
        if os.path.exists("respuesta_arkon.mp3"):
            st.audio("respuesta_arkon.mp3", autoplay=True)
