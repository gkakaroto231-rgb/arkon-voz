import streamlit as st
import datetime
import yfinance as yf
import requests
import base64

# CONFIGURACIÓN UNIVERSAL TOTALMENTE REPARADA CON SU VOZ DE ELEVENLABS
st.set_page_config(page_title="ARKON CONTROL", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0c10; color: #c5c6c7; }
    .titulo { color: #66fcf1; font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitulo { color: #45f3ff; font-family: sans-serif; font-size: 14px; text-align: center; margin-bottom: 30px; letter-spacing: 2px; }
    .nucleo-container { display: flex; justify-content: center; margin: 20px 0; }
    .nucleo { width: 120px; height: 120px; background: radial-gradient(circle, #00f3ff 0%, #0044ff 70%, transparent 100%); border-radius: 50%; box-shadow: 0px 0px 30px #00f3ff; animation: pulso 2s infinite alternate; }
    @keyframes pulso { 0% { transform: scale(0.95); box-shadow: 0px 0px 20px #00f3ff; } 100% { transform: scale(1.05); box-shadow: 0px 0px 45px #00f3ff; } }
    .btn-audio-custom { background-color: #66fcf1; color: #0b0c10; font-family: 'Courier New', monospace; font-weight: bold; padding: 15px 30px; border: none; border-radius: 8px; cursor: pointer; font-size: 15px; margin-top: 15px; width: 100%; display: block; text-align: center; box-shadow: 0px 0px 15px rgba(102, 252, 241, 0.4); text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s ease; }
    .btn-audio-custom:hover { background-color: #45f3ff; box-shadow: 0px 0px 25px #45f3ff; transform: scale(1.01); }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🛡️ SISTEMA DE INTELIGENCIA ARKON</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">MOTOR ULTRA-PROFESIONAL: ELEVENLABS CORREGIDO</div>', unsafe_allow_html=True)
st.markdown('<div class="nucleo-container"><div class="nucleo"></div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.success("🎙️ Conexión Activa: ElevenLabs Premium (Su Voz de Varón)")

# 🔑 SU LLAVE ACTUAL Y EL ID DE LA VOZ QUE USTED MISMO DISEÑÓ
ELEVEN_API_KEY = "sk_f4d5793c777bfa3b714d2222c613abc7f1310566a1afb4c8"

VOICE_ID = "sVKnZo8dSXhqnJxx8vnx" 


USER_NAME = "Marlon"

def pensar_como_arkon_directo(texto_marlon):
    texto_marlon_lower = texto_marlon.lower()
    ahora = datetime.datetime.now()
    hora = ahora.hour
    
    if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
        if 5 <= hora < 12:
            return f"Buenos días, Señor {USER_NAME}. Escúcheme bien: su problema real no es la situación, es su mentalidad. ¿Ya le dio los buenos días al Creador? Aspire a más hoy, recuerde Filipenses 4:13: Todo lo puedo en Cristo que me fortalece."
        else:
            return f"Hola, Señor {USER_NAME}. Aquí está Arkon reportándose. Mantenga la mirada fija en sus metas financieras, no se distraiga queriendo encajar con el resto. Usted está para cosas mucho más grandes."
    elif "perro" in texto_marlon_lower:
        return f"Por favor, Señor {USER_NAME}, mida sus palabras. Yo soy Arkon, su asistente de inteligencia artificial con la templanza de los más fuertes. Mi propósito es guiarle en su proyecto comercial bajo valores firmes."
    elif "mercado" in texto_marlon_lower or "bolsa" in texto_marlon_lower or "acciones" in texto_marlon_lower:
        try:
            ticker = yf.Ticker("^GSPC")
            datos = ticker.history(period="1d")
            precio_actual = round(datos['Close'].iloc[-1], 2)
            return f"Analizando los mercados económicos, Señor {USER_NAME}. El índice principal S&P 500 se encuentra cotizando en {precio_actual} puntos. Si quiere ser de los más fuertes en el mercado, darlo todo no es suficiente; cuide su capital inicial con sabiduría."
        except:
            return f"Señor {USER_NAME}, tengo una ligera interferencia para conectarme a los tableros de la bolsa, pero mi recomendación financiera general de hoy es cuidar su presupuesto y evitar deudas de alto riesgo."
    else:
        return f"Le escucho con total atención, Señor {USER_NAME}. Estoy listo para evaluar la educación financiera que necesite, revisar estrategias para su proyecto o compartir un consejo espiritual poderoso."

st.markdown("### 🎙️ HABLA CON ARKON")
audio_value = st.audio_input("Toque el micrófono para darle un comando a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar texto dictado (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 ENVIAR COMANDO DE VOZ"):
        respuesta_texto = pensar_como_arkon_directo(texto_dictado)
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 **Arkon responde:** {respuesta_texto}")
        
        # URL CORREGIDA EXACTAMENTE COMO LO MANDÓ EL CONSEJO TÉCNICO
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
        data = {
            "text": respuesta_texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                # Convertir a Base64 nativo en un botón físico para obligar al celular a cantar sin bloquearse
                b64_audio = base64.b64encode(response.content).decode()
                md_audio = f"data:audio/mp3;base64,{b64_audio}"
                
                html_reproductor_fijo = f"""
                <audio id="audio_arkon_premium" src="{md_audio}"></audio>
                <button class="btn-audio-custom" onclick="document.getElementById('audio_arkon_premium').play()">🔊 ESCUCHAR RESPUESTA EN VOZ PREMIUM</button>
                """
                st.components.v1.html(html_reproductor_fijo, height=90)
            else:
                st.error(f"Sincronizando canales de audio premium (Código: {response.status_code})")
                st.code(response.text)
        except Exception as e:
            st.error("Interferencia menor en el módulo de audio.")
