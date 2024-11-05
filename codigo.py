import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Marvel Movies.csv')

st.write("""
# Top Marvel Movies
## Gráficos usando la base de datos de Marvel Movies
""")

with st.sidebar:
    st.write("# Opciones")
    div = st.slider('Número de bins:', 0, 10, 2)
    st.write("Bins =", div)


fig, ax = plt.subplots()
ax.hist(df['Box Office'], bins=div)  
ax.set_xlabel('Box Office')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Marvel Movies Box Office')
st.pyplot(fig)
