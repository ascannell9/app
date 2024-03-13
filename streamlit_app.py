import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.header('All confirmed Exoplanet discoveries')
st.write('Here you can see the data from every discovered exoplanet')
st.write('Do you want to see this data?')

select = st.selectbox('Answer', ['Yes','No'])
    
if select=='Yes':
    exo = pd.read_csv('PS_2024.03.11_08.53.21.csv',skiprows=96)
    exo.drop_duplicates(subset='pl_name', keep='last', inplace=True)
    exo.reset_index(drop=True, inplace=True)
    st.dataframe(exo)
    st.write('You can assign yourself a new planet to move to by clicking the button below')
    st.button('Random planet generator')
    x = np.random.randint(5594)
    st.write(f"You have been selected to go to planet {exo.loc[x]['pl_name']}")
    st.write(f"Here are some details about {exo.loc[x]['pl_name']:}")
    st.write(f"{exo.loc[x]}")
else:   
    st.write('Then why are you using this app?????')
    





