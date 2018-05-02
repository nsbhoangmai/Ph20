import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from A31_spr_exp import *
from A31_spr_imp import *

def spring(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment
    
    Plot x(t) and v(t) of a simple harmonic oscillator with initial
    conditions specified in the input and k/m = 1.
    '''
    
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    
    (Ie, Xe, Ve) = spring_exp(x0, v0, t, h)
    (Ii, Xi, Vi) = spring_imp(x0, v0, t, h)
    Xa = v0 * np.sin(Ie) + x0 * np.cos(Ie)
    Va = v0 * np.cos(Ie) - x0 * np.sin(Ie)
    
    plt.plot(Ie, Xe, label='$x_{exp}$', color=plt.cm.hot(0.2))
    plt.plot(Ii, Xi, label='$x_{imp}$', color=plt.cm.hot(0.6))
    plt.plot(Ie, Xa, label='$x_a$', color=plt.cm.hot(0.4))
    
    plt.plot(Ie, Ve, label='$v_{exp}$', color=plt.cm.cool(0.2), ls='--')
    plt.plot(Ii, Vi, label='$v_{imp}$', color=plt.cm.cool(0.6), ls='--')    
    plt.plot(Ie, Va, label='$v_a$', color=plt.cm.cool(0.4), ls='--')
    
    plt.xlabel('$t(s)$', fontsize=14)
    plt.legend(bbox_to_anchor=(1.2,0.5),loc='center right', fontsize=16)
    plt.title('Motion of a mass on a spring', fontsize=18)
    plt.savefig("Spring.png", bbox_inches='tight')