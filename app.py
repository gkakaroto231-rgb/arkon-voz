import streamlit as st
import datetime
import yfinance as yf
import requests

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO SUPREMO - EDICIÓN ARKON COMMAND MILITAR
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO S&P 500 TÁCTICO
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "7,724.10"

# INGENIERÍA VISUAL AVANZADA: REPLICACIÓN EXACTA DE LA INTERFAZ HUD CINEMATOGRÁFICA DE LA FOTO
st.markdown("""
    <style>
    /* Fondo Negro Absoluto y Fuente Monoespaciada Militar */
    .stApp { background-color: #000000; color: #ff3333; font-family: 'Courier New', monospace; padding: 10px; }
    
    /* Paneles Tácticos con Bordes Rojos Neón y Esquinas de Precisión */
    .panel-militar {
        background-color: rgba(6, 0, 0, 0.85);
        border: 1px solid #ff0000;
        border-radius: 4px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.2), inset 0px 0px 10px rgba(255, 0, 0, 0.1);
        position: relative;
    }
    .panel-militar::before {
        content: ""; position: absolute; top: 0; left: 0; width: 6px; height: 6px; border-top: 2px solid #ff3333; border-left: 2px solid #ff3333;
    }
    .panel-militar::after {
        content: ""; position: absolute; bottom: 0; right: 0; width: 6px; height: 6px; border-bottom: 2px solid #ff3333; border-right: 2px solid #ff3333;
    }
    
    /* Textos y Títulos del HUD */
    .titulo-seccion { color: #ff4444; font-size: 13px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; border-bottom: 1px dashed rgba(255, 0, 0, 0.3); padding-bottom: 4px; display: flex; align-items: center; }
    .status-green { color: #00ff00; font-weight: bold; font-size: 11px; }
    .status-red { color: #ff0000; font-weight: bold; font-size: 11px; }
    .status-yellow { color: #ffaa00; font-weight: bold; font-size: 11px; }
    
    /* Cabecera Principal ARKON COMMAND */
    .header-supremo { text-align: center; border-bottom: 2px solid #ff0000; padding-bottom: 10px; margin-bottom: 20px; box-shadow: 0px 4px 10px rgba(255, 0, 0, 0.1); }
    .titulo-supremo { color: #ff0000; font-size: 45px; font-weight: bold; text-shadow: 0px 0px 20px #ff0000; letter-spacing: 6px; margin: 0; }
    .sub-supremo { color: #ff6666; font-size: 11px; letter-spacing: 4px; font-weight: bold; opacity: 0.9; margin-top: 5px; }
    
    /* NÚCLEO CENTRAL HOLOGRÁFICO: ESFERA DE PLASMA LÍQUIDO EN MOVIMIENTO ROTATIVO */
    .wrapper-holograma { display: flex; flex-direction: column; justify-content: center; align-items: center; height: 320px; position: relative; }
    
    .scanner-facial-box {
        position: relative; width: 260px; height: 260px; border: 1px dashed rgba(255, 0, 0, 0.3); border-radius: 4px; display: flex; justify-content: center; align-items: center; overflow: hidden;
    }
    .laser-hud {
        position: absolute; width: 100%; height: 2px; background: linear-gradient(to right, transparent, #ff0000, transparent); box-shadow: 0px 0px 12px #ff0000; animation: barridoLaser 3.5s ease-in-out infinite alternate; z-index: 12;
    }
    
    /* Capas del Radar Giratorio */
    .anillo-plasma-1 { position: absolute; width: 220px; height: 220px; border: 1px dotted rgba(255, 0, 0, 0.4); border-radius: 50%; animation: girarCW 30s linear infinite; }
    .anillo-plasma-2 { position: absolute; width: 190px; height: 190px; border: 2px dashed #ff0000; border-radius: 50%; animation: girarCCW 15s linear infinite; opacity: 0.6; }
    
    /* El núcleo esférico de plasma líquido de la foto */
    .plasma-core { 
        width: 140px; height: 140px; border-radius: 50%; position: absolute; 
        background: radial-gradient(circle, rgba(255,0,0,0.15) 0%, rgba(0,0,0,1) 85%); 
        border: 2px solid #ff0000; display: flex; justify-content: center; align-items: center; 
        box-shadow: 0px 0px 40px #ff0000, inset 0px 0px 20px rgba(255, 0, 0, 0.5); z-index: 10; 
    }
    
    /* Animación reactiva cuando está en modo SPEAKING */
    .plasma-core.activado {
        animation: pulsarHablando 0.4s ease-in-out infinite alternate;
        border-color: #ffffff;
        box-shadow: 0px 0px 50px #ffffff, inset 0px 0px 25px rgba(255, 255, 255, 0.6);
    }
    
    /* Movimiento continuo de las olas internas del plasma */
    .plasma-core::before {
        content: ""; position: absolute; width: 240px; height: 240px; background-color: rgba(255, 0, 0, 0.25); 
        top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 38%; animation: girarCW 6s linear infinite;
    }
    
    .letra-plasma { color: #ffffff; font-family: sans-serif; font-size: 65px; font-weight: bold; position: relative; z-index: 15; text-shadow: 0px 0px 15px #ffffff, 0px 0px 30px #ff0000; }
    
    /* Animación del Ecualizador de Ondas de Sonido */
    .wave-container { display: flex; justify-content: center; align-items: center; gap: 3px; height: 30px; margin-top: 10px; }
    .wave-bar { width: 3px; height: 15px; background-color: #ff0000; animation: latidoAudio 0.6s ease-in-out infinite alternate; }
    .wave-bar:nth-child(2) { animation-delay: 0.1s; }
    .wave-bar:nth-child(3) { animation-delay: 0.2s; }
    .wave-bar:nth-child(4) { animation-delay: 0.3s; }
    .wave-bar:nth-child(5) { animation-delay: 0.4s; }
    
    /* Barras de Carga del Sistema (CPU / Memoria) */
    .progress-hud { background-color: rgba(255,0,0,0.1); border: 1px solid #ff0000; height: 12px; border-radius: 2px; margin-bottom: 8px; overflow: hidden; }
    .bar-fill { background-color: #ff0000; height: 100%; box-shadow: 0px 0px 8px #ff0000; }
    
    /* ANIMACIONES CSS */
    @keyframes girarCW { 100% { transform: translate(-50%, -50%) rotate(360deg); } }
    @keyframes girarCCW { 100% { transform: rotate(-360deg); } }
    @keyframes barridoLaser { 0% { top: 0%; } 100% { top: 100%; } }
    @keyframes latidoAudio { 0% { height: 5px; } 100% { height: 28px; } }
    @keyframes pulsarHablando { 0% { transform: scale(1); } 100% { transform: scale(1.06); } }
    
    /* Campos de Entrada Modificados */
    .stTextInput>div>div>input { background-color: #0a0000; color: #ff4444; border: 1px solid #ff0000; font-family: monospace; }
    .stSuccess { background-color: #120000; color: #ff9999; border: 1px solid #ff0000; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA GENERAL DEL CENTRO DE MANDO
st.markdown('<div class="header-supremo"><div class="titulo-supremo">ARKON COMMAND</div><div class="sub-supremo">BIOMETRIC INTERFACE // HYDRO-CORE 3D ACTIVE</div></div>', unsafe_allow_html=True)

# CONTROL INTERACTIVO DE RECONOCIMIENTO SUGERIDO POR CHATGPT
st.markdown("### 🎙️ REGISTRO TÁCTICO DE ENTRADA")
audio_value = st.audio_input("Transmitir comando de voz a Arkon:")

# Evaluación del estado del micrófono para activar el núcleo reactivo
audio_activo = audio_value is not None
clase_nucleo = "plasma-core activado" if audio_activo else "plasma-core"

# DISTRIBUCIÓN COLUMNAS TÁCTICAS (CALCADO DE LA FOTO)
col_izq, col_centro, col_der = st.columns([1.2, 1.6, 1.2])

with col_izq:
    st.markdown("""
        <div class="panel-militar">
            <div class="titulo-seccion">🕵️ RASTREO BIOMÉTRICO</div>
            <p class="status-green">● DETECCIÓN FACIAL: ONLINE</p>
            <p class="status-red">● NÚCLEO LÍQUIDO 3D: ESTABLE</p>
            <p class="status-yellow">● ESCÁNER LÁSER: EN EJECUCIÓN</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-militar">
            <div class="titulo-seccion">⏱️ RELOJ DE SECUENCIA</div>
            <h3 style="color:#ff0000; font-size:32px; margin:5px 0; text-align:center; font-weight:bold; letter-spacing:2px; text-shadow: 0 0 10px #ff0000;">{datetime.datetime.now().strftime('%H:%M:%S')}</h3>
            <p style="font-size:9px; color:#aa0000; text-align:center; text-transform:uppercase;">Eje Temporal del Búnker</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="panel-militar">
            <div class="titulo-seccion">📊 ESTADO DEL SISTEMA</div>
            <p style="font-size:11px; margin:2px 0;">CPU USAGE [64%]</p>
            <div class="progress-hud"><div class="bar-fill" style="width: 64%;"></div></div>
            <p style="font-size:11px; margin:2px 0;">MEMORY [72%]</p>
            <div class="progress-hud"><div class="bar-fill" style="width: 72%;"></div></div>
            <p style="font-size:11px; margin:2px 0;">SECURITY [100%]</p>
            <div class="progress-hud"><div class="bar-fill" style="width: 100%;"></div></div>
            <p class="status-green" style="font-size:10px; margin-top:5px;">ALL SYSTEMS OPERATIONAL // AUTHORIZATION ALFA</p>
        </div>
    """, unsafe_allow_html=True)

with col_centro:
    # RECONSTRUCCIÓN CON INTERFAZ CONCATENADA PURA (CERO COMILLAS TRIPLES SUELTAS)
    texto_estado_holograma = "SPEAKING // PROCESSING" if audio_activo else "HABLANDO..."
    
    html_centro_melo = "<div class='wrapper-holograma'>"
    html_centro_melo += "  <div class='scanner-facial-box'>"
    html_centro_melo += "    <div class='laser-hud'></div>"
    html_centro_melo += "    <div class='anillo-plasma-1'></div>"
    html_centro_melo += "    <div class='anillo-plasma-2'></div>"
    html_centro_melo += "    <div class='" + clase_nucleo + "'>"
    html_centro_melo += "      <div class='letra-plasma'>サ</div>"
    html_centro_melo += "    </div>"
    html_centro_melo += "  </div>"
    html_centro_melo += "  <p style='color:#ff3333; font-size:11px; letter-spacing:3px; margin-top:15px; font-weight:bold;'>" + texto_estado_holograma + "</p>"
    html_centro_melo += "  <div class='wave-container'>"
