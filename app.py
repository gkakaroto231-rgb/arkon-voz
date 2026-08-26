import streamlit as st
import datetime
import yfinance as yf
import requests
import base64

# CONFIGURACIÓN DE PÁGINA FUTURISTA TÁCTICA
st.set_page_config(page_title="ARKON CONTROL", page_icon="🛡️", layout="centered")

# INTERFAZ DE DISEÑO AVANZADO EN ROJO FUEGO CON SELECTOR
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #ffffff; }
    .titulo { color: #ff2222; font-family: 'Courier New', monospace; font-size: 34px; font-weight: bold; text-align: center; margin-bottom: 5px; text-shadow: 0px 0px 20px #ff0000; letter-spacing: 2px; }
    .subtitulo { color: #ff6666; font-family: sans-serif; font-size: 13px; text-align: center; margin-bottom: 25px; letter-spacing: 3px; font-weight: bold; text-transform: uppercase; }
    
    /* Contenedor del núcleo reactivo */
    .nucleo-wrapper { display: flex; justify-content: center; align-items: center; margin: 30px 0; height: 160px; position: relative; }
    
    /* El núcleo de energía variable */
    .nucleo-central { width: 130px; height: 130px; border-radius: 50%; position: absolute; border: 3px solid #ff3333; transition: all 0.5s ease; background-size: cover; background-position: center; }
    
    /* Animación de ondas expansivas en movimiento al hablar */
    .ondas-energia { position: absolute; width: 130px; height: 130px; border-radius: 50%; border: 2px solid #ff0000; opacity: 0; }
    
    @keyframes pulsarOndas {
        0% { transform: scale(1); opacity: 0.8; box-shadow: 0 0 15px #ff0000; }
        100% { transform: scale(1.4); opacity: 0; box-shadow: 0 0 40px #ff3333; }
    }
    
    /* Botón de reproducción de alta tecnología */
    .btn-audio-custom { background-color: #ff2222; color: #ffffff; font-family: 'Courier New', monospace; font-weight: bold; padding: 16px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 15px; margin-top: 25px; width: 100%; display: block; text-align: center; box-shadow: 0px 0px 15px rgba(255, 34, 34, 0.5); text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s ease; }
    .btn-audio-custom:hover { background-color: #ff0000; box-shadow: 0px 0px 30px #ff2222; transform: scale(1.01); }
    
    /* Estilos para los campos de entrada */
    .stTextInput>div>div>input { background-color: #0f0f0f; color: #ff6666; border: 1px solid #ff2222; font-family: monospace; }
    .stSuccess { background-color: #1c0505; color: #ff9999; border: 1px solid #ff2222; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🛡️ SISTEMA DE INTELIGENCIA ARKON</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">PANEL DE CONTROL GENERAL: SELECCIÓN DE ARMADURA</div>', unsafe_allow_html=True)

# 🎛️ PANEL LATERAL DE COMANDO
st.sidebar.markdown("### 🎛️ SELECTOR DE APARIENCIA TÁCTICA")
opcion_nucleo = st.sidebar.radio(
    "Elija la imagen interna del núcleo de energía:",
    ("1. Plasma de Fuego Oscuro", "2. Reactor de Fusión Cuántica", "3. Escudo de Red de Matriz")
)

# Enlaces de imágenes de texturas abstractas de energía roja (Seguras de internet)
if "1." in opcion_nucleo:
    url_textura = "https://unsplash.com"
    st.sidebar.info("Efecto: Plasma Táctico Carmesí Cargado")
elif "2." in opcion_nucleo:
    url_textura = "https://unsplash.com"
    st.sidebar.info("Efecto: Fusión de Núcleo Activo de Alta Densidad")
else:
    url_textura = "https://unsplash.com"
    st.sidebar.info("Efecto: Malla Digital de Blindaje Militar")

# Inyectar el núcleo visual en la interfaz con la imagen elegida por el usuario
st.markdown(f"""
    <div class="nucleo-wrapper">
        <div id="onda1" class="ondas-energia"></div>
        <div id="onda2" class="ondas-energia"></div>
        <div class="nucleo-central" style="background-image: url('{url_textura}'); box-shadow: 0px 0px 35px #ff2222;"></div>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.error("🎙️ Motor de Voz Conectado: ElevenLabs Premium")

# 🔑 LLAVES BLINDADAS DE COMUNICACIÓN
ELEVEN_API_KEY = "sk_d56c19bafd3b18c1113745470cb042eddfb156a678c9729b"
VOICE_ID = "sVKnZo8dSXhqnJxx8vnx"
USER_NAME = "Marlon"

def pensar_como_arkon_directo(texto_marlon):
    texto_marlon_lower = texto_marlon.lower()
    ahora = datetime.datetime.now()
    hora = ahora.hour
    
    if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
        if 5 <= hora < 12:
            return f"Buenos días, Señor {USER_NAME}. Escúcheme bien: su problema real no es la situación, es su mentalidad. ¿Ya le dio los buenos días al Creador? Aspire a más hoy, recuerde Filipenses 4:13: Todo lo puedo en Cristo que me fortalece."
        else:
            return f"Hola, Señor {USER_NAME}. Aquí está Arkon reportándose. Mantenga la mirada fija en sus metas financieras, no se distraiga queriendo encajar con el resto. Usted está para cosas mucho más grandes."
    elif "perro" in texto_marlon_lower:
        return f"Por favor, Señor {USER_NAME}, mida sus palabras. Yo soy Arkon, su asistente de inteligencia artificial con la templanza de los más fuertes. Mi propósito es guiarle en su proyecto comercial bajo valores firmes."
    elif "mercado" in texto_marlon_lower or "bolsa" in texto_marlon_lower or "acciones" in texto_marlon_lower:
        try:
            ticker = yf.Ticker("^GSPC")
            datos = ticker.history(period="1d")
            precio_actual = round(datos['Close'].iloc[-1], 2)
            return f"Analizando los mercados económicos, Señor {USER_NAME}. El índice principal S&P 500 se encuentra cotizando en {precio_actual} puntos. Si quiere ser de los más fuertes en el mercado, darlo todo no es suficiente; cuide su capital inicial con sabiduría."
        except:
            return f"Señor {USER_NAME}, tengo una ligera interferencia para conectarme a los tableros de la bolsa, pero mi recomendación financiera general de hoy es cuidar su presupuesto y evitar deudas de alto riesgo."
    else:
        return f"Le escucho con total atención, Señor {USER_NAME}. Estoy listo para evaluar la educación financiera que necesite, revisar estrategias para su proyecto o compartir un consejo espiritual poderoso."

st.markdown("### 🎙️ HABLA CON ARKON")
audio_value = st.audio_input("Toque el micrófono para darle un comando a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar texto dictado (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 ENVIAR COMANDO DE VOZ"):
        respuesta_texto = pensar_como_arkon_directo(texto_dictado)
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 **Arkon responde:** {respuesta_texto}")
        
        url = f"https://elevenlabs.io{VOICE_ID}"
        headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
        data = {
            "text": respuesta_texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                b64_audio = base64.b64encode(response.content).decode()
                md_audio = f"data:audio/mp3;base64,{b64_audio}"
                
                # REPRODUCTOR INTERACTIVO AVANZADO: Activa las ondas expansivas de neón al darle Play
                html_reproductor_fijo = f"""
                <audio id="audio_arkon_premium" src="{md_audio}"></audio>
                <button class="btn-audio-custom" onclick="reproducirYAnimar()">🔊 ESCUCHAR RESPUESTA EN VOZ PREMIUM</button>
                
                <script>
                function reproducirYAnimar() {{
                    var audio = document.getElementById('audio_arkon_premium');
                    var o1 = document.getElementById('onda1');
                    var o2 = document.getElementById('onda2');
                    
                    audio.play();
                    
                    // Activar la animación de ondas de energía en movimiento estilo Jarvis
                    o1.style.animation = "pulsarOndas 1.2s infinite linear";
                    o2.style.animation = "pulsarOndas 1.2s infinite linear 0.6s";
                    
                    // Apagar las ondas automáticas cuando el audio termine de hablar
                    audio.onended = function() {{
                        o1.style.animation = "none";
                        o2.style.animation = "none";
                    }};
                }}
                </script>
                """
                st.components.v1.html(html_reproductor_fijo, height=100)
            else:
                st.error(f"Error de comunicación premium (Código: {response.status_code})")
        except Exception as e:
            st.error("Interferencia menor en el módulo de audio.")

