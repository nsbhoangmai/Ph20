import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.integrate as sci
import matplotlib.axes as axe

from spr_exp import *
from spr_imp import *
from spr_sym import*
from load import *

def spring_comp(input_file, output_file):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    h: time increment 
    
    Plot phase space geometry of the trajectories produced by
    different methods
    '''
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    [x0, v0, t, h] = load_num(input_file)
    (Ie, Xe, Ve) = spring_exp(x0, v0, t, h)
    (Ii, Xi, Vi) = spring_imp(x0, v0, t, h)
    (Is, Xs, Vs) = spring_sym(x0, v0, t, h)
    Xa = v0 * np.sin(Ie) + x0 * np.cos(Ie)
    Va = v0 * np.cos(Ie) - x0 * np.sin(Ie)    
    
    plt.plot(Xe, Ve, label='Explicit', color=plt.cm.hot(0.25))
    plt.plot(Xi, Vi, label='Implicit', color=plt.cm.hot(0.7))    
    plt.plot(Xs, Vs, label='Symplectic', color=plt.cm.hot(0.6),\
             ls=':')
    plt.plot(Xa, Va, label='Analytic', color=plt.cm.hot(0.5), lw=2.0)    
    
    
    plt.xlabel('$x(t)$', fontsize=14)
    plt.ylabel('$v(t)$', fontsize=14)
    
    plt.legend(bbox_to_anchor=(1.4,0.5),loc='center right', fontsize=16)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Behavior of spring-mass system in phase space', fontsize=18)
    plt.savefig(output_file, bbox_inches='tight')

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    spring_comp(input_file, output_file)