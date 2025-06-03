## Supplement: Gibbs randomness-compression proposition: An efficient deep learning

A supplement is provided for the paper   

Gibbs randomness-compression proposition: An efficient deep learning     
doi: [10.48550/arXiv.2505.23869](https://arxiv.org/abs/2505.23869)  

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
