import streamlit as st
import datetime
import yfinance as yf

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO TÁCTICO ORIGINAL
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# Inicializar la memoria del chat en el servidor para que no se borre la conversación
if "historial_arkon" not in st.session_state:
    st.session_state.historial_arkon = []

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO S&P 500
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "5,278.40"

# ESTILIZACIÓN DE ALTA TECNOLOGÍA EN ROJO FUEGO MILITAR (SU INTERFAZ ORIGINAL)
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
    
    /* MODULACIÓN DEL MICRÓFONO PLANO FLOTANTE SIN LA BARRA GRIS ORIGINAL */
    div[data-testid="stAudioInput"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    div[data-testid="stAudioInput"] > div {
        display: none !important;
    }

    .microfono-bunker-box {
        background-color: #000000;
        border: 1px solid #ff0000;
        border-radius: 4px;
        padding: 15px;
        display: flex;
        align-items: center;
        gap: 20px;
        margin-top: 15px;
        box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.2);
        position: relative;
    }
    .circulo-mic {
        width: 50px;
        height: 50px;
        border: 2px solid #ff0000;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 0px 15px #ff0000;
    }
    .icono-mic { color: #ffffff; font-size: 24px; text-shadow: 0px 0px 10px #ff0000; }
    .info-mic { display: flex; flex-direction: column; justify-content: center; flex-grow: 1; }
    .texto-mic-activo { color: #ff3333; font-size: 11px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px; }
    
    .contenedor-ondas { display: flex; align-items: center; gap: 3px; height: 20px; }
    .barra-onda { width: 3px; height: 10px; background-color: #ff0000; box-shadow: 0px 0px 5px #ff0000; animation: latirOnda 0.5s ease-in-out infinite alternate; }
    .barra-onda:nth-child(2n) { animation-delay: 0.1s; }
    .barra-onda:nth-child(3n) { animation-delay: 0.2s; }
    .barra-onda:nth-child(4n) { animation-delay: 0.3s; }
    
    @keyframes latirOnda { 0% { height: 4px; } 100% { height: 18px; } }
    
    /* DISEÑO EXCLUSIVO DEL HISTORIAL DE TRANSMISIONES COMPACTO Y EXTRA FINO */
    .chat-box-hud {
        background-color: rgba(10, 2, 2, 0.85);
        border: 1px solid #ff1111;
        border-radius: 4px;
        padding: 12px;
        max-height: 200px;
        overflow-y: auto;
        font-family: monospace;
        font-size: 11px;
        margin-top: 10px;
        box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.15);
    }
    .msg-marlon { color: #38bdf8; margin: 3px 0; font-weight: bold; }
    .msg-arkon { color: #ff3333; margin: 3px 0 8px 0; line-height: 1.3; }
    
    /* Botón Táctico Pequeño */
    .stButton>button {
        background-color: #1a0303 !important;
        color: #ff6666 !important;
        border: 1px solid #ff2222 !important;
        font-family: monospace !important;
        font-size: 11px !important;
        font-weight: bold !important;
        width: 100%;
        margin-top: 5px;
    }
    .stButton>button:hover {
        background-color: #ff2222 !important;
        color: #ffffff !important;
        box-shadow: 0px 0px 10px #ff2222;
    }

    .stTextInput>div>div>input { background-color: #050505; color: #ff6666; border: 1px solid #ff2222; font-family: monospace; }
    .stSuccess { background-color: #1a0303; color: #ff9999; border: 1px solid #ff2222; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA GENERAL DEL TABLERO
st.markdown('<div class="header-arkon"><div class="titulo-principal">ARKON</div><div class="sub-principal">SISTEMA DE INTELIGENCIA AVANZADA</div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.success("🎙️ Registrador: Bitácora de Enlace Lista")

# DISTRIBUCIÓN DEL TABLERO CON SUS 2 CUADROS ORIGINALES POR LADO
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
            <p style="color:#888; font-size:10px; margin:5px 0 0 0;">Canal de comunicación táctica local habilitado.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="panel-tactico">
            <div class="titulo-panel">🛡️ MERCADOS</div>
            <p style="color:#ffaa00; font-size:11px; margin:0;">S&P 500 INDEX</p>
            <h4 style="color:#ffffff; font-size:16px; margin:2px 0;">{precio_sp} PTS</h4>
        </div>
    """, unsafe_allow_html=True)

# INTERFAZ INTERACTIVA DEL MICRÓFONO PREMIUM REPLICADO
st.markdown("""
    <div class="microfono-bunker-box">
        <div class="circulo-mic"><span class="icono-mic">🎙️</span></div>
        <div class="info-mic">
            <div class="texto-mic-activo">MICRÓFONO ACTIVO // RECONOCIMIENTO SISTEMA</div>
            <div class="contenedor-ondas">
                <div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div>
                <div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Capturador oculto de audio para procesar el dictado por voz
audio_value = st.audio_input("Registro oculto:")

# Crear la división táctica en la parte inferior para alojar el chat manual y el historial melo
col_chat_izq, col_chat_der = st.columns([1.5, 2.5])

entrada_texto_marlon = ""
procesar_entrada = False

with col_chat_izq:
    # 🔳 EL CUADRITO PEQUEÑO Y BONITO PARA ESCRIBIR COMANDOS MANUALES
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    entrada_texto_marlon = st.text_input("💻 INYECTAR COMANDO MANUAL (ESCRIBIR):", key="input_manual_marlon")
    if st.button("🚀 ENVIAR REGISTRO"):
        if entrada_texto_marlon.strip() != "":
            procesar_entrada = True
            texto_final_entrada = entrada_texto_marlon

# Evaluar si la señal vino por el micrófono de fábrica
if audio_value and not procesar_entrada:
    procesar_entrada = True
    texto_final_entrada = "Arkon, buenos días" # Simulación del dictado por voz por defecto

# PROCESAMIENTO GENERAL DE LA INTELIGENCIA TÁCTICA
if procesar_entrada:
    USER_NAME = "Marlon"
    texto_marlon_lower = texto_final_entrada.lower()
    
    if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
        respuesta_texto = f"Buenos días, Señor {USER_NAME}. ARKON se encuentra completamente operativo bajo sus órdenes."
    else:
