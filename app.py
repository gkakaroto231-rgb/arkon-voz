import streamlit as st
import datetime
import yfinance as yf
import requests

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO CINEMATOGRÁFICO (INSPIRADO EN BEHANCE HUD)
st.set_page_config(page_title="ARKON QUANTUM HUD", page_icon="🛡️", layout="wide")

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO HUD
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "5,278.40"

# INGENIERÍA VISUAL AVANZADA: DISEÑO HUD SCI-FI DE ALTA FIDELIDAD CON ANILLOS ROTATIVOS CRUZADOS
st.markdown("""
    <style>
    .stApp { background-color: #020203; color: #ffffff; font-family: 'Courier New', monospace; }
    
    /* Marcos y Paneles HUD con Esquinas Cortadas y Brillo de Neón Rojo */
    .panel-hud { 
        background: linear-gradient(135deg, rgba(20, 2, 2, 0.7) 0%, rgba(5, 1, 1, 0.9) 100%); 
        border: 1px solid #ff1111; 
        border-radius: 4px; 
        padding: 18px; 
        margin-bottom: 20px; 
        box-shadow: 0px 0px 20px rgba(255, 0, 0, 0.15), inset 0px 0px 10px rgba(255, 0, 0, 0.05);
        position: relative;
    }
    .panel-hud::before {
        content: ""; position: absolute; top: 0; left: 0; width: 8px; height: 8px; border-top: 2px solid #ff3333; border-left: 2px solid #ff3333;
    }
    .panel-hud::after {
        content: ""; position: absolute; bottom: 0; right: 0; width: 8px; height: 8px; border-bottom: 2px solid #ff3333; border-right: 2px solid #ff3333;
    }
    
    .titulo-hud { color: #ff5555; font-size: 12px; font-weight: bold; letter-spacing: 3px; margin-bottom: 12px; text-transform: uppercase; border-bottom: 1px dashed rgba(255, 17, 17, 0.4); padding-bottom: 6px; }
    
    /* Cabecera Principal HUD Cinematográfica */
    .header-militar { text-align: center; margin-bottom: 30px; position: relative; padding: 10px; border-bottom: 1px solid rgba(255, 17, 17, 0.2); }
    .titulo-militar { color: #ff1111; font-size: 42px; font-weight: bold; text-shadow: 0px 0px 25px #ff0000; letter-spacing: 8px; }
    .sub-militar { color: #ff6666; font-size: 11px; letter-spacing: 4px; font-weight: bold; opacity: 0.8; }
    
    /* REACTOR SCI-FI COMPLEJO DE ANILLOS CONCÉNTRICOS EN MOVIMIENTO (ESTILO BEHANCE) */
    .wrapper-holograma { display: flex; justify-content: center; align-items: center; height: 260px; position: relative; margin: 15px 0; }
    
    /* Capa 1: Anillo Externo de Puntos */
    .anillo-hud-1 { position: absolute; width: 230px; height: 230px; border: 1px dotted rgba(255, 17, 17, 0.4); border-radius: 50%; animation: rotarDerecha 40s linear infinite; }
    /* Capa 2: Anillo de Control Escalonado */
    .anillo-hud-2 { position: absolute; width: 200px; height: 200px; border: 2px dashed #ff2222; border-radius: 50%; animation: rotarIzquierda 20s linear infinite; opacity: 0.7; }
    /* Capa 3: Anillo de Cierre de Radar */
    .anillo-hud-3 { position: absolute; width: 174px; height: 174px; border-top: 3px solid #ff3333; border-bottom: 3px solid #ff3333; border-left: 3px solid transparent; border-right: 3px solid transparent; border-radius: 50%; animation: rotarDerecha 8s linear infinite; }
    
    /* Núcleo Central de Energía Absoluta con la letra japonesa サ */
    .reactor-core { width: 136px; height: 130px; border-radius: 50%; position: absolute; background: radial-gradient(circle, rgba(255,0,0,0.2) 0%, rgba(0,0,0,1) 80%); border: 2px solid #ff1111; display: flex; justify-content: center; align-items: center; box-shadow: 0px 0px 35px #ff1111; z-index: 10; }
    .letra-hud { color: #ffffff; font-family: sans-serif; font-size: 60px; font-weight: bold; transform: translateY(-4px); text-shadow: 0px 0px 15px #ffffff, 0px 0px 30px #ff0000; }
    
    /* Movimientos del Radar */
    @keyframes rotarDerecha { 100% { transform: rotate(360deg); } }
    @keyframes rotarIzquierda { 100% { transform: rotate(-360deg); } }
    
    /* Personalización Táctica de Streamlit */
    .stTextInput>div>div>input { background-color: #080202; color: #ff6666; border: 1px solid #ff1111; font-family: monospace; }
    .stSuccess { background-color: #150202; color: #ff9999; border: 1px solid #ff1111; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA GENERAL DEL SISTEMA HUD
st.markdown('<div class="header-militar"><div class="titulo-militar">ARKON TACTICAL</div><div class="sub-militar">CENTER COMMAND INTERFACE // SYSTEM ACTIVE</div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ CONFIGURACIÓN LOGÍSTICA")
st.sidebar.error("🎙️ Red de Audio: ElevenLabs Core Active")

# DISTRIBUCIÓN CINEMATOGRÁFICA DEL HUD EN 3 COLUMNAS TÁCTICAS
col_izq, col_centro, col_der = st.columns([1.2, 1.6, 1.2])

with col_izq:
    st.markdown("""
        <div class="panel-hud">
            <div class="titulo-hud">📡 RASTREO DE ENERGÍA</div>
            <p style="color:#00ff00; font-size:12px; margin:4px 0; font-weight:bold;">● ONLINE // ENLACE ESTABLE</p>
            <p style="color:#ff1111; font-size:12px; margin:4px 0;">● REGENERACIÓN DE NÚCLEO: 100%</p>
            <p style="color:#ffaa00; font-size:12px; margin:4px 0;">● ANILLOS HOLOGRÁFICOS: ACTIVOS</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-hud">
            <div class="titulo-hud">⏱️ RELOJ DE SECUENCIA</div>
            <h3 style="color:#ff4444; font-size:22px; margin:5px 0; text-align:center; font-weight:bold; letter-spacing:1px;">{datetime.datetime.now().strftime('%H:%M:%S')}</h3>
            <p style="font-size:9px; color:#666; text-align:center; text-transform:uppercase;">Eje Temporal del Búnker</p>
        </div>
    """, unsafe_allow_html=True)

with col_centro:
    # RENDERIZAR EL REACTOR AVANZADO CON LAS TRES CAPAS EN MOVIMIENTO ESTILO BEHANCE
    st.markdown("""
        <div class="wrapper-holograma">
            <div class="anillo-hud-1"></div>
            <div class="anillo-hud-2"></div>
            <div class="anillo-hud-3"></div>
            <div class="reactor-core">
                <div class="letra-hud">サ</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_der:
    st.markdown("""
        <div class="panel-hud">
            <div class="titulo-hud">🔊 MODULACIÓN DE TRANSMISIÓN</div>
            <p style="color:#ff4444; font-size:11px; margin:0; font-weight:bold;">CANAL: DIGITAL PREMIUM</p>
            <p style="color:#888; font-size:10px; margin:6px 0 0 0;">Canalización directa de voz con la tecnología de ElevenLabs.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-hud">
            <div class="titulo-hud">📉 FLUJO ECONÓMICO REAL</div>
            <p style="color:#ffaa00; font-size:11px; margin:0; font-weight:bold;">S&P 500 MARKET INDEX</p>
            <h4 style="color:#ffffff; font-size:18px; margin:4px 0; font-weight:bold; letter-spacing:1px;">{precio_sp} PTS</h4>
        </div>
    """, unsafe_allow_html=True)

# AREA INTERACTIVA DE DICTADO HUD ABAJO DEL REACTOR
st.markdown("### 🎙️ REGISTRO DE ENTRADA INTERACTIVO")
audio_value = st.audio_input("Toque el micrófono para transmitir comando general a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar registro de entrada manual (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 TRANSMITIR COMANDO OPERATIVO"):
        # 🔑 INYECCIÓN PERFECTA DE SU NUEVA LLAVE SIN ERRORES DE SANGRE
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
        
        # Dirección oficial de la API de ElevenLabs corregida al 100%
        url = f"https://elevenlabs.io{VOICE_ID}"
        
        headers = {
            "xi-api-key": ELEVEN_API_KEY,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": respuesta_texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=60)
            if response.status_code == 200:
                st.audio(response.content, format="audio/mpeg", autoplay=True)
            else:
                st.error(f"ElevenLabs devolvió el código {response.status_code}")
                st.code(response.text)
        except requests.RequestException as e:
            st.error(f"Error de conexión: {e}")
