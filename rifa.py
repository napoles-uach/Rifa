import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
st.title('Rifa de Halloween 🎃 👻 ')
st.markdown('# Apoyo a [Dante](https://www.youtube.com/channel/UCd_08SA9p1BIGuT-BW_rR9g) 🎩')
st.markdown('## Premio: Una Tablet con Teclado 💻 (con valor de $3000)')
st.markdown('## Valor del Boleto: $50')
st.markdown('Ganador: Últimas 2 cifras del Primer Lugar de la Lotería Nacional del 31 de Octubre 2021.')


df = pd.read_csv('https://raw.githubusercontent.com/napoles-uach/Rifa/main/Rifa_Halloween_boletos.csv')
# Put your Python+Streamlit code here ...
# you can modify it by double cliking on the folder icon at the left
#st.dataframe(df)

st.write('# Números disponibles:')
disponible=df[df['ocupado']==0]

#numb=st.selectbox('Terminaciones disponibles',disponible)

#boton=st.button(str(numb))

#if boton:
#  st.balloons()

st.write(disponible['Num'])
#sel_url='https://www.youtube.com/user/VideotecaLotenal/videos'

st.markdown('# [Link al canal de Youtube de la Lotería Nacional](https://www.youtube.com/user/VideotecaLotenal/videos) Transmisión a las 20:00 Horas en Cd. de México')
#components.iframe(sel_url,height=800,scrolling=True)

st.sidebar.image('tablet.png')
st.sidebar.markdown('''
Características

* Pantalla 10.1´´ IPS
* Resolución 1280 x 800
* Cámara Trasera + Frontal
* Quadcore 1.5 GHz
* Memoria RAM 2 GB
* Almacenamiento interno 32 GB
* Ranura Tarjeta TF 32 GB (No inc.)
* Conexión WiFi y BT
* Entrada USB
* Entrada 3.5 mm
* Android 10.1
* Batería 4000 mAh

Contenido
* 1 Tablet 10.1´´
* 1 Teclado inalámbrico
* Manual de Usuario
''')