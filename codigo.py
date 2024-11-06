import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('Marvel Movies.csv')

st.write("""
# Top Marvel Movies
## Gráficos usando la base de datos de Marvel Movies
""")
st.sidebar.image("Marvel-en-2019-destacada.jpg")

# Función para dibujar el gráfico
def plot_chart(color):
    x = np.arange(10)
    y = np.random.randint(1, 10, size=10)
    plt.bar(x, y, color=color)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    st.pyplot(plt.gcf())

# Opciones de colores
color_options = {
    'Rojo': 'red',
    'Azul': 'blue',
    'Dorado': 'gold',
    'Rosado': 'pink'
}

# Crear un selectbox para elegir el color
color_choice = st.selectbox('Cambia el color del gráfico', list(color_options.keys()))

# Dibujar el gráfico con el color seleccionado
plot_chart(color_options[color_choice])



with st.sidebar:
    st.write("# Opciones")
    div = st.slider('Número de bins:', 0, 100, 1)
    st.write("Bins =", div)

plt.figure(figsize=(12, 6))
plt.hist(df['worldwide gross ($m)'], bins=div) # Using a default of 10 bins
plt.xlabel('worldwide gross ($m)')
plt.ylabel('% budget recovered')
plt.title('Histogram of worldwide gross')
st.pyplot()
    
plt.figure(figsize=(12, 6))
plt.hist(df['audience % score'], bins=div)
plt.xlabel('audience % score')
plt.ylabel('% budget recovered')
plt.title('Histogram of Audience Score')
st.pyplot()

plt.figure(figsize=(12,6))
plt.hist(df['year'], bins = div)
plt.xlabel('year')
plt.ylabel('% budget recovered')
plt.title('Histogram of Year')
st.pyplot()
