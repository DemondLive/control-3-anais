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

plt.figure(figsize=(12, 6))
    plt.hist(df['worldwide gross ($m)'], bins=10) # Using a default of 10 bins
    plt.xlabel('worldwide gross ($m)')
    plt.ylabel('% budget recovered')
    plt.title('Histogram of worldwide gross')
    plt.show()
    
    plt.figure(figsize=(12, 6))
    plt.hist(df['audience % score'], bins=10)
    plt.xlabel('audience % score')
    plt.ylabel('% budget recovered')
    plt.title('Histogram of Audience Score')
    plt.show()

    plt.figure(figsize=(12,6))
    plt.hist(df['year'], bins = 10)
    plt.xlabel('year')
    plt.ylabel('')
    plt.title('Histogram of Year')
    plt.show()
