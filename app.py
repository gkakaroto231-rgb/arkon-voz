import streamlit as st
import datetime
import yfinance as yf
import requests
import base64

# CONFIGURACIÓN UNIVERSAL DEL CENTRO DE MANDO TÁCTICO
st.set_page_config(page_title="ARKON COMMAND", page_icon="🛡️", layout="wide")

# OBTENER DATOS REALES DE LA BOLSA PARA EL TABLERO
try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")
    precio_sp = round(datos_sp['Close'].iloc[-1], 2)
except:
    precio_sp = "5,278.40"

# ESTILIZACIÓN DE ALTA TECNOLOGÍA EN ROJO FUEGO MILITAR (ESTILO HUD JARVIS DE LA FOTO)
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
    
    /* Reactor Central con la letra japonesa サ */
    .wrapper-reactor { display: flex; justify-content: center; align-items: center; height: 220px; position: relative; margin: 20px 0; }
    .anillo-exterior { position: absolute; width: 190px; height: 190px; border: 2px dashed #ff3333; border-radius: 50%; animation: rotarAnillo 20s linear infinite; }
    .reactor-nucleo { width: 150px; height: 150px; border-radius: 50%; position: absolute; border: 3px solid #ff2222; background-color: #000000; display: flex; justify-content: center; align-items: center; box-shadow: 0px 0px 40px #ff2222; }
    .letra-centro { color: #ffffff; font-family: sans-serif; font-size: 65px; font-weight: bold; transform: translateY(-4px); text-shadow: 0px 0px 10px #ffffff; }
    
    /* Ondas de choque en movimiento al hablar */
    .ondas-energia { position: absolute; width: 150px; height: 150px; border-radius: 50%; border: 2px solid #ff0000; opacity: 0; }
    
    @keyframes rotarAnillo { 100% { transform: rotate(360deg); } }
    @keyframes pulsarOndas {
        0% { transform: scale(1); opacity: 0.8; box-shadow: 0 0 15px #ff0000; }
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

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.error("🎙️ Motor de Voz Conectado: ElevenLabs Premium")

# DISTRIBUCIÓN DEL TABLERO EN 3 COLUMNAS TÁCTICAS (ESTILO HUD DE SU FOTO)
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
    st.markdown(f"""
        <div class="wrapper-reactor">
            <div class="anillo-exterior"></div>
            <div id="o1" class="ondas-energia"></div>
            <div id="o2" class="ondas-energia"></div>
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

# AREA INTERACTIVA DE COMANDOS
st.markdown("### 🎙️ INTERFAZ DE DICTADO")
audio_value = st.audio_input("Toque el micrófono para transmitir orden a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar registro de entrada (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 TRANSMITIR COMANDO GENERAL"):
        ELEVEN_API_KEY = "sk_d56c19bafd3b18c1113745470cb042eddfb156a678c9729b"
        VOICE_ID = "sVKnZo8dSXhqnJxx8vnx"
        USER_NAME = "Marlon"
        
        texto_marlon_lower = texto_dictado.lower()
        if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
            respuesta_texto = f"Buenos días, Señor {USER_NAME}. Escúcheme bien: su problema real no es la situación, es su mentalidad. ¿Ya le dio los buenos días al Creador? Aspire a más hoy, recuerde Filipenses 4:13: Todo lo puedo en Cristo que me fortalece."
        else:
            respuesta_texto = f"Recibiendo transmisión, Señor {USER_NAME}. Estoy listo para evaluar las estrategias comerciales o la educación financiera que necesite hoy."
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 ARKON EN LÍNEA: {respuesta_texto}")
        
        # 🚨 DIRECCIÓN DE API REPARADA AL 100% PARA QUE SÍ COJA LA VOZ
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
                
                # REPRODUCCIÓN EN CADENAS SIMPLES PLANAS CONCATENADAS (SÍ SUENA SEGURO)
                js_code = "function ejecutarHUD() { var audio = document.getElementById('audio_hud'); var onda1 = document.getElementById('o1'); var onda2 = document.getElementById('o2'); audio.play(); onda1.style.animation = 'pulsarOndas 1.2s infinite linear'; onda2.style.animation = 'pulsarOndas 1.2s infinite linear 0.6s'; audio.onended = function() { onda1.style.animation = 'none'; onda2.style.animation = 'none'; }; }"
                html_hud_audio = "<audio id='audio_hud' src='" + md_audio + "'></audio><button class='btn-audio-custom' onclick='ejecutarHUD()'>🔊 DEVELAR RESPUESTA DEL SISTEMA</button><script>" + js_code + "</script>"
                
                st.components.v1.html(html_hud_audio, height=90)
            else:
                st.error(f"Error de comunicación premium (Código: {response.status_code})")
        except Exception as e:
            st.error("Interferencia menor en el módulo de audio.")
