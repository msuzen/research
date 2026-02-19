# Introduction
[![arXiv:2505.23869](https://img.shields.io/badge/arXiv-2503.03769-B31B1B.svg)](https://arxiv.org/abs/2503.03769) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17158156.svg)](https://doi.org/10.5281/zenodo.17158156)

    M. Süzen   
    (c) 2025, 2026

Simulation code and reproducible research for the paper: 

Understanding entropy production with a thermal zero-player game.   
<a href="https://arxiv.org/abs/2503.03769">arXiv preprint arXiv:2503.03769</a> (2025)     

## Software Requirements 

The model `ising_conway.py` provides tools to playing Ising-Conway game with temperature. 
See `requirements.txt`.  

`Python` version 3.10.13 is used and dependencies are minimal. `NumPy` 
for core simulation code, `matplotlib` for visualisationas and `dill`
for data storage.

```python 
numpy==1.24.2
matplotlib==3.8.0
dill==0.3.9
pandas==2.3.3
scipy==1.14.0
```

## `ising_conway` methods

Main game functions and utilities:

`initialise` : Creates the game, N by M, M 1s at the corner of 1D N lattice.    
`get_total_energy`: Sum of average of neighbours with 1s.    
`metropolis_accept`: Acceptance of a move via Metropolis dynamics.   
`glauber_accept`: Acceptance of a move via Glauber dynamics.    
`move_step`: Move one step.   
`play`: Play the entire game given M, N, temperature, steps, seed.    
`generate_entropy_production`: Measure entropy over repeated plays, alignment & averaged.   
`generate_data_set`: Generate dataset given N,M and temperatures.   
`plot_entropy_from_sim_results_betas`: Using result from data generation to plot entropy evolution with temperatures.   
`get_entropy_production_from_sim_results`: Using result from data generation to plot entropy production over temperature.   

## Generate data & plots

Following scripts generate the data and plots. 
   
`entropy_generate_dataset.py`: Generates dataset `data_entropy_production.dill`.       
`stacked_trajectories.py`: Full evolution of games, as an example.      
`plot_entropy_evolution.py`: Entropy evolution of all settings from generated dataset.      
`plot_entropy_production.py`: Entropy production of all settings from production.      
`dynamic_difference_finete_size.ipynb`: KS-test and Finite-size plots.

## Outputs

Data files due to dataset generation, `data_entropy_production.dill`.     
   
Images due to plot scripts, with uncertainties.
    
```bash
entropy_N30M10dynamicsglauber.png
entropy_N30M10dynamicsmetropolis.png
entropy_N40M10dynamicsglauber.png
entropy_N40M10dynamicsmetropolis.png
entropy_N50M10dynamicsglauber.png
entropy_N50M10dynamicsmetropolis.png
entropy_production_cdf.png
entropy_production_finite_size_glauber.png
entropy_production_finite_size_metropolis.png
entropy_production_glauber.png
entropy_production_metropolis.png
ising_conway_glauber_evolution_50_10_beta_1.png
ising_conway_metropolis_evolution_50_10_beta_1.png
```

## License

This project and all contributions are licensed under :
* All non-code  [![License: CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
* Code under [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


