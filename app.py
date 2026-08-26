import streamlit as st
import datetime
import yfinance as yf

# CONFIGURACIÓN UNIVERSAL CON REPRODUCTOR SEGURO ANTI-BLOQUEOS
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
st.markdown('<div class="subtitulo">MOTOR ULTRA-FLUIDO (INTERFAZ DE AUDIO PREMIUM)</div>', unsafe_allow_html=True)
st.markdown('<div class="nucleo-container"><div class="nucleo"></div></div>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ PANEL DE AJUSTES")
st.sidebar.success("🎙️ Conexión Activa: Arkon Universal Speech Engine")

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
        
        # Limpiar el texto para inyectarlo de forma segura en las funciones de audio
        texto_limpio = respuesta_texto.replace('"', '\\"').replace('\n', ' ')
        
        # Inyección forzada de ResponsiveVoice en un botón físico interactivo de alta fidelidad
        html_reproductor_fijo = f"""
        <script src="https://responsivevoice.org"></script>
        <button class="btn-audio-custom" onclick="activarVozArkon()">🔊 ESCUCHAR RESPUESTA (VOZ MASCULINA)</button>
        <script>
        function activarVozArkon() {{
            if (typeof responsiveVoice !== 'undefined') {{
                responsiveVoice.cancel();
                // Forzamos la descarga del archivo de audio del hombre latino de corrido
                responsiveVoice.speak("{texto_limpio}", "Spanish Latin American Male", {{pitch: 0.82, rate: 0.9}});
            }} else {{
                alert("El motor de audio se está sincronizando, por favor presione de nuevo en un segundo.");
            }}
        }}
        </script>
        """
        st.components.v1.html(html_reproductor_fijo, height=90)

