import streamlit as st
import pandas as pd
import numpy as np


st.header('st.write')
st.write('Hello World!')

exo = pd.read_csv('PS_2024.03.11_08.53.21.csv', skiprows=96)
st.write(exo)
exo.drop_duplicates(subset = 'pl_name', keep ='last', 
                    inplace = True)
exo.reset_index(drop=True, inplace=True)

period = exo.copy()
period_ = period.sort_values('pl_orbper')
bins = [0,1,2,5,10,100,200,365,1000,1e9]
bin_names = ['0-1 days', '1-2 days', '2-5 days',
             '5-10 days', '10-100 days', '100-200 days',
             '200-365 days', '365-1000 days','1000+ days']
try:
    period_['orbital period'] = pd.cut(period_['pl_orbper'],
           bins = bins,
           labels = bin_names, 
           include_lowest = True).astype('category')
except:
    print('cannot do')

#plt.figure(figsize = (15,10))
#sns.countplot(data = period_,
            # x = 'orbital period',
            # palette = 'summer')
#plt.xticks(fontsize = 'small')
#plt.title('Planet Orbital Periods in Earth Days')
#plt.xlabel('Orbital Period')
#plt.ylabel('Number of Planets')
#plt.plot(4,1900, marker='o',color='grey',ms=5,label='Mercury')
#plt.plot(6,250, marker='o',color='y',ms=19, label='Venus')
#plt.plot(6.8,350, marker='o',color='b',ms=20, label='Earth')
#plt.plot(7.2,350, marker='o',color='r',ms=10, label='Mars')
#plt.legend(markerscale=0.65)
#plt.show()

# Mercury = 88 days, Venus = 225 days, Earth = 365 days, Mars = 687 days , Jupiter = 4331 days
st.barchart(period_['orbital period'])


