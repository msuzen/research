
#
#
# Visualize Glauber/Metropolis Entropy evolution different temperatures
#
#
import ising_conway

import numpy as np
import dill

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


data = dill.load(open("data_entropy_production.dill", "rb"))
params = data['sim_params']
sim_results = data['sim_results']


styles = iter(['-', '--', '-.', ':', '.', '>', '<', '*', 'x', '!', 'o'])
font = {"family": "monospace", "weight": "bold", "size": 17}
plt.rc("font", **font)

  
N=30
M=10
dynamics='metropolis'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))

N=40
M=10
dynamics='metropolis'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles)) 

N=50
M=10
dynamics='metropolis'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles)) 
 
 
plt.legend()
font = {"family": "monospace", "weight": "bold", "size": 16}
plt.rc("font", **font)
plt.xlabel(r"Different Temperature $\beta$ ")
plt.ylabel("Entropy Production \n Due to Thermal Bath")
plt.ylim([0.9, 1.3])
plt.title("Entropy Production \n Different Temperatures ")
plt.savefig("entropy_production_metropolis.png", format="png", bbox_inches="tight")  
plt.close()


styles = iter(['-', '--', '-.', ':', '.', '>', '<', '*', 'x', '!', 'o'])

N=30
M=10
dynamics='glauber'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))

N=40
M=10
dynamics='glauber'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles)) 

N=50
M=10
dynamics='glauber'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles)) 
 
 
plt.legend()
font = {"family": "monospace", "weight": "bold", "size": 16}
plt.rc("font", **font)
plt.xlabel(r"Different Temperature $\beta$ ")
plt.ylabel("Entropy Production \n Due to Thermal Bath")
plt.ylim([0.9, 1.3])
plt.title("Entropy Production \n Different Temperatures ")
plt.savefig("entropy_production_glauber.png", format="png", bbox_inches="tight")  
plt.close()
