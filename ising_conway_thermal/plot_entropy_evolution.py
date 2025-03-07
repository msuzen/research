
#
#
# Visualize Glauber/Metropolis Entropy evolution different temperatures
#
#
import ising_conway

import numpy as np
from numpy.random import randint
from numpy.random import choice
from numpy import zeros, where
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})
plt.rcParams["figure.autolayout"] = True
plt.rcParams['figure.constrained_layout.use'] = True
matplotlib.use('agg')
import dill

data = dill.load(open("data_entropy_production.dill", "rb"))
params = data['sim_params']
sim_results = data['sim_results']

N=100 
M=20
dynamics='metropolis'    
ising_conway.plot_entropy_from_sim_results_betas(sim_results, N, M, dynamics)

N=100 
M=20
dynamics='glauber'    
ising_conway.plot_entropy_from_sim_results_betas(sim_results, N, M, dynamics)


N=150 
M=45
dynamics='metropolis'    
ising_conway.plot_entropy_from_sim_results_betas(sim_results, N, M, dynamics)

N=150 
M=45
dynamics='glauber'    
ising_conway.plot_entropy_from_sim_results_betas(sim_results, N, M, dynamics)