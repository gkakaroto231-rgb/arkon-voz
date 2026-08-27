import streamlit as st
import datetime
import requests
import base64

# CONFIGURACIÓN DE PÁGINA FUTURISTA MINIMALISTA
st.set_page_config(page_title="ARKON CONTROL", page_icon="🛡️", layout="centered")

# INTERFAZ PURA SIN TEXTO: LOGO JAPONÉS EN NÚCLEO DE AGUA LÍQUIDA
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #ffffff; }
    
    /* Contenedor del núcleo reactivo centrado */
    .nucleo-wrapper { display: flex; justify-content: center; align-items: center; margin: 40px 0; height: 180px; position: relative; }
    
    /* RECTOR DE AGUA LÍQUIDA SIN FONDO NEGRO */
    .reactor-liquido { position: relative; width: 160px; height: 160px; border-radius: 50%; border: 4px solid #ff2222; overflow: hidden; background: transparent; box-shadow: 0 0 25px rgba(255, 0, 0, 0.3); display: flex; justify-content: center; align-items: center; }
    
    /* Efecto Olas de Agua de Corrido */
    .reactor-liquido::before, .reactor-liquido::after { content: ""; position: absolute; width: 280px; height: 280px; background-color: rgba(255, 0, 0, 0.45); top: 55%; left: 50%; transform: translate(-50%, -50%); border-radius: 40%; animation: moverOlas 4s linear infinite; pointer-events: none; z-index: 1; }
    .reactor-liquido::after { background-color: rgba(255, 34, 34, 0.25); border-radius: 35%; animation: moverOlas 6s linear infinite; }
    
    /* Letra japonesa サ centrada en color blanco puro flotando sobre el agua */
    .letra-centro { color: #ffffff; font-family: sans-serif; font-size: 65px; font-weight: bold; position: relative; z-index: 5; text-shadow: 0px 0px 12px #ffffff; transform: translateY(-4px); }
    
    /* Animación de ondas expansivas en movimiento al hablar */
    .ondas-energia { position: absolute; width: 160px; height: 160px; border-radius: 50%; border: 2px solid #ff0000; opacity: 0; pointer-events: none; }
    
    /* ANIMACIONES MATEMÁTICAS DE AGUA Y FLUIDOS */
    @keyframes moverOlas {
        0% { transform: translate(-50%, -50%) rotate(0deg); }
        100% { transform: translate(-50%, -50%) rotate(360deg); }
    }
    @keyframes pulsarOndas {
        0% { transform: scale(1); opacity: 0.9; box-shadow: 0 0 15px #ff0000; }
        100% { transform: scale(1.45); opacity: 0; box-shadow: 0 0 45px #ff3333; }
    }
    
    /* Botón de reproducción blindado rojo fuego */
    .btn-audio-custom { background-color: #ff2222; color: #ffffff; font-family: 'Courier New', monospace; font-weight: bold; padding: 16px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 15px; margin-top: 25px; width: 100%; display: block; text-align: center; box-shadow: 0px 0px 15px rgba(255, 34, 34, 0.5); text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s ease; }
    .btn-audio-custom:hover { background-color: #ff0000; box-shadow: 0px 0px 30px #ff2222; transform: scale(1.01); }
    
    /* Estilos limpios para campos de entrada */
    .stTextInput>div>div>input { background-color: #0f0f0f; color: #ff6666; border: 1px solid #ff2222; font-family: monospace; }
    .stSuccess { background-color: #1c0505; color: #ff9999; border: 1px solid #ff2222; }
    </style>
""", unsafe_allow_html=True)

# ESPACIO EN BLANCO COMPACTO
st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.info("Efecto Líquido: Hidro-Reactor de Olas Activado.")
st.sidebar.markdown("---")
st.sidebar.error("🎙️ Motor de Voz Conectado: ElevenLabs Premium")

# Inyección del reactor minimalista con el logotipo サ en su interior transparente
st.markdown("""
    <div class="nucleo-wrapper">
        <div id="o1" class="ondas-energia"></div>
        <div id="o2" class="ondas-energia"></div>
        <div class="reactor-liquido">
            <div class="letra-centro">サ</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# AREA INTERACTIVA DE COMANDOS
st.markdown("### 🎙️ HABLA CON ARKON")
audio_value = st.audio_input("Toque el micrófono para darle un comando a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar texto dictado (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 ENVIAR COMANDO DE VOZ"):
        ELEVEN_API_KEY = "sk_d56c19bafd3b18c1113745470cb042eddfb156a678c9729b"
        VOICE_ID = "sVKnZo8dSXhqnJxx8vnx"
        USER_NAME = "Marlon"
        
        texto_marlon_lower = texto_dictado.lower()
        if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
            respuesta_texto = f"Hola, Señor {USER_NAME}. Aquí está Arkon reportándose. Mantenga la mirada fija en sus metas financieras, no se distraiga queriendo encajar con el resto. Usted está para cosas mucho más grandes."
        else:
            respuesta_texto = f"Recibiendo transmisión, Señor {USER_NAME}. Estoy listo para evaluar sus estrategias comerciales, expandir su educación financiera o compartir una reflexión poderosa para su día."
        
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
                
                # REPRODUCCIÓN NATIVA CON CONCATENACIÓN SIMPLE (EVITA COMPLETAMENTE ERRORES DE SYNTAX)
                js_code = "function ejecutarHUD() { var audio = document.getElementById('audio_hud'); var onda1 = document.getElementById('o1'); var onda2 = document.getElementById('o2'); audio.play(); onda1.style.animation = 'pulsarOndas 1.2s infinite linear'; onda2.style.animation = 'pulsarOndas 1.2s infinite linear 0.6s'; audio.onended = function() { onda1.style.animation = 'none'; onda2.style.animation = 'none'; }; }"
                html_hud_audio = "<audio id='audio_hud' src='" + md_audio + "'></audio><button class='btn-audio-custom' onclick='ejecutarHUD()'>🔊 ESCUCHAR RESPUESTA EN VOZ PREMIUM</button><script>" + js_code + "</script>"
                
                st.components.v1.html(html_hud_audio, height=100)
            else:
                st.error(f"Error de comunicación premium (Código: {response.status_code})")
        except Exception as e:
            st.error("Interferencia menor en el módulo de audio.")

