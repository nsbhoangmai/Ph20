import numpy as np


def spring_exp(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment
    
    Compute x(t) and v(t) of a simple harmonic oscillator with initial
    conditions specified in the input and k/m = 1 using explicit
    Euler's method.
    '''
    
    T = int(t/h)
    X = np.zeros(T)
    V = np.zeros(T)
    
    X[0] = x0
    V[0] = v0
    for i in range(0, T-1):
        X[i+1] = X[i] + h*V[i]
        V[i+1] = V[i] - h*X[i]
    I = np.arange(0, t, h)
    
    return (I, X, V)