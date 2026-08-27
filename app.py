import streamlit as st
import datetime
import yfinance as yf
import requests
import base64

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO TÁCTICO - EDICIÓN AGUA LÍQUIDA
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "5,278.40"

# INGENIERÍA VISUAL: EFECTO DE OLAS DE AGUA LÍQUIDA EN MOVIMIENTO (SIN FONDO NEGRO DE ESFERA)
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #ffffff; font-family: 'Courier New', monospace; }
    
    /* Contenedores de los Paneles Tácticos */
    .panel-tactico { background-color: rgba(15, 3, 3, 0.6); border: 1px solid #ff2222; border-radius: 6px; padding: 15px; margin-bottom: 15px; box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.1); }
    .titulo-panel { color: #ff6666; font-size: 13px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase; border-bottom: 1px dashed #ff2222; padding-bottom: 4px; }
    
    /* Cabecera Principal */
    .header-arkon { text-align: center; margin-bottom: 20px; }
    .titulo-principal { color: #ff2222; font-size: 38px; font-weight: bold; text-shadow: 0px 0px 20px #ff0000; letter-spacing: 5px; }
    .sub-principal { color: #ff6666; font-size: 11px; letter-spacing: 3px; font-weight: bold; }
    
    /* RECTOR DE AGUA LÍQUIDA SIN FONDO NEGRO */
    .wrapper-reactor { display: flex; justify-content: center; align-items: center; height: 240px; position: relative; margin: 20px 0; }
    
    /* Anillo exterior dashed decorativo */
    .anillo-exterior { position: absolute; width: 210px; height: 210px; border: 1px dashed rgba(255, 34, 34, 0.3); border-radius: 50%; animation: rotarAnillo 25s linear infinite; }
    
    /* Contenedor del Tanque de Agua Transparente */
    .reactor-liquido { position: relative; width: 160px; height: 160px; border-radius: 50%; border: 4px solid #ff2222; overflow: hidden; background: transparent; box-shadow: 0 0 25px rgba(255, 0, 0, 0.3); display: flex; justify-content: center; align-items: center; }
    
    /* Efecto Olas de Agua de Corrido */
    .reactor-liquido::before, .reactor-liquido::after { content: ""; position: absolute; width: 280px; height: 280px; background-color: rgba(255, 0, 0, 0.45); top: 55%; left: 50%; transform: translate(-50%, -50%); border-radius: 40%; animation: moverOlas 4s linear infinite; pointer-events: none; z-index: 1; }
    /* Segunda ola cruzada para simular líquido real */
    .reactor-liquido::after { background-color: rgba(255, 34, 34, 0.25); border-radius: 35%; animation: moverOlas 6s linear infinite; }
    
    /* Letra Japonesa サ Flotando en el centro absoluto por encima del agua */
    .letra-centro { color: #ffffff; font-family: sans-serif; font-size: 65px; font-weight: bold; position: relative; z-index: 5; text-shadow: 0px 0px 12px #ffffff; transition: all 0.3s ease; }
    
    /* Ondas de choque que se activan al presionar Hablar */
    .ondas-energia { position: absolute; width: 160px; height: 160px; border-radius: 50%; border: 2px solid #ff0000; opacity: 0; pointer-events: none; }
    
    /* ANIMACIONES MATEMÁTICAS DE AGUA Y FLUIDOS */
    @keyframes moverOlas {
        0% { transform: translate(-50%, -50%) rotate(0deg); }
        100% { transform: translate(-50%, -50%) rotate(360deg); }
    }
    @keyframes rotarAnillo { 100% { transform: rotate(360deg); } }
    @keyframes pulsarOndas {
        0% { transform: scale(1); opacity: 0.9; box-shadow: 0 0 15px #ff0000; }
        100% { transform: scale(1.4); opacity: 0; box-shadow: 0 0 45px #ff3333; }
    }
    
    /* Botón de reproducción Blindado */
    .btn-audio-custom { background-color: #ff2222; color: #ffffff; font-family: 'Courier New', monospace; font-weight: bold; padding: 14px 20px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; width: 100%; display: block; text-align: center; box-shadow: 0px 0px 15px rgba(255, 34, 34, 0.4); text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s ease; margin-top: 15px; }
    .btn-audio-custom:hover { background-color: #ff0000; box-shadow: 0px 0px 25px #ff2222; }
    
    /* Inputs de Streamlit modificados estilo Táctico */
    .stTextInput>div>div>input { background-color: #050505; color: #ff6666; border: 1px solid #ff2222; font-family: monospace; }
    .stSuccess { background-color: #1a0303; color: #ff9999; border: 1px solid #ff2222; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA GENERAL DEL TABLERO
st.markdown('<div class="header-arkon"><div class="titulo-principal">ARKON</div><div class="sub-principal">SISTEMA DE INTELIGENCIA AVANZADA</div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ LOGÍSTICA DE REGENERACIÓN")
st.sidebar.info("Efecto Líquido: Hidro-Reactor de Olas Tácticas Activado.")
st.sidebar.markdown("---")
st.sidebar.error("🎙️ Motor de Voz Conectado: ElevenLabs Premium")

# DISTRIBUCIÓN DEL TABLERO EN 3 COLUMNAS TÁCTICAS
col_izq, col_centro, col_der = st.columns([1.1, 1.8, 1.1])

with col_izq:
    st.markdown("""
        <div class="panel-tactico">
            <div class="titulo-panel">📡 ESTADO DEL SISTEMA</div>
            <p style="color:#00ff00; font-size:12px; margin:4px 0;">● CONECTADO</p>
            <p style="color:#ff3333; font-size:12px; margin:4px 0;">● FLUIDO ESTABLE</p>
            <p style="color:#ffaa00; font-size:12px; margin:4px 0;">● OPERATIVOS 100%</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-tactico">
            <div class="titulo-panel">⏱️ PARÁMETRO TEMPORAL</div>
            <h3 style="color:#ff6666; font-size:20px; margin:5px 0; text-align:center;">{datetime.datetime.now().strftime('%H:%M:%S')}</h3>
            <p style="font-size:10px; color:#888; text-align:center; text-transform:uppercase;">Eje Temporal Activo</p>
        </div>
    """, unsafe_allow_html=True)

with col_centro:
    # RENDERIZAR EL REACTOR TRANSPARENTE CON OLAS DINÁMICAS Y LOGO FLOTANTE
    st.markdown(f"""
        <div class="wrapper-reactor">
            <div class="anillo-exterior"></div>
            <div id="o1" class="ondas-energia"></div>
            <div id="o2" class="ondas-energia"></div>
            <div class="reactor-liquido">
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
            <div class="titulo-panel">📈 MERCADOS</div>
            <p style="color:#ffaa00; font-size:11px; margin:0;">S&P 500 INDEX</p>
            <h4 style="color:#ffffff; font-size:16px; margin:2px 0;">{precio_sp} PTS</h4>
        </div>
    """, unsafe_allow_html=True)

# AREA INTERACTIVA DE COMANDOS ABAJO DEL CENTRO DE MANDO
st.markdown("### 🎙️ INTERFAZ DE DICTADO")
audio_value = st.audio_input("Toque el micrófono para transmitir orden a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar registro de entrada (Opcional):", value="Arkon, estado del mercado")
    
    if st.button("🚀 TRANSMITIR COMANDO GENERAL"):
        ELEVEN_API_KEY = "sk_d56c19bafd3b18c1113745470cb042eddfb156a678c9729b"
        VOICE_ID = "sVKnZo8dSXhqnJxx8vnx"
        USER_NAME = "Marlon"
        
        texto_marlon_lower = texto_dictado.lower()
        if "mercado" in texto_marlon_lower or "bolsa" in texto_marlon_lower:
            respuesta_texto = f"Analizando los mercados, Señor {USER_NAME}. El S&P 500 se encuentra cotizando estable en {precio_sp} puntos. Mi recomendación táctica de hoy es: enfoque estricto, disciplina de acero y protección absoluta de su capital inicial. No tome riesgos innecesarios."
        else:
            respuesta_texto = f"Recibiendo transmisión, Señor {USER_NAME}. Estoy evaluando los parámetros de su proyecto comercial. Mantenga la cabeza fría y la disciplina al máximo nivel hoy."
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 ARKON EN LÍNEA: {respuesta_texto}")
        
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
                audio_bytes = response.content
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
                
                # Sincronizador de animación nativo para las olas expansivas de TikTok
                st.markdown("""
                    <script>
                    var onda1 = window.parent.document.getElementById('o1');
                    var onda2 = window.parent.document.getElementById('o2');
                    if(onda1 && onda2) {
                        onda1.style.animation = 'pulsarOndas 1.2s infinite linear';
                        onda2.style.animation = 'pulsarOndas 1.2s infinite linear 0.6s';
                        setTimeout(function(){
                            onda1.style.animation = 'none';
                            onda2.style.animation = 'none';
                        }, 5000);
                    }
                    </script>
                """, unsafe_allow_html=True)
            else:
