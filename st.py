# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 00:43:28 2021

@author: matthew.ofomi
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

#latest_iteration = st.empty()
'''
# Hacker statistics

'''
np.random.seed(123)
dice = np.random.randint(1,7)
step = 50


if dice <=2:
    step = step - 1
elif dice >=2:
    step = step +1
else:
    step = step + np.random.randint(1,7)

st.write(dice)
st.write(step)


  

































