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
     "dynamics": ["glauber", "metropolis"],
     "betas": [0.01, 0.5, 0.9, 1.0, 1.5, 2.0, 5.0, 10.0],
     "N_M": [[30, 10], [40, 10], [50, 10]],
     "nrepeat": 100,
     "nstep": 8000,
}

data_set = ising_conway.generate_data_set(sim_params)
dill.dump(data_set, open("data_entropy_production.dill", "wb"))
