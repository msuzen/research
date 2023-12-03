"""
# H-theorem do-conjecture 

    M. Suzen 
    (c) 2023
    Licence GPLv3

   Supplement for: https://arxiv.org/abs/2310.01458

## Interventional ensembles on a random walker deterministic diffusion

Setting

* $M$ sites, 1-dimensional representation.
* $N$ occupancy, i.e., mimic a particle.
* $\Omega$ count of $k$ states, of boundaries between two outermost occupied sites. Associated with the entropy and H-function.
* Initial condition, $N$ sites occupy a corner fully.

Dynamic rules 

* Move left or right if neigbouring sites are empty, choose to move if possible.
* Use single-move per time-step.
* If left or right is boundary, don't move.
* In case of intervention, move two sites, applying the same dynamical rules.

"""

import numpy as np
from numpy.random import randint
from numpy.random import choice
from numpy import zeros, where
import matplotlib.pyplot as plt

def initialise(M, N):
    sites = zeros(M, dtype=np.int64)
    sites[0:N] = 1
    return sites

def move_step(sites):
    """ Single site move. """
    choosen_occupancy = choice(where(sites)[0], 1)[0]
    if (choosen_occupancy > 0) and (choosen_occupancy < len(sites)-1):
        move_increment = choice([0,1,-1], 1)[0]
        candidate_site = choosen_occupancy + move_increment
        if sites[candidate_site] == 0: 
            sites[candidate_site] = 1
            sites[choosen_occupancy] = 0
    span_ = where(sites)[0]
    exponent_ = max(span_) - min(span_)
    return sites, exponent_


def move_step_intervention(sites):
    """ Two site move: An intervention. """
    choosen_occupancy_1 = choice(where(sites)[0], 1)[0]
    choosen_occupancy_2 = choice(where(sites)[0], 1)[0]
    if choosen_occupancy_1 != choosen_occupancy_2:
        l_choosen_occupancy_1 = (choosen_occupancy_1 > 0) and (choosen_occupancy_1 < len(sites)-1)
        l_choosen_occupancy_2 = (choosen_occupancy_2 > 0) and (choosen_occupancy_2 < len(sites)-1)
        if l_choosen_occupancy_1 and l_choosen_occupancy_2:
            move_increment_1 = choice([0,1,-1], 1)[0]
            candidate_site_1 = choosen_occupancy_1 + move_increment_1
            move_increment_2 = choice([0,1,-1], 1)[0]
            candidate_site_2 = choosen_occupancy_1 + move_increment_2
            if candidate_site_1 != candidate_site_2:
                if sites[candidate_site_1] == 0: 
                    sites[candidate_site_1] = 1
                    sites[choosen_occupancy_1] = 0
                if sites[candidate_site_2] == 0: 
                    sites[candidate_site_2] = 1
                    sites[choosen_occupancy_2] = 0
    # now move o
    span_ = where(sites)[0]
    exponent_ = max(span_) - min(span_)
    return sites, exponent_


def simulate_single_spin_flip_game(M=10, N=3, seed=42*42, plot_eps=False):
    """ Diffusion demo over space """
    np.random.seed(seed)
    m_sites = initialise(M, N)
    dynamic_evolution = []
    for _ in np.arange(100):
        dynamic_evolution.append(m_sites.copy())
        m_sites, omega_size = move_step(m_sites)
    
    font = {"family": "monospace", "weight": "bold", "size": 24}
    plt.ioff()
    plt.rc("font", **font)
    plt.matshow(np.array(dynamic_evolution).transpose(), cmap=plt.cm.binary)
    plt.xlabel("Time step", **font)
    plt.ylabel("Site Id", **font)
    plt.title("Diffusion over time ")
    if plot_eps:
        plt.savefig("dynamicM10N3.eps", format="eps", dpi=60, bbox_inches="tight")
    plt.savefig("dynamicM10N3.png", format="png", bbox_inches="tight")
    #plt.show()
    plt.close('all')


def simulate_interventional_ensemble_effect(M, N, seed=42, plot_eps=False):
    """ Interventional effect """
    plot_file_name = "omegaM" + str(M) + "N" + str(N)
    m_sites = initialise(M, N)
    omega_t = []
    dynamic_evolution = []
    np.random.seed(seed)
    for _ in np.arange(3e5):
        dynamic_evolution.append(m_sites.copy())
        m_sites, omega_size = move_step(m_sites)
        omega_t.append(omega_size.copy())

    m_sites = initialise(M, N)
    omega_t_interventional = []
    dynamic_evolution_interventional = []
    np.random.seed(seed)
    for _ in np.arange(3e5):
        dynamic_evolution_interventional.append(m_sites.copy())
        m_sites, omega_size = move_step_intervention(m_sites)
        omega_t_interventional.append(omega_size.copy())
    
    omega_t = omega_t[0::200]
    omega_t_interventional = omega_t_interventional[0::200]
    
    font = {"family": "monospace", "weight": "bold", "size": 12}
    plt.ioff()
    plt.rc("font", **font)
    plt.plot(np.abs(np.array(omega_t)-np.array(omega_t_interventional)), label="$\Delta H$-causal effect")
    plt.plot(omega_t, "--", label="$\Omega$")
    plt.plot(omega_t_interventional, "-.", label="$\Omega_{intervention}$")
    plt.xscale("log")
    plt.legend()
    plt.xlabel("Time step", **font)
    plt.ylabel("Ensemble size: $k$, $2^k$", **font)
    plt.title("State-size evolution over time ")
    if plot_eps:
        plt.savefig(plot_file_name + ".eps", format="eps", dpi=60, bbox_inches="tight")
    plt.savefig(plot_file_name + ".png", format="png", bbox_inches="tight")
    #plt.show()
    plt.close('all')
