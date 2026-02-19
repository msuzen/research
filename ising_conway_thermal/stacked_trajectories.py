
#
#
# Visualize Glauber/Metropolis Dynamics Evolution Stacked view
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


 


 

#
#
# Visualize Metropolis Dynamics Evolution 
#
#
seed = 424242
nstep = 4000
dynamic_evolution, _ = ising_conway.play(50, 10, nstep=nstep, beta=1.0, dynamic_type="metropolis", seed=seed)
de = np.array(dynamic_evolution)
i_i = 0
i_f = 500
delta = 500
vs = []
for _ in range(7):
    vs.append(de[i_i:i_f])
    i_i = i_i + delta
    i_f = i_f + delta
de2 = np.hstack(vs)


font = {"family": "monospace", "weight": "bold", "size": 16}
plt.ioff()
plt.rc("font", **font)
plt.matshow(np.array(de2).transpose(),cmap=plt.cm.Blues)
plt.xticks([])
plt.yticks([])
plt.ylabel("Lattice sites of the game over time \n Next row is a continuation of the game.")
plt.xlabel("Time evolution (Monte Carlo steps) \n Each row is a time window")
plt.title(r"Metropolis 50/10 $\beta=1.0$")
plt.savefig("ising_conway_metropolis_evolution_50_10_beta_1.png", format="png" , bbox_inches="tight")
plt.show()

#
#
# Visualize Glauber Dynamics Evolution 
#
#
seed = 424242
nstep = 4000
dynamic_evolution, _ = ising_conway.play(50, 10, nstep=nstep, beta=1.0, dynamic_type="glauber", seed=seed)
de = np.array(dynamic_evolution)
i_i = 0
i_f = 500
delta = 500
vs = []
for _ in range(7):
    vs.append(de[i_i:i_f])
    i_i = i_i + delta
    i_f = i_f + delta
de2 = np.hstack(vs)


font = {"family": "monospace", "weight": "bold", "size": 16}
plt.ioff()
plt.rc("font", **font)
plt.matshow(np.array(de2).transpose(),cmap=plt.cm.Blues)
plt.xticks([])
plt.yticks([])
plt.ylabel("Lattice sites of the game over time \n Next row is a continuation of the game.")
plt.xlabel("Time evolution (Monte Carlo steps) \n Each row is a time window")
plt.title(r"Glauber 50/10 $\beta=1.0$")
plt.savefig("ising_conway_glauber_evolution_50_10_beta_1.png", format="png" , bbox_inches="tight")
plt.show()
