
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


styles = iter(['-', '--', '-.', ':', '.', '>', '<', '*', 'x', '!', 'o'])
font = {"family": "monospace", "weight": "bold", "size": 14}
plt.rc("font", **font)

N=100 
M=20
dynamics='metropolis'    
betas, entropy_production, entropy_production_se  = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))

N=100 
M=20
dynamics='glauber'    
betas, entropy_production, entropy_production_se = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))
N=150 
M=45
dynamics='metropolis'    
betas, entropy_production, entropy_production_se = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))
N=150 
M=45
dynamics='glauber'    
betas, entropy_production, entropy_production_se = ising_conway.get_entropy_production_from_sim_results(sim_results, N, M, dynamics)
plt.errorbar(x=betas, y=entropy_production,
                        yerr=entropy_production_se,
                        label=f"Game {N}-{M} {dynamics}", fmt=next(styles))

plt.legend()
plt.xlabel(r"Different Temperature $\beta$ ")
plt.ylabel("Entropy Production Due to Thermal Bath")
plt.ylim([0.8, 5.0])
plt.title("Entropy Production \n Different Temperatures ")
plt.savefig("entropy_production.png", format="png", bbox_inches="tight")  
plt.close()