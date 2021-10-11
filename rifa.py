import streamlit as st
import pandas as pd
st.title('Rifa de Halloween 🎃 👻 ')
st.markdown('# Apoyo a [Dante](https://www.youtube.com/channel/UCd_08SA9p1BIGuT-BW_rR9g) 🎩')
st.markdown('## Premio: Una Tablet con Teclado 💻 (con valor de $3000)')
st.markdown('## Valor del Boleto: $50')
st.markdown('Ganador: Número del Primer Lugar de la Lotería Nacional del 31 de Octubre 2021.')

df = pd.read_csv('https://raw.githubusercontent.com/napoles-uach/Rifa/main/Rifa_Halloween_boletos.csv')
# Put your Python+Streamlit code here ...
# you can modify it by double cliking on the folder icon at the left
#st.dataframe(df)
disponible=df[df['ocupado']==0]

numb=st.selectbox('Números disponibles',disponible)

boton=st.button(str(numb))

if boton:
  st.balloons()
