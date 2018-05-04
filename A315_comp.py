import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.integrate as sci
import matplotlib.axes as axe

from ene_exp import *
from ene_imp import *
from load import *

def energy_comp(input_file, output_file):
    '''
    Input: 
    x0, v0: Initial values of x and v.
    t: total time taken
    
    Plot energy against time of a simple harmonic oscillator with
    initial conditions specified in the input and k/m = 1 computed
    with different methods.
    '''
    sns.set_style('whitegrid')
        
    plt.rc('figure',figsize=[9.45, 6.53]) 
    plt.rc('font',size=12)
    plt.rc('text', usetex=True)    
    
    [x0, v0, t, h] = load_num(input_file)	
    (I_e, E_e, E_ea) = energy_exp(x0, v0, t, h)
    (I_i, E_i, E_ia) = energy_imp(x0, v0, t, h)
    
    plt.plot(I_e, E_e, label='$E_{exp}$', color=plt.cm.hot(0.2))
    plt.plot(I_i, E_i, label='$E_{imp}$', color=plt.cm.hot(0.6))    
    plt.plot(I_e, E_ea, label='$E_a$', color=plt.cm.hot(0.4))
    
    plt.xlabel('$t(s)$', fontsize=14)
    
    plt.legend(bbox_to_anchor=(1.2,0.5),loc='center right', fontsize=16)
    plt.title('Energy of a mass on a spring', fontsize=18)
    plt.savefig(output_file, bbox_inches='tight')
	
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    energy_comp(input_file, output_file)