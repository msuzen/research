""" 

Run Simulations: Generate plots

"""
from do_ensemble import simulate_single_spin_flip_game
from do_ensemble import simulate_interventional_ensemble_effect
print("Spin Flip : Demo")
simulate_single_spin_flip_game()
print("Interventional Effect M=800 N=500")
simulate_interventional_ensemble_effect(800, 500, seed=4242, plot_eps=True)
