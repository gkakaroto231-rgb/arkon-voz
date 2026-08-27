import streamlit as st
import datetime
import yfinance as yf
import requests
import base64

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="ARKON COMMAND",
    page_icon="🛡️",
    layout="wide"
)

# ============================================================
# ELEVENLABS
# ============================================================

try:
    ELEVEN_API_KEY = st.secrets["ELEVEN_API_KEY"]
except Exception:
    ELEVEN_API_KEY = ""

VOICE_ID = "sVKnZo8dSXhqnJxx8vnx"
USER_NAME = "Marlon"

# ============================================================
# S&P 500
# ============================================================

try:
    ticker_sp = yf.Ticker("^GSPC")
    datos_sp = ticker_sp.history(period="1d")

    if not datos_sp.empty:
        precio_sp = round(float(datos_sp["Close"].iloc[-1]), 2)
    else:
        precio_sp = "N/D"

except Exception:
    precio_sp = "N/D"

# ============================================================
# ESTILO ARKON
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #030303;
    color: #ffffff;
    font-family: 'Courier New', monospace;
}

.panel-tactico {
    background-color: rgba(15, 3, 3, 0.6);
    border: 1px solid #ff2222;
    border-radius: 6px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.1);
}

.titulo-panel {
    color: #ff6666;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-transform: uppercase;
    border-bottom: 1px dashed #ff2222;
    padding-bottom: 4px;
}

.header-arkon {
    text-align: center;
    margin-bottom: 20px;
}

.titulo-principal {
    color: #ff2222;
    font-size: 38px;
    font-weight: bold;
    text-shadow: 0px 0px 20px #ff0000;
    letter-spacing: 5px;
}

.sub-principal {
    color: #ff6666;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: bold;
}

.wrapper-reactor {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 220px;
    position: relative;
    margin: 20px 0;
}

.anillo-exterior {
    position: absolute;
    width: 190px;
    height: 190px;
    border: 2px dashed #ff3333;
    border-radius: 50%;
    animation: rotarAnillo 20s linear infinite;
}

.reactor-nucleo {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    position: absolute;
    border: 3px solid #ff2222;
    background-color: #000000;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 0px 40px #ff2222;
}

.letra-centro {
    color: #ffffff;
    font-family: sans-serif;
    font-size: 65px;
    font-weight: bold;
    transform: translateY(-4px);
    text-shadow: 0px 0px 10px #ffffff;
}

@keyframes rotarAnillo {
    100% {
        transform: rotate(360deg);
    }
}

.stTextInput > div > div > input {
    background-color: #050505;
    color: #ff6666;
    border: 1px solid #ff2222;
    font-family: monospace;
}

