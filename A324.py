import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from A32_spr_sym import *

def lag_sym(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment 
    
    Plot the lag of x(t) and v(t) computed by the symplectic Euler
    method compared to the analytic solutions for large t.
    '''
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    (I, X, V) = spring_sym(x0, v0, t, h)
    Xa = v0 * np.sin(I) + x0 * np.cos(I)
    Va = v0 * np.cos(I) - x0 * np.sin(I)    
    
    cut = int(len(X)*0.99)
    X = X[cut:]
    V = V[cut:]
    I = I[cut:]
    Xa = Xa[cut:]
    Va = Va[cut:]
    
    plt.plot(I, X, label='$x_s$', color=plt.cm.hot(0.2))
    plt.plot(I, Xa, label='$x_a$', color=plt.cm.hot(0.4), ls='--') 
    plt.plot(I, V, label='$v_s$', color=plt.cm.cool(0.2))    
    plt.plot(I, Va, label='$v_a$', color=plt.cm.cool(0.4), ls='--') 
    
    plt.xlabel('$t(s)$', fontsize=14)
    
    plt.legend(bbox_to_anchor=(1.2,0.5),loc='center right', fontsize=16)
    plt.title('Behavior of spring-mass system', fontsize=18)
    plt.savefig("Err_sym.png", bbox_inches='tight')