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

def covariance(X,Y):
    data=pd.DataFrame()
    data['X']=pd.Series(data=X)
    data['Y']=pd.Series(data=Y)
    data['X-X_bar']=data['X']-np.mean(data['X'])
    data['Y-Y_bar']=data['Y']-np.mean(data['Y'])
    data['X-X_bar*Y-Y_bar']=data['X-X_bar']*data['Y-Y_bar']
    
    return np.sum(data['X-X_bar*Y-Y_bar'])/(len(data)-1)

def standardDeviation(X):
    
    data=pd.DataFrame()
    data['X']=pd.Series(data=X)
    data['X-X_bar_wholesqare']=np.square(data['X']-np.mean(data['X']))
    
    return np.sqrt(np.sum(data['X-X_bar_wholesqare'])/(len(data)-1))

