# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:04:06 2022

@author: Maheen
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models
house_price_model=pickle.load(open('house_price.sav','rb'))

#Diabetes prediction page

st.title('House Price Prediction using ML')

#getting the input data from user
#columns for input fields

    
col1,col2,col3=st.columns(3)
    
with col1:
    CRIM=st.text_input('Crime Rate')
with col2:
    ZN=st.text_input('Proportion of Residential land')
with col3:
    INDUS=st.text_input('Proportion of non retail business acres')
with col1:
    CHAS=st.text_input('Charles River')
with col2:
    NOX=st.text_input('Nitric oxides concentration')
with col3:
    RM=st.text_input('Avg no. of rooms')
with col1:
    AGE=st.text_input('Age of house')
with col2:
    DIS=st.text_input('Distance to Employment Centres')
with col3:
    RAD=st.text_input('Accessibility to highways')
with col1:
    TAX=st.text_input('Tax-Rate')
with col2:
    PTRATIO=st.text_input('Pupil-Teacher ratio')
with col3:
    B=st.text_input('Proportion of blacks')
with col1:
    LSTAT=st.text_input('Lower stat of population')

#code for prediction
price_prediction=''
    
#creating a button for prediction
if st.button('Predict House Price'):
    price_pred=house_price_model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])    

st.success(price_prediction)   
 
    
    
    
    
    
    
    