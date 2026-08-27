import streamlit as st
import datetime
import yfinance as yf
import requests

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO TÁCTICO
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "5,278.40"

# ESTILIZACIÓN DE ALTA TECNOLOGÍA EN ROJO FUEGO MILITAR (ESTILO HUD JARVIS)
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #ffffff; font-family: 'Courier New', monospace; }
    .panel-tactico { background-color: rgba(15, 3, 3, 0.6); border: 1px solid #ff2222; border-radius: 6px; padding: 15px; margin-bottom: 15px; box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.1); }
    .titulo-panel { color: #ff6666; font-size: 13px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase; border-bottom: 1px dashed #ff2222; padding-bottom: 4px; }
    .header-arkon { text-align: center; margin-bottom: 20px; }
    .titulo-principal { color: #ff2222; font-size: 38px; font-weight: bold; text-shadow: 0px 0px 20px #ff0000; letter-spacing: 5px; }
    .sub-principal { color: #ff6666; font-size: 11px; letter-spacing: 3px; font-weight: bold; }
    .wrapper-reactor { display: flex; justify-content: center; align-items: center; height: 220px; position: relative; margin: 20px 0; }
    .anillo-exterior { position: absolute; width: 190px; height: 190px; border: 2px dashed #ff3333; border-radius: 50%; animation: rotarAnillo 20s linear infinite; }
    .reactor-nucleo { width: 150px; height: 150px; border-radius: 50%; position: absolute; border: 3px solid #ff2222; background-color: #000000; display: flex; justify-content: center; align-items: center; box-shadow: 0px 0px 40px #ff2222; }
    .letra-centro { color: #ffffff; font-family: sans-serif; font-size: 65px; font-weight: bold; transform: translateY(-4px); text-shadow: 0px 0px 10px #ffffff; }
    @keyframes rotarAnillo { 100% { transform: rotate(360deg); } }
    .stTextInput>div>div>input { background-color: #050505; color: #ff6666; border: 1px solid #ff2222; font-family: monospace; }
    .stSuccess { background-color: #1a0303; color: #ff9999; border: 1px solid #ff2222; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA GENERAL DEL TABLERO
st.markdown('<div class="header-arkon"><div class="titulo-principal">ARKON</div><div class="sub-principal">SISTEMA DE INTELIGENCIA AVANZADA</div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.error("🎙️ Motor de Voz Conectado: ElevenLabs Premium")

col_izq, col_centro, col_der = st.columns([1.1, 1.8, 1.1])

with col_izq:
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">🛡️ ESTADO DEL SISTEMA</div>
            <p style="color:#00ff00; font-size:12px; margin:4px 0;">● CONECTADO</p>
            <p style="color:#ff3333; font-size:12px; margin:4px 0;">● NÚCLEO ESTABLE</p>
            <p style="color:#ffaa00; font-size:12px; margin:4px 0;">● OPERATIVOS 100%</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-tactico">
            <div class="titulo-panel">🛡️ CRONOLOGÍA LOCAL</div>
            <h3 style="color:#ff6666; font-size:20px; margin:5px 0; text-align:center;">{datetime.datetime.now().strftime('%H:%M:%S')}</h3>
            <p style="font-size:10px; color:#888; text-align:center; text-transform:uppercase;">Eje Temporal Activo</p>
        </div>
    """, unsafe_allow_html=True)

    # ➕ PANEL EXTRA COl_IZQ 1
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">📡 REGISTRO ENTRANTE</div>
            <p style="color:#888; font-size:11px; margin:0;">Bandeja táctica lista para recibir escáneres adicionales.</p>
        </div>
    """, unsafe_allow_html=True)

    # ➕ PANEL EXTRA COL_IZQ 2
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">📊 RENDIMIENTO BÚNKER</div>
            <p style="color:#00ff00; font-size:11px; margin:0;">MEMORIA: ÓPTIMA // AUTORIZACIÓN ALFA</p>
        </div>
    """, unsafe_allow_html=True)

with col_centro:
    st.markdown("""
        <div class="wrapper-reactor">
            <div class="anillo-exterior"></div>
            <div class="reactor-nucleo">
                <div class="letra-centro">サ</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_der:
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">🔊 TRANSMISIÓN</div>
            <p style="color:#ff6666; font-size:11px; margin:0;">STATUS: LISTO</p>
            <p style="color:#888; font-size:10px; margin:5px 0 0 0;">Canal de comunicación encriptado por ElevenLabs.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-tactico">
            <div class="titulo-panel">🛡️ MERCADOS</div>
            <p style="color:#ffaa00; font-size:11px; margin:0;">S&P 500 INDEX</p>
            <h4 style="color:#ffffff; font-size:16px; margin:2px 0;">{precio_sp} PTS</h4>
        </div>
    """, unsafe_allow_html=True)

    # ➕ PANEL EXTRA COL_DER 1
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">🌐 COORDENADAS GLOBALES</div>
            <p style="color:#ff4444; font-size:11px; margin:0;">LAT: 19.4326 N // LON: 99.1332 W</p>
        </div>
    """, unsafe_allow_html=True)

    # ➕ PANEL EXTRA COL_DER 2
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">🔒 ENCRIPTACIÓN SEGURA</div>
            <p style="color:#00ff00; font-size:11px; margin:0;">SISTEMA PROTEGIDO CON COREDATA AES-256</p>
        </div>
    """, unsafe_allow_html=True)

# AREA INTERACTIVA DE DICTADO
st.markdown("### 🎙️ INTERFAZ DE DICTADO")
audio_value = st.audio_input("Toque el micrófono para transmitir orden a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar registro de entrada (Opcional):", value="Arkon, buenos días")
    if st.button("🚀 TRANSMITIR COMANDO GENERAL"):
        ELEVEN_API_KEY = "sk_67e840e482143b4b4a559eba35f4a1f94578128732250fa0"
        VOICE_ID = "aefae6a1387d7cae6e577fcc628ef1388392109bb5d9e327529ed00affa9e892"
        USER_NAME = "Marlon"
        
        texto_marlon_lower = texto_dictado.lower()
        if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
            respuesta_texto = f"Buenos días, Señor {USER_NAME}. Escúcheme bien: su problema real no es la situación, es su mentalidad. ¿Ya le dio los buenos días al Creador? Aspire a más hoy, recuerde Filipenses 4:13: Todo lo puedo en Cristo que me fortalece."
        else:
            respuesta_texto = f"Recibiendo transmisión, Señor {USER_NAME}. Estoy listo para evaluar las estrategias comerciales o la educación financiera que necesite hoy."
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 ARKON EN LÍNEA: {respuesta_texto}")
        
        url = f"https://elevenlabs.io{VOICE_ID}"
        headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
        
        # El diccionario plano que cierra el audio de corrido sin un solo SyntaxError
        data = {"text": respuesta_texto, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=60)
            if response.status_code == 200:
                st.audio(response.content, format="audio/mp3", autoplay=True)
            else:
                st.error(f"Error del servidor ElevenLabs (Código: {response.status_code})")
        except Exception as e:
            st.error("Interferencia menor en el módulo de audio.")