.stButton > button {
    background-color: #ff2222;
    color: white;
    border: 1px solid #ff5555;
    font-family: 'Courier New', monospace;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #ff0000;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# CABECERA
# ============================================================

st.markdown("""
<div class="header-arkon">
    <div class="titulo-principal">ARKON</div>
    <div class="sub-principal">
        SISTEMA DE INTELIGENCIA AVANZADA
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")

if ELEVEN_API_KEY:
    st.sidebar.success("🎙️ Motor de Voz: CONECTADO")
else:
    st.sidebar.error("🎙️ Motor de Voz: SIN CLAVE")

# ============================================================
# COLUMNAS
# ============================================================

col_izq, col_centro, col_der = st.columns([1.1, 1.8, 1.1])

# ============================================================
# IZQUIERDA
# ============================================================

with col_izq:

    st.markdown("""
    <div class="panel-tactico">

        <div class="titulo-panel">
            🛡️ ESTADO DEL SISTEMA
        </div>

        <p style="color:#00ff00;font-size:12px;">
            ● CONECTADO
        </p>

        <p style="color:#ff3333;font-size:12px;">
            ● NÚCLEO ESTABLE
        </p>

        <p style="color:#ffaa00;font-size:12px;">
            ● OPERATIVOS 100%
        </p>

    </div>
    """, unsafe_allow_html=True)

    hora = datetime.datetime.now().strftime("%H:%M:%S")

    st.markdown(f"""
    <div class="panel-tactico">

        <div class="titulo-panel">
            🛡️ CRONOLOGÍA LOCAL
        </div>

        <h3 style="
            color:#ff6666;
            text-align:center;
            font-size:20px;
        ">
            {hora}
        </h3>

        <p style="
            font-size:10px;
            color:#888;
            text-align:center;
        ">
            EJE TEMPORAL ACTIVO
        </p>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CENTRO
# ============================================================

with col_centro:

    st.markdown("""
    <div class="wrapper-reactor">

        <div class="anillo-exterior"></div>

        <div class="reactor-nucleo">
            <div class="letra-centro">サ</div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# DERECHA
# ============================================================

with col_der:

    st.markdown("""
    <div class="panel-tactico">

        <div class="titulo-panel">
            🔊 TRANSMISIÓN
        </div>

        <p style="color:#ff6666;font-size:11px;">
            STATUS: LISTO
        </p>

        <p style="color:#888;font-size:10px;">
            Canal de comunicación procesado por ElevenLabs.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="panel-tactico">

        <div class="titulo-panel">
            🛡️ MERCADOS
        </div>

        <p style="color:#ffaa00;font-size:11px;">
            S&P 500 INDEX
        </p>

        <h4 style="color:#ffffff;font-size:16px;">
            {precio_sp} PTS
        </h4>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# MICRÓFONO
# ============================================================

st.markdown("### 🎙️ INTERFAZ DE DICTADO")

audio_value = st.audio_input(
    "Toque el micrófono para transmitir orden a ARKON:"
)

# ============================================================
# PROCESAR COMANDO
# ============================================================

if audio_value:

    texto_dictado = st.text_input(
        "Modificar registro de entrada (Opcional):",
        value="Arkon, buenos días"
    )

    if st.button("🚀 TRANSMITIR COMANDO GENERAL"):

        if not ELEVEN_API_KEY:

            st.error(
                "❌ No se encontró la API KEY de ElevenLabs."
            )

            st.stop()

        texto_marlon_lower = texto_dictado.lower()

        # ====================================================
        # RESPUESTAS
        # ====================================================

        if (
            "buenos días" in texto_marlon_lower
            or "buenos dias" in texto_marlon_lower
            or "hola" in texto_marlon_lower
            or "saluda" in texto_marlon_lower
        ):

            respuesta_texto = (
                f"Buenos días, Señor {USER_NAME}. "
                "Escúcheme bien: su problema real no es "
                "la situación, es su mentalidad. "
                "¿Ya le dio los buenos días al Creador? "
                "Aspire a más hoy. "
                "Recuerde Filipenses 4:13: "
                "Todo lo puedo en Cristo que me fortalece."
            )

        else:

            respuesta_texto = (
                f"Recibiendo transmisión, Señor {USER_NAME}. "
                "Estoy listo para evaluar las estrategias "
                "comerciales o la educación financiera "
                "que necesite hoy."
            )

        # ====================================================
        # MOSTRAR RESPUESTA
        # ====================================================

        st.write(
            f"🗣️ **Usted dijo:** {texto_dictado}"
        )

        st.success(
            f"🤖 ARKON EN LÍNEA: {respuesta_texto}"
        )

        # ====================================================
        # ELEVENLABS API
        # ====================================================

        url = (
            "https://api.elevenlabs.io/v1/"
            f"text-to-speech/{VOICE_ID}"
        )

        headers = {
            "xi-api-key": ELEVEN_API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }

        data = {
            "text": respuesta_texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        # ====================================================
        # ENVIAR
        # ====================================================

        try:

            with st.spinner(
                "🔊 ARKON está sintetizando la transmisión..."
            ):

                response = requests.post(
                    url,
                    json=data,
                    headers=headers,
                    timeout=60
                )

            if response.status_code == 200:

                b64_audio = base64.b64encode(
                    response.content
                ).decode("utf-8")

                md_audio = (
                    "data:audio/mpeg;base64,"
                    + b64_audio
                )

                html_audio = f"""
                <!DOCTYPE html>

                <html>

                <body style="
                    background:transparent;
                    margin:0;
                ">

                <audio
                    id="audio_hud"
                    src="{md_audio}">
                </audio>

                <button
                    onclick="reproducir()"
                    style="
                        background:#ff2222;
                        color:white;
                        font-family:monospace;
                        font-weight:bold;
                        padding:14px;
                        border:1px solid #ff5555;
                        border-radius:4px;
                        cursor:pointer;
                        width:100%;
                        font-size:14px;
                    "
                >
                    🔊 DEVELAR RESPUESTA DEL SISTEMA
                </button>

                <script>

                function reproducir() {{

                    const audio =
                        document.getElementById("audio_hud");

                    audio.currentTime = 0;

                    audio.play().catch(
                        function(error) {{
                            console.log(error);
                        }}
                    );
                }}

                </script>

                </body>

                </html>
                """

                st.components.v1.html(
                    html_audio,
                    height=80
                )

            else:

                st.error(
                    f"❌ ElevenLabs respondió con "
                    f"código {response.status_code}"
                )

                try:
                    st.code(
                        response.json(),
                        language="json"
                    )
                except Exception:
                    st.code(
                        response.text,
                        language="text"
                    )

        except requests.exceptions.Timeout:

            st.error(
                "⏱️ ElevenLabs tardó demasiado en responder."
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "🌐 No se pudo conectar con ElevenLabs."
            )

        except Exception as e:

            st.error(
                "⚠️ Error en el módulo de voz."
            )

            st.code(
                str(e),
                language="text"
            )
