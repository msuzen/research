#
# Generate dataset
# Entropy production
#
#
# Entropy over time/data gen: Metropolis, Glauber
#

import ising_conway
import numpy as np
import dill

sim_params = {
    "dynamics": ["metropolis", "glauber"],
    "betas": [0.001, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9],
    "N_M": [[100,20], [150, 45]],
    "nrepeat": 100,
    "nstep": 80000,
}
data_set = ising_conway.generate_data_set(sim_params)
dill.dump(data_set, open("data_entropy_production.dill", "wb"))
