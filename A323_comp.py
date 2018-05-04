import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ene_sym import *
from load import *

def energy_comp2(input_file, output_file):
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
    (Is, Es, Ea) = energy_sym(x0, v0, t, h)
    
    plt.plot(Is, Es, label='$E_{sym}$', color=plt.cm.hot(0.2))
    plt.plot(Is, Ea, label='$E_{a}$', color=plt.cm.hot(0.4))    
    
    plt.xlabel('$t(s)$', fontsize=14)
    
    plt.legend(bbox_to_anchor=(1.2,0.5),loc='center right', fontsize=16)
    plt.title('Energy of a mass on a spring', fontsize=18)
    plt.savefig(output_file, bbox_inches='tight')

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    energy_comp2(input_file, output_file)