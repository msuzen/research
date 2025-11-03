# Comprehensive Dataset for Anomalous Functional-Diffusion for ergodicity convergence

[![arXiv:1606.08693](https://img.shields.io/badge/arXiv-1606.08693-B31B1B.svg)](https://arxiv.org/abs/1606.08693)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17515178.svg)](https://doi.org/10.5281/zenodo.17515178)

  (c) 2013, 2014, 2015, 2016, 2025  
  Süzen
  GPL v3 

## Summary

We provide entire datasets, plots and table with reporducible notebooks to regenerate them, for the working paper. Extensive automated and visual diagnostics are provided.

Anomalous diffusion in convergence to effective ergodicity
M. Suezen  
[arXiv:1606.08693](https://arxiv.org/abs/1606.08693)

## v2 Notes

This is significantly advanced analysis with two different power-laws, one for distribution of  the Gamma (Rate of effective ergodic convergence modified TM-metric) and time-displacement for the Kappa (Inverse of Gamma). 

* Enhanced fitting diagnostics: Extensive automated and visual plots for each case.
* Clarification of Power-laws.
* Extensive diagnostic plotting of temperature-field ranges.
* KS-statistics comparing Glauber/Metropolis dynamics. 

For its content see the README.md file. 

### Reproducing Trajectories and Diagnostic plots

Datasets that would be generate with notebooks would be around~7GB. In this repository we only retain the analysis output not the trajectories and diagnostic plots.  
Trajectory files are ising1Dmagnetisation.rds,  ising1DrateErgodicity.rds, ising1DrateErgodicityFields.rds. The remaining datasets are powerlaw data frames. 
Individual diagnostic plots are also not placed due to space consideration. plots/powerLawKappa, plots/powerLawKappaFields/ and plots/magnetisation/. 

## Notebooks

R Jupyter noetbooks are provided. Some helper methods are used `src/power_utilities.R`. 

### Core data generations:
`gamma_temperature_generate.ipynb` : Generate TM-metric's Gamma over different sizes and temperature range.
`gamma_field_generate.ipynb`: Generate TM-metric's Gamma over different sizes and field range
`magnetisation_autocorrelation_generate.ipynb`: Generation of average magnetisation autocorrelations data.

### Powerlaws data generation
`magnetisation_autocorrelation_analysis.ipynb`: Magnetisation autocorrelation compute, over temperatures. 
`gamma_powerlaw_generate.ipynb`: Compute power-laws for Gamma (see manuscript), over temperatures. 
`kappa_powerlaw_generate.ipynb`: Compute power-laws for Kappa (see manuscript), over temperatures. 
`gamma_powerlaw_generate_fields.ipynb`: Compute power-laws for Gamma (see manuscript) over different field.

### Plotting and futher analysis

`analysis_finite_size_scaling.ipynb`: Basic finite-size scaling analysis.
`dynamics_stat_test.ipynb`: KS test to see the difference between Glauber-Metropolis dynamics
`gamma_powerlaw_analysis_fields.ipynb`: Gamma powerlaw temperature, analysis.
`diffusion_coeffients_kappa.ipynb`: Kappa, generalized diffusion coefficients.    
`kappa_powerlaw_fields_analysis.ipynb`: Kappa powerlaw over different fields.
`kappa_powerlaw_fields_single_plots.ipynb`: Single cases plots over fields, individual curves.
`kappa_powerlaw_single_plots.ipynb`: Single cases plots over temperatures, individual curves.
`gamma_powerlaw_analysis.ipynb`: Plot view of powerlaws.
`kappa_powerlaws_analysis.ipynb`: Plot view of powerlaws.

## Datasets

We store datasets as R dataset format, `RDS`. All are output of notebooks presented above.

`ising1Dmagnetisation.rds`: Magnetisation autocorrelations over temperature and sizes. A list object.
`ising1DrateErgodicity.rds`: Kappa values over temperature and sizes. A list object.
`ising1DrateErgodicityFields.rds`: Kappa values over fields and sizes. A list object.
`ising1DrateErgodicityPowerlawsDistribution.rds`: Powerlaws of Gamma distributions over temperatures. A list object.
`ising1DrateErgodicityPowerlawsDistributionFields.rds`: Powerlaws of Gamma distributions over fields. A data frame.
`ising1DrateErgodicityPowerlawsTime.rds`: Powerlaws of Kappa vs. time over temperatures.  A data frame.
`ising1DrateErgodicityPowerlawsTimeFields.rds`:  Powerlaws of Kappa vs. time over temperatures. A data frame.

## Plots

Extensive plotting is provided for both presentation and visual debugging. 

`finiteSizeScaling`: Basic finite size scalling. 
`magnetisation`: Magnetisation autocorrelation plots for indivudial cases.
`magnetisationOverTemp`: Magnetisation autocorrelation plots over temperatures.
`powerLawGammaDist`: Distributive power laws for Gamma for individual cases.
`powerLawKappa`: Time power laws for Kappa for indivisual case over temperatures.
`powerLawKappaFields`: Time power laws for Kappa for indivisual case over fields.
`temperaturesPowerlaws`: Time power laws for Kappa over temperatures.
`fieldsPowerlaws`: Time power laws for Kappa over fields.

## Tables
Details of power-law fits and diagnostics.

`kappa_powerlaw_time.latex`: Power laws for kappa over temperatures. 
`kappa_powerlaw_time_fields.latex`: Power laws for kappa over fields. 
`gamma_powerlaw_dist.latex`: Power laws for gamma distribution over temperatures. 
`gamma_powerlaw_dist_fields.latex`:Power laws for gamma distribution over fields. 
`metropolis_glauber_ks_tests.latex`: KS-test for checking Glauber-Metropolis.

## License

This project and all contributions are licensed under :
* All non-code  [![License: CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
* Code under [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

