# Mixed Random Matrix Theory (mixedRMT) : Practice and resources

## Introduction

There are many processes that one can apply Random Matrix Theory (RMT), from quantum statistical mechanics to computer networks to deep learning. Primary shortcoming of the existing RMT ensemble approaches that they fix the size of the matrices sampled. This limit the applicability of RMT in many situations, whereby  primary components are heterogeneous. This lead to need for building mixed matrix ensembles (MMEs). The analysis of such ensembles is called Mixed RMT.

## Formal definition 
Due to [suzen21]:

A random matrix ensemble is defined as a mixed ensemble $\mathscr{M}$ if its $M$ constituent matrices appear in varying orders $s_i$, the $i$-th matrix, $s_{i} \in [2, N]$. Whereby non-mixed ensemble is the conventional matrix ensembles of matrix orders of only $N$.

**The degree of the mixture** expresses the ratio of different matrix orders in $M$ matrices, i.e., $m_{i}$ is the number of matrices of order $s_{i}$. This definition brings a constraint on the mixing distribution, with distribution of $m_{i}$, $\rho^{m}(m_{i};s_{i})$, such that $\sum_{i} m_{i} = M$. 

## Some Application areas

* Deep learning: layers produce different size weight matrices.
* Financial instruments: Components that have different-frequency 
* Computer networks: Heterogeneous  connectivity over different devices. 
* Brain and biological networks: Activity in different sub-regions in the brain or biological networks.

## How to generate mixed ensemble?

This is probably one of the core issue. One approach would be using Binomial distribution at the given level
of degree of mixture [suzen21]. 

## Resources
Currently there are limited works in this direction.

### Articles 

* [suzen21] Empirical deviations of semicircle law in mixed-matrix ensembles 
  [hal-03464130](https://hal.science/hal-03464130/) (2021)


## License

This repository and all contributions are licensed under : 
* All non-code  [![License: CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
* Code under [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

