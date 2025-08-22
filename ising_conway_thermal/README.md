# Introduction

Simulation code and reproducible research for the paper: 

Understanding entropy production with a thermal zero-player game<br>
<a href="https://arxiv.org/abs/2503.03769">arXiv preprint arXiv:2503.03769</a> (2025)  <br> <br>

The model `ising_conway.py` provides tools to playing Ising-Conway game with temperature. 
See `requirements.txt`.  

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

## Outputs

Data files due to dataset generation, `data_entropy_production.dill`.     
   
Images due to plot scripts.    
    
```bash
entropy_N100M20dynamicsglauber.png
entropy_N100M20dynamicsmetropolis.png
entropy_N150M45dynamicsglauber.png
entropy_N150M45dynamicsmetropolis.png
entropy_production.png
ising_conway_glauber_evolution_150_45_beta_0.9.png
ising_conway_metropolis_evolution_150_45_beta_0.9.png
```

## License

This repository and all contributions are licensed under :
* All non-code  [![License: CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
* Code under [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


