"""
# Ising-Conway Entropy Game with thermal bath and utilities

    M. Suzen
    (c) 2025
    Licence GPLv3

Setting

* $M$ sites, 1-dimensional representation.
* $N$ occupancy, i.e., mimic a particle.
* $\Omega$ count of $k$ states, of boundaries between two outermost occupied sites. Associated with the entropy and H-function.
* Initial condition, $N$ sites occupy a corner fully.

Dynamic rules

* Move left or right if neigbouring sites are empty, choose to move if possible.
* Use single-move per time-step.
* Check move with Metropolis or Glauber with temperature Beta
  # Given Sites & thermal
  Metropolis  min { 1, exp(-Beta H )}
  Glauber min {1, 1/(1+exp(Beta H)) }
  H is total energy, two neighbours 1.0, only one neigbour occupies 0.5, no neigbours 0.0.
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


def get_total_energy(sites):
    total_energy = 0.0
    n = len(sites)
    for i in range(1, n - 1):
        if sites[i] == 1:
            local_energy = (sites[i - 1] + sites[i + 1]) / 2.0
            total_energy += local_energy
    return total_energy


def metropolis_accept(sites, trial_sites, beta=0.1):
    total_energy0 = get_total_energy(sites)
    total_energy1 = get_total_energy(trial_sites)
    delta_energy = total_energy1 - total_energy0
    return np.min([1.0, np.exp(-beta * delta_energy)]) > np.random.random()


def glauber_accept(sites, trial_sites, beta=0.1):
    total_energy0 = get_total_energy(sites)
    total_energy1 = get_total_energy(trial_sites)
    delta_energy = total_energy1 - total_energy0
    return np.min([1.0, 1.0 / (1.0 + np.exp(beta * delta_energy))]) > np.random.random()


def move_step(sites, beta=0.1, dynamics_type="metropolis"):
    """Single site move."""
    trial_sites = sites.copy()
    # Make a move obeying game rules
    choosen_occupancy = choice(where(trial_sites)[0], 1)[0]
    if (choosen_occupancy > 0) and (choosen_occupancy < len(trial_sites) - 1):
        move_increment = choice([0, 1, -1], 1)[0]
        candidate_site = choosen_occupancy + move_increment
        if trial_sites[candidate_site] == 0:
            trial_sites[candidate_site] = 1
            trial_sites[choosen_occupancy] = 0
    if dynamics_type == "metropolis":
        is_accept = metropolis_accept(sites, trial_sites, beta)
    if dynamics_type == "glauber":
        is_accept = glauber_accept(sites, trial_sites, beta)
    if is_accept:
        sites = trial_sites.copy()
    span_ = where(sites)[0]
    exponent_ = max(span_) - min(span_)
    return sites, exponent_


def play(M=10, N=3, nstep=1000, beta=0.1, dynamic_type="glauber", seed=42 * 42):
    """Play the game"""
    np.random.seed(seed)
    m_sites = initialise(M, N)
    dynamic_evolution = []
    omega_t = list()
    for _ in np.arange(nstep):
        dynamic_evolution.append(m_sites.copy())
        m_sites, omega_size = move_step(m_sites, beta=beta, dynamics_type=dynamic_type)
        omega_t.append(omega_size)
    return dynamic_evolution, omega_t


def generate_entropy_production(
    N=100, M=20, nstep=80000, beta=0.01, dynamics="metropolis", nrepeat=30
):
    """Repeated runs with alignment."""
    entropy_product = []
    for _ in range(nrepeat):
        sq1 = np.random.SeedSequence()
        seed = abs(int(sq1.entropy / 2**100))
        _, entropy_ = play(
            N, M, nstep=nstep, beta=beta, dynamic_type=dynamics, seed=seed
        )
        entropy_product.append(entropy_)
    min_length_align = np.min([len(ep) for ep in entropy_product])
    entropy_product_mean = np.array(
        [
            ep[0:min_length_align] for ep in entropy_product
        ]  # these are actually just entropy over moves
    ).mean(axis=0)
    entropy_product_std = np.array(
        [
            ep[0:min_length_align] for ep in entropy_product
        ]  # these are actually just entropy over moves
    ).std(axis=0)
    entropy_product_data = {
        "N": N,
        "M": M,
        "nstep": nstep,
        "beta": beta,
        "dynamics": dynamics,
        "nrepeat": nrepeat,
        "entropy_product_mean": entropy_product_mean,  # these are actually just entropy over moves
        "entropy_product_se": entropy_product_std / np.sqrt(nrepeat),
    }
    return entropy_product_data


def generate_data_set(sim_params):
    """

    Produce data_set

    data_set = { "sim_params":{"dynamics": ["metropollis", "glauber"],
        "betas": [0.001, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9], "N_M", [[100,20], [150, 45]], "nrepeat":30, "nstep":80000},
        "sim_results":[entropy_product_data,entropy_product_data,...]
     }

    """
    data_set = {}
    data_set["sim_params"] = sim_params
    data_set["sim_results"] = []
    for dynamics in sim_params["dynamics"]:
        for beta in sim_params["betas"]:
            for N_M in sim_params["N_M"]:
                print(f"N {N_M[0]} M {N_M[1]} dynamics {dynamics} beta {beta}")
                entropy_product_data = generate_entropy_production(
                    N=N_M[0],
                    M=N_M[1],
                    nstep=sim_params["nstep"],
                    beta=beta,
                    dynamics=dynamics,
                    nrepeat=sim_params["nrepeat"],
                )
                data_set["sim_results"].append(entropy_product_data)
    return data_set


def plot_entropy_from_sim_results_betas(sim_results, N, M, dynamics, spacing=500):
    styles = iter(["-", "--", "-.", ":", ".", ">", "<", "*", "x", "!", "o"])
    for res in sim_results:
        if res["N"] == N and res["M"] == M and res["dynamics"] == dynamics:
            nstep = len(res["entropy_product_mean"])
            x = np.arange(0, nstep)
            plt.errorbar(
                x=x[::spacing],
                y=res["entropy_product_mean"][::spacing],
                yerr=res["entropy_product_se"][::spacing],
                label=f"beta={res['beta']}",
                fmt=next(styles),
            )
    plt.legend(fontsize=11)
    font = {"family": "monospace", "weight": "bold", "size": 16}
    plt.rc("font", **font)
    plt.xlabel(f"Accepted Game Move x{spacing}", fontsize=16)
    plt.ylabel("Entropy", fontsize=16)
    plt.title(
        f"Evolution of Entropy Game \n Different Temperatures N={N} M={M} dynamics {dynamics}", fontsize=16
    )
    plt.savefig(
        f"entropy_N{N}M{M}dynamics{dynamics}.png", format="png", bbox_inches="tight"
    )
    plt.close()


def get_entropy_production_from_sim_results(sim_results, N, M, dynamics):
    """Get entropy production."""
    entropy_beta = []
    entropy_se = []
    for res in sim_results:
        if res["N"] == N and res["M"] == M and res["dynamics"] == dynamics:
            entropy_beta.append((res["beta"], res["entropy_product_mean"]))
            entropy_se.append((res["beta"], res["entropy_product_se"]))
    betas = [beta[0] for beta in entropy_beta]
    align_length = np.min([len(beta[1]) for beta in entropy_beta])
    entropy_curves = [data[1][:align_length] for data in entropy_beta]
    entropy_curves_se = [data[1][:align_length] for data in entropy_se]
    entropy_prod = [np.sum(ec) for ec in entropy_curves]
    entropy_prod_se = [
        np.sum(ec) for ec in entropy_curves_se
    ]  # Here we compute SE area
    return betas, entropy_prod / entropy_prod[0], entropy_prod_se / entropy_prod[0]
