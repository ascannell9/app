import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.header('All confirmed Exoplanet discoveries')
st.write('Here you can see the data from every discovered exoplanet')
st.write('Do you want to see this data?')
if st.checkbox('Yes'):
    exo = pd.read_csv('PS_2024.03.11_08.53.21.csv',skiprows=96)
    exo.drop_duplicates(subset='pl_name', keep='last', inplace=True)
    exo.reset_index(drop=True, inplace=True)
    exo
    st.write('You can assign yourself a new planet to move to with this random number generator')
    st.button('Random number generator')
    x = np.random.randint(5594)
    st.write(f"you have been given planet {exo.loc[x]['pl_name']}")

if st.checkbox('No'):    
    st.write('Then why are you using this app?????')
    





