#######################################################################
##
## Licencia GPL 3.0
## carlos@cardenas.pe
##
## Gráfica GIF de Contagios y Fallecidos en LA.
##
########################################################################

import matplotlib.patches as mpatches
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.legend import Legend
from datetime import datetime

def buildmebarchart(i=int):
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values)
    q=len(df1[:i].index)
    m=1
    for px in  df1[:i].index:
        if q ==m:
            print (px)
            plt.title(str(px).split(' ')[0]) 	
        m=m+1
    for i in range(0,7):
        p[i].set_color(color[i])

#url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

df = pd.read_csv(url, delimiter=',', header='infer')
df_interest = df.loc[
    df['Country/Region'].isin(['Peru', 'Chile', 'Colombia', 'Mexico','Brazil','Ecuador','Argentina'])
    & df['Province/State'].isna()]
df_interest.rename(
    index=lambda x: df_interest.at[x, 'Country/Region'], inplace=True)
df1 = df_interest.transpose()
df1 = df1.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)

color = ['red', 'green', 'blue', 'orange','pink','cyan','brown']

fig = plt.figure()

plt.xticks(rotation=45, ha="right", rotation_mode="anchor")

plt.subplots_adjust(bottom = 0.2, top = 0.9) 

#plt.ylabel('Nro. de Muertes Covid @unimauro')

plt.ylabel('Nro. de Confirmados»')

plt.xlabel('Fecha ... made @unimauro')

animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)

animator.save('Confirmados20200510.gif', writer='imagemagick', fps=30)

plt.show()
