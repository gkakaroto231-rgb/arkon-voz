import streamlit as st
import datetime
import yfinance as yf

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO TÁCTICO ORIGINAL
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# Inicializar la memoria del chat en el servidor para que no se borre la conversación
if "historial_arkon" not in st.session_state:
    st.session_state.historial_arkon = []

# OBTENER DATOS REALES DE LA BOLSA Y NOTICIAS CON IMÁGENES
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
    # Extraer las noticias reales completas de Yahoo Finance / yfinance
    noticias_reales = ticker_sp.news[:3]  # Tomamos las 3 más frescas con imágenes y números
except:
    precio_sp = "5,640.15"
    noticias_reales = []

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
    
    /* DISEÑO EXCLUSIVO DEL HISTORIAL DE TRANSMISIONES COMPACTO */
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
st.sidebar.success("🎙️ Mercados: Terminal de Noticias Conectada")

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
    st.markdown(f"""
        <div class="panel-tactico">
            <div class="titulo-panel">🛡️ MERCADOS INDEX</div>
            <p style="color:#ffaa00; font-size:11px; margin:0;">S&P 500 REALS</p>
            <h4 style="color:#ffffff; font-size:22px; margin:2px 0; font-weight:bold; letter-spacing:1px;">{precio_sp} PTS</h4>
        </div>
    """, unsafe_allow_html=True)

    # 🔳 BOLETÍN MULTIMEDIA BLINDADO - CONEXIÓN CON NOTICIAS EN VIVO RESPETANDO SANGRIAS DE PYTHON
    with st.container():
        st.markdown('<div class="panel-tactico"><div class="titulo-panel">📰 TITULARES DE LA BOLSA EN VIVO</div>', unsafe_allow_html=True)
        
        if noticias_reales:
            for idx, n in enumerate(noticias_reales):
                titulo_noticia = n.get('title', 'Actualización de mercado')
                fuente_noticia = n.get('publisher', 'MERCADO')
                link_noticia = n.get('link', 'https://yahoo.com')
                
                # Extraer miniatura o logotipo de la noticia de corrido
                imagen_noticia = None
                if 'thumbnail' in n and 'resolutions' in n['thumbnail'] and n['thumbnail']['resolutions']:
                    imagen_noticia = n['thumbnail']['resolutions'][0].get('url', None)
                
                # Impresión de textos planos limpios para evitar que falle Render
                st.markdown(f"<p style='color:#ffaa00; font-size:10px; font-weight:bold; margin: 0 0 2px 0;'>📡 {fuente_noticia}</p>", unsafe_allow_html=True)
                if imagen_noticia:
                    st.image(imagen_noticia, width=120)
                st.markdown(f"<p style='font-size:11px; margin: 0 0 5px 0; line-height:1.2;'>{titulo_noticia}</p>", unsafe_allow_html=True)
                st.link_button("🌐 VER PORTADA COMPLETA", link_noticia)
                st.markdown("<p style='color:rgba(255,34,34,0.2); margin:4px 0;'>- - - - - - - - - - - - - - - - - - - -</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:#666; font-size:11px; text-align:center; margin:10px 0;'>CONECTANDO CON WALL STREET...</p>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

# AREA INTERACTIVA DEL MICRÓFONO PREMIUM REPLICADO
st.markdown("""
    <div class="microfono-bunker-box">
        <div class="circulo-mic"><span class="icono-mic">🎙️</span></div>
        <div class="info-mic">
            <div class="texto-mic-activo">MICRÓFONO ACTIVO // RECONOCIMIENTO SISTEMA</div>
            <div class="contenedor-ondas">
                <div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div><div class="barra-onda"></div>
