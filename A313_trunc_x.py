import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from A31_spr_exp import *

def trunc_exp(x0, v0, t, h):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    
    Plot truncation error against h (t_i = t_0 + ih) in computing 
    x(t) of a simple harmonic oscillator with initial conditions 
    specified in the input and k/m = 1.
    '''
    
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    H = np.geomspace(h, h/1024, num=11)
    D1 = []
    D2 = []
    for k in H:
        T = int(t/k)
        
        diff1 = 0
        diff2 = 0
        
        (I, X, V) = spring_exp(x0, v0, t, k)
        X1 = v0 * np.sin(I) + x0 * np.cos(I)
        V1 = v0 * np.cos(I) - x0 * np.sin(I)
        for j in range(0, T-1):
            d1 = abs(X1[j]-X[j])
            d2 = abs(V1[j] - V[j])
            if d1 > diff1:
                diff1 = d1
            if d2 > diff2:
                diff2 = d2
        D1.append(diff1)
        D2.append(diff2)
       
    plt.loglog(H, D1, label='$max(x_a - x_i)$',marker='*',\
               color=plt.cm.hot(0.2))
    plt.loglog(H, D2, label='$max(v_a - v_i)$',marker='o',\
               color=plt.cm.hot(0.4))    
    
    plt.ylabel('Truncation error', fontsize=14)
    plt.xlabel('$h$', fontsize=14)
    
    plt.legend(bbox_to_anchor=(1.3,0.5),loc='center right', fontsize=16)
    plt.title('Relation between truncation error and $h$',\
              fontsize=18)
    plt.savefig("Trunc.png", bbox_inches='tight')