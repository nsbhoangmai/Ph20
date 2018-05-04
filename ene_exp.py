import numpy as np

from spr_exp import*

def energy_exp(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment
    
    Compute total mechanical energy of the simple harmonic oscillator
    against time with initial conditions specified in the input and 
    k/m = 1 using the explicit Euler method.
    '''
    T = int(t/h)
    E = np.zeros(T)
    E1 = np.zeros(T)
        
    (I, X, V) = spring_exp(x0, v0, t, h)
    X1 = v0 * np.sin(I) + x0 * np.cos(I)
    V1 = v0 * np.cos(I) - x0 * np.sin(I)
        
    for j in range(0, T-1):
        E[j] = X[j] ** 2 + V[j] ** 2
        E1[j] = X1[j] ** 2 + V1[j] ** 2
    I = I[:-1]
    E = E[:-1]
    E1 = E1[:-1]
    
    return (I, E, E1)