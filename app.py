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
    
    /* 🚨 CORTINA DE CARGA SÓNICA CON ANIMACIÓN MILITAR DE ENTRADA */
    .pantalla-carga-arkon {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: #000000; z-index: 99999;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        animation: desaparecerCortina 0.5s ease-in forwards; animation-delay: 2.5s;
        pointer-events: none;
    }
    .texto-carga-neon {
        color: #ff0000; font-size: 16px; font-weight: bold; letter-spacing: 4px;
        text-shadow: 0px 0px 15px #ff0000; margin-bottom: 15px;
        animation: parpadeoAlerta 0.8s infinite alternate;
    }
    .barra-carga-militar {
        width: 250px; height: 4px; background-color: rgba(255,0,0,0.1);
        border: 1px solid #ff0000; border-radius: 2px; overflow: hidden;
    }
    .progreso-carga {
        width: 0%; height: 100%; background-color: #ff0000;
        box-shadow: 0px 0px 10px #ff0000;
        animation: llenarBarra 2.3s ease-out forwards;
    }
    @keyframes desaparecerCortina { 100% { opacity: 0; visibility: hidden; } }
    @keyframes parpadeoAlerta { 0% { opacity: 0.3; } 100% { opacity: 1; } }
    @keyframes llenarBarra { 100% { width: 100%; } }
    </style>
""", unsafe_allow_html=True)

# 🚨 INYECTOR SÓNICO DE BIENVENIDA AUTOMÁTICO (SONIDO SCI-FI DE CARGA EN VIVO)
st.components.v1.html("""
    <div class="pantalla-carga-arkon">
        <div class="texto-carga-neon">INICIALIZANDO NÚCLEO ARKON</div>
        <div class="barra-carga-militar">
            <div class="progreso-carga"></div>
        </div>
    </div>
    <script>
    // Sintetizador de audio web nativo para generar el sonido mecánico de encendido IA
    window.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            try {
                var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                
                // Pulso sónico 1: Frecuencia baja de poder
                var osc1 = audioCtx.createOscillator();
                var gain1 = audioCtx.createGain();
                osc1.type = 'sawtooth';
                osc1.frequency.setValueAtTime(80, audioCtx.currentTime);
                osc1.frequency.exponentialRampToValueAtTime(180, audioCtx.currentTime + 1.5);
                gain1.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain1.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 1.8);
                osc1.connect(gain1);
                gain1.connect(audioCtx.destination);
                
                // Pulso sónico 2: Pitido digital de confirmación
                var osc2 = audioCtx.createOscillator();
                var gain2 = audioCtx.createGain();
                osc2.type = 'sine';
                osc2.frequency.setValueAtTime(880, audioCtx.currentTime + 1.2);
                gain2.gain.setValueAtTime(0.0, audioCtx.currentTime);
                gain2.gain.setValueAtTime(0.1, audioCtx.currentTime + 1.2);
                gain2.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 1.6);
                osc2.connect(gain2);
                gain2.connect(audioCtx.destination);
                
                osc1.start(); osc1.stop(audioCtx.currentTime + 1.8);
                osc2.start(audioCtx.currentTime + 1.2); osc2.stop(audioCtx.currentTime + 1.6);
            } catch(e) { console.log("Interferencia de audio mitigada"); }
        }, 300);
    });
    </script>
""", height=0, width=0)

# CABECERA GENERAL DEL TABLERO
st.markdown('<div class="header-arkon"><div class="titulo-principal">ARKON</div><div class="sub-principal">SISTEMA DE INTELIGENCIA AVANZADA</div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.success("🎙 => Registrador: Bitácora de Enlace Lista")

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
