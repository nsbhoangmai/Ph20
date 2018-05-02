import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.integrate as sci
import matplotlib.axes as axe

def spring_sym(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment
    
    Compute x(t) and v(t) of a simple harmonic oscillator with initial
    conditions specified in the input and k/m = 1 using symplectic
    Euler's method.
    '''
    
    T = int(t/h)
    X = np.zeros(T)
    V = np.zeros(T)
        
    X[0] = x0
    V[0] = v0
    for i in range(0, T-1):
        X[i+1] = X[i] + h*V[i]
        V[i+1] = V[i] - h*X[i+1]
    I = np.arange(0, t, h)
    
    return (I, X, V)