# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:10:49 2022

@author: Maheen
"""

import pickle
import numpy as np


#loading the saved models
loaded_model=pickle.load(open('house_price.sav','rb'))

input_data=(0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)