#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:54:04 2019

@author: Gustavo
"""

import sympy  as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
init_printing(pretty_print=True)


x,y,z = sp.symbols('x,y,z')

sp.diff(3*x**2 +1,x)

x=np.linspace(-3,3)
plt.plot(x,f(x))


def f(x):
    return 3*x**2 +1

def g(x):
    return derivative(f,x)
    
x=np.linspace(-3,3)
plt.plot(x,g(x))














