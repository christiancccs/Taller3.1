import streamlit as st 
import matplotlib.pyplot as plt 
import pandas as pd 
gpa = pd.read_csv('gpa1.csv')
st.title("Análisis de promedio")

tab1, tab2 =st.tabs(['Análisis Univariado', 'Análisis bivariado'])

with tab1: 
    fig, ax =plt.subplots(1,4, figsize=(10, 4))

    #Pormedio academico
    gpa['Prom_académico'].plot(kind='hist', bins=20, title='Prom_académico', ax = ax[0])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    #edad
    gpa['Edad'].plot(kind='hist', bins=20, title='Edad', ax = ax[1])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    #Pomedio alcohol
    gpa['Prom_alcohol_sem'].plot(kind='hist', bins=20, title='Prom_alcohol_sem', ax = ax[2])
    plt.gca().spines[['top', 'right',]].set_visible(False) 
    #Genero
    gpa.groupby('Genero').size().plot(kind='barh', ax = ax[3])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))

    #1
    gpa.plot(kind='scatter', x='Edad', y='Prom_académico', s=32, alpha=.8, ax = ax[0])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    #2
    gpa.plot(kind='scatter', x='Genero', y='Prom_académico', s=32, alpha=.8, ax = ax[1])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    #3
    gpa.plot(kind='scatter', x='Prom_alcohol_sem', y='Prom_académico', s=32, alpha=.8, ax = ax[2])
    plt.gca().spines[['top', 'right',]].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)