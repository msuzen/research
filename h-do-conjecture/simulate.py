""" 

Run Simulations: Generate plots

"""
from do_ensemble import simulate_single_spin_flip_game
from do_ensemble import simulate_interventional_ensemble_effect
print("Single Spin Flip : Demo")
simulate_single_spin_flip_game()
print("Interventional Effect M=100 N=10")
simulate_interventional_ensemble_effect(100, 10)
print("Interventional Effect M=1000 N=100")
simulate_interventional_ensemble_effect(1000, 100)
