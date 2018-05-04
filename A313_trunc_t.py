import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from spr_exp import *
from spr_imp import *
from load import *

def trunc_t(input_file, output_file):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment
    
    Plot truncation error against t in computing x(t) of a simple
    harmonic oscillator with initial conditions specified in the input
    and k/m = 1 using different methods.
    '''
    
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    [x0, v0, t, h] = load_num(input_file)
    t0 = np.geomspace(t, t*512, num=10)
    D1 = []
    D2 = []
    for k in t0:
        T = int(k/h)
        
        diff1 = 0
        diff2 = 0
        
        (Ie, Xe, Ve) = spring_exp(x0, v0, k, h)
        (Ii, Xi, Vi) = spring_imp(x0, v0, k, h)
        X1 = v0 * np.sin(Ie) + x0 * np.cos(Ie)
        for j in range(0, T-1):
            d1 = abs(X1[j]-Xe[j])
            d2 = abs(X1[j]-Xi[j])
            if d1 > diff1:
                diff1 = d1
            if d2 > diff2:
                diff2 = d2
                
        D1.append(diff1)
        D2.append(diff2)
                
    plt.loglog(t0, D1, label='Explicit', marker='*', color=plt.cm.hot(0.2))
    plt.loglog(t0, D2, label='Implicit', marker='o', color=plt.cm.hot(0.6))
    
    plt.ylabel('$max(x_a - x_i)$', fontsize=14)
    plt.xlabel('$t$', fontsize=14)
    plt.title('Relation between truncation error and $t$',\
              fontsize=18)
    plt.legend(bbox_to_anchor=(1.25,0.5),loc='center right', fontsize=16)
    
    plt.savefig(output_file, bbox_inches='tight')

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    trunc_t(input_file, output_file)