## Supplement: Gibbs randomness-compression proposition: An efficient deep learning

[![arXiv:2505.23869](https://img.shields.io/badge/arXiv-2505.23869-B31B1B.svg)](https://arxiv.org/abs/2505.23869)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15751974.svg)](https://doi.org/10.5281/zenodo.15751974)

    M. Süzen   
    (c) 2025

A supplement is provided for the paper   

Gibbs randomness-compression proposition: An efficient deep learning     
doi: [10.48550/arXiv.2505.23869](https://arxiv.org/abs/2505.23869)  

## Zenedo 

Also available on Zenedo [doi](https://doi.org/10.5281/zenodo.15751973)

## Summary discussion

[gibbs_randomness_proposition_notebooklm.mp3](gibbs_randomness_proposition_notebooklm.mp3)  
Thank to Google's NotebookLM.

## Regenerating the data 

The data consist of train-compress cylcle on MNIST dataset, storing
different methods of puring including DTC (Dual Tomographic Compression).  
Notebook is [dtcp_generate_data.ipynb](dtcp_generate_data.ipynb). 
This will generate the data file, dictionary of the dataset `d2c_data.dill`.

Alread generated data is also available, in case only analysis is required
[data/d2c_data.dill](data/d2c_data.dill)

## Analysis and plots 

The notebook [dtcp_analysis.ipynb](dtcp_analysis.ipynb) can be used to 
generate the plots. Generated plots can be found under [plots](plots) as 
eps format. 

## License

This project and all contributions are licensed under :
* All non-code  [![License: CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
* Code under [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
~                                                                                                                                  
