# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:26:30 2021

@author: Lenovo
"""

import numpy as np
from scipy.linalg import solve
A = np.array([[0.5,0.2],[1.,1.]])
B = np.array([10.,30.])
x = solve(A,B)
print(x)

