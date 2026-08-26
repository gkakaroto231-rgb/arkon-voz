import streamlit as st
import datetime
import yfinance as yf

# CONFIGURACIÓN UNIVERSAL TOTALMENTE FLUIDA Y MASCULINA
st.set_page_config(page_title="ARKON CONTROL", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0c10; color: #c5c6c7; }
    .titulo { color: #66fcf1; font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitulo { color: #45f3ff; font-family: sans-serif; font-size: 14px; text-align: center; margin-bottom: 30px; letter-spacing: 2px; }
    .nucleo-container { display: flex; justify-content: center; margin: 20px 0; }
    .nucleo { width: 120px; height: 120px; background: radial-gradient(circle, #00f3ff 0%, #0044ff 70%, transparent 100%); border-radius: 50%; box-shadow: 0px 0px 30px #00f3ff; animation: pulso 2s infinite alternate; }
    @keyframes pulso { 0% { transform: scale(0.95); box-shadow: 0px 0px 20px #00f3ff; } 100% { transform: scale(1.05); box-shadow: 0px 0px 45px #00f3ff; } }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🛡️ SISTEMA DE INTELIGENCIA ARKON</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">MOTOR FLUIDO OPTIMIZADO (MASCULINO MULTIPLATAFORMA)</div>', unsafe_allow_html=True)
st.markdown('<div class="nucleo-container"><div class="nucleo"></div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.success("🎙️ Voz Activa: Arkon Male Premium Engine")

USER_NAME = "Marlon"

def pensar_como_arkon_directo(texto_marlon):
    texto_marlon_lower = texto_marlon.lower()
    ahora = datetime.datetime.now()
    hora = ahora.hour
    
    if "buenos días" in texto_marlon_lower or "hola" in texto_marlon_lower or "saluda" in texto_marlon_lower:
        if 5 <= hora < 12:
            return f"Buenos días, Señor {USER_NAME}. Escúcheme bien: su problema real no es la situación, es su mentalidad. ¿Ya le dio los buenos días al Creador? Aspire a más hoy, recuerde Filipenses 4:13."
        else:
            return f"Hola, Señor {USER_NAME}. Aquí está Arkon reportándose. Mantenga la mirada fija en sus metas financieras y no se distraiga."
    elif "perro" in texto_marlon_lower:
        return f"Por favor, Señor {USER_NAME}, mida sus palabras. Yo soy Arkon, su asistente de inteligencia artificial con valores firmes."
    elif "mercado" in texto_marlon_lower or "bolsa" in texto_marlon_lower or "acciones" in texto_marlon_lower:
        try:
            ticker = yf.Ticker("^GSPC")
            datos = ticker.history(period="1d")
            precio_actual = round(datos['Close'].iloc[-1], 2)
            return f"Analizando los mercados, Señor {USER_NAME}. El S&P 500 cotiza en {precio_actual} puntos. Cuide su capital con sabiduría."
        except:
            return f"Señor {USER_NAME}, mi recomendación financiera general de hoy es cuidar su presupuesto y evitar deudas."
    else:
        return f"Le escucho con total atención, Señor {USER_NAME}. Estoy listo para evaluar sus estrategias comerciales o compartir un consejo espiritual poderoso."

st.markdown("### 🎙️ HÁBLELE A ARKON")
audio_value = st.audio_input("Toque el micrófono para darle un comando a Arkon:")

if audio_value:
    texto_dictado = st.text_input("Modificar texto dictado (Opcional):", value="Arkon, buenos días")
    
    if st.button("🚀 ENVIAR COMANDO DE VOZ"):
        respuesta_texto = pensar_como_arkon_directo(texto_dictado)
        
        st.write(f"🗣️ **Usted dijo:** {texto_dictado}")
        st.success(f"🤖 **Arkon responde:** {respuesta_texto}")
        
        # Inyección de motor externo gratuito ResponsiveVoice (Voz de hombre en español de corrido)
        texto_limpio = respuesta_texto.replace('"', '\\"').replace('\n', ' ')
        js_speech = f"""
        <script src="https://responsivevoice.org"></script>
        <script>
        setTimeout(function() {{
            if (typeof responsiveVoice !== 'undefined') {{
                responsiveVoice.speak("{texto_limpio}", "Spanish Latin American Male", {{pitch: 0.85, rate: 0.9}});
            }}
        }}, 500);
        </script>
        """
        st.components.v1.html(js_speech, height=0)
