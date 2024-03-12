import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.header('Let\'s hope this works!')
st.write('After numerous errors lets hope we get none')

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

st.map(map_data)



