# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 06:11:17 2020

@author: sudhe
"""
import pandas as pd
import numpy as np

def correlation(X,Y):
    
    data=pd.DataFrame()
    data['X']=pd.Series(data=X)
    data['Y']=pd.Series(data=Y)
    data['XY']=data['X']*data['Y']
    data['X^2']=np.square(data['X'])
    data['Y^2']=np.square(data['Y'])

    n=len(data)

    r=((n*np.sum(data['XY']))-(np.sum(data['X'])*np.sum(data['Y'])))/np.sqrt((n*np.sum(data['X^2'])-np.sum(data['X'])**2)*(n*np.sum(data['Y^2'])-np.sum(data['Y'])**2))
    
    return r
'''
X=np.array([43,21,25,42,57,59])
Y=np.array([99,65,79,75,87,81])

import plotly.graph_objects as go
from plotly.offline import plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=data['X'], y=data['Y'],mode='markers'))

fig.update_layout()
plot(fig, auto_open=True)
'''