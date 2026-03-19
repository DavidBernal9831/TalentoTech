import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   

st.set_page_config(layout='centered',
                   page_title='Talento_Tech',
                   page_icon=":bar_chart:")



t1,t2 = st.columns([0.3,0.7])

t1.image(r'talentotech.jpg',width=200)

t2.title("Análisis de datos con python")
t2.markdown('**tel:** 3167465079 | **email:** **david.bernal9831@gmail.com**')

steps = st.tabs(['pestaña_1','pestaña_2','pestaña_$\sqrt{9}$'])

with steps[0]:
    st.write('contenido pestaña 1')

with steps[1]:
    st.title('pestaña 2')

with steps[2]:
    df = pd.DataFrame({
        'A': [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]
    })
    st.dataframe(df)
    fig, axs = plt.subplots(1, 3)
    sns.barplot(x=['A','B'], y=[1,2], ax=axs[0])
    sns.barplot(x=['C','D'], y=[3,4], ax=axs[1])
    sns.barplot(x=['E','I'], y=[5,1], ax=axs[2])
    st.pyplot(fig)

with steps[1]:
    df = pd.DataFrame({
        'A': [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]
    })
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax = sns.barplot(x=['A','B','C'], y= [1,2,3])
    st.pyplot(fig)



