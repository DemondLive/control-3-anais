import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame de la base de datos Marvel Movies
df = pd.read_csv('Marvel Movies.csv')

# Título y descripción
st.write("""
# Top Marvel Movies
## Gráficos usando la base de datos de Marvel Movies
""")
st.sidebar.image("Marvel-en-2019-destacada.jpg")

# Opciones de colores
color_options = {
    'Rojo': 'red',
    'Azul': 'blue',
    'Dorado': 'gold',
    'Rosado': 'pink'
}

# Crear el menú en la barra lateral para cambiar el color y los bins
with st.sidebar:
    st.write("# Cambiar cantidad de Bins")
    div = st.slider('Número de bins:', 1, 100, 10)  # Rango de 1 a 100 con valor por defecto 10
    st.write("Bins =", div)
    
    # Selección del color en la barra lateral
    color_choice = st.selectbox('Cambia el color del gráfico', list(color_options.keys()))

# Función para mostrar los gráficos con el color seleccionado y número de bins
def plot_histograms(color, div):
    # Histograma 1: worldwide gross
    plt.figure(figsize=(12, 6))
    plt.hist(df['worldwide gross ($m)'], bins=div, color=color)
    plt.xlabel('worldwide gross ($m)')
    plt.ylabel('% budget recovered')
    plt.title('Histogram of worldwide gross')
    st.pyplot(plt.gcf())
    
    # Histograma 2: audience % score
    plt.figure(figsize=(12, 6))
    plt.hist(df['audience % score'], bins=div, color=color)
    plt.xlabel('audience % score')
    plt.ylabel('% budget recovered')
    plt.title('Histogram of Audience Score')
    st.pyplot(plt.gcf())

    # Histograma 3: year
    plt.figure(figsize=(12, 6))
    plt.hist(df['year'], bins=div, color=color)
    plt.xlabel('year')
    plt.ylabel('% budget recovered')
    plt.title('Histogram of Year')
    st.pyplot(plt.gcf())

# Llamar a la función para dibujar los histogramas con el color y número de bins seleccionados
plot_histograms(color_options[color_choice], div)
