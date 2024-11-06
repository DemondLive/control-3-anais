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

# Selección del color en el menú lateral
color_choice = st.sidebar.selectbox('Cambia el color del gráfico', list(color_options.keys()))

# Definir divisiones para los histogramas
div = 10

# Función para mostrar los gráficos con el color seleccionado
def plot_histograms(color):
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

# Llamar a la función para dibujar los histogramas con el color seleccionado
plot_histograms(color_options[color_choice])
