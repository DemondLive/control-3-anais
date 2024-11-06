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
    div = st.slider('Número de bins:', 1, 100, 10)  # Mínimo 1, máximo 100, valor por defecto 10
    st.write("Bins =", div)
    
    # Selección del color en la barra lateral
    color_choice = st.selectbox('Cambia el color del gráfico', list(color_options.keys()))

# Función para mostrar los gráficos con el color seleccionado y número de bins
def plot_histograms(color, div):
    # Limpiar figuras
