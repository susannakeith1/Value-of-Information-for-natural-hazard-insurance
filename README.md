# Value of Information framework for natural hazard insurance

Value of Information Framework for Natural Hazard Insurance

This repository contains the Python code used to implement the Value of Information (*VoI*) framework for natural hazard insurance presented in Keith et al. (2025). The code includes both continuous and discrete formulations for assessing the value of additional information about earthquake hazard and its implications for insurance decisions.

The repository includes Python scripts containing the calculation functions and Jupyter notebooks demonstrating their application and reproducing the results presented in the paper. The continuous formulation is described in detail below, as it is used to generate Figures 8 and 9.

## Methodology

The *VoI* framework evaluates whether additional information about earthquake hazard can improve insurance decisions and quantifies the resulting value for different stakeholders. The analysis considers uncertainty in the time-averaged shear-wave velocity in the upper 30 m of soil $Vs_{30}$ and its influence on expected losses and insurance premiums.

The calculations involve the following steps:

### 1. Loss assessment:
Expected losses are calculated as a function of $Vs_{30}$, using the relationship between site conditions and earthquake losses.

### 2. Prior decision: 
The optimal insurance decision is identified using the available information about $Vs_{30}$.

### 3. Pre-posterior analysis: 
The expected outcome is evaluated by considering the decisions that could be made following the acquisition of additional information.

### 4. VoI calculation: 
The *VoI* is calculated as the difference between the expected outcome with additional information and the expected outcome under the prior information. The analysis considers the value to both the client and the insurer.

The framework assumes a rational, risk-neutral decision-maker and uses expected outcomes to compare decisions. The *VoI* represents the maximum amount that could be justified for acquiring the additional information under the assumptions of the analysis.


## Repository structure

The repository contains Python scripts and Jupyter notebooks for both the continuous and discrete formulations of the Value of Information (*VoI*) framework. The continuous formulation is described in detail below and is used to generate Figures 8 and 9 in the paper.

```
.
├── Discrete/
│   ├── VoI_Code_Discrete.py
│   └── VoI_Example_Discrete.ipynb
│
├── Continuous/
│   ├── VoI_Code_Continuous.py
│   ├── VoI_Example_Continuous.ipynb
│   ├── VoI_JSON_Example.ipynb
│   ├── vs30_250_evpi_client.json
│   ├── vs30_250_evpi_insurer.json
│   ├── vs30_500_evpi_client.json
│   └── vs30_500_evpi_insurer.json
│
└── README.md
```


**Continuous formulation** 

Implements the continuous formulation of the *VoI* framework, where $Vs_{30}$ is represented as a continuous variable. The notebook demonstrates the calculations and plots the results.

`VoI_Code_Continuous.py`: Contains the functions implementing the continuous VoI formulation.

`VoI_Example_Continuous.ipynb`: Demonstrates the application of the continuous formulation and reproduces the results for varying $\alpha$, as used in Figures 8 and 9 of the paper.

`VoI_JSON_Example.ipynb`: Demonstrates how to load the JSON files containing the client and insurer *VoI* results and reproduce the associated contour plots.

`vs30_250_evpi_client.json` and `vs30_250_evpi_insurer.json`: Store the client and insurer *VoI* results for the $Vs_{30} = 250$m/s case.

`vs30_500_evpi_client.json` and `vs30_500_evpi_insurer.json`: Store the client and insurer *VoI* results for the $Vs_{30} = 500$m/s  case.


**Discrete formulation**

Implements the discrete formulation, where $Vs_{30}$ is represented by a finite set of possible values. The notebook demonstrates the calculations and plots the results.

VoI_Code_Discrete.py: Contains the functions implementing the discrete *VoI* formulation.

VoI_Example_Discrete.ipynb: Demonstrates the application of the discrete formulation and reproduces the results for $\alpha = 2$, as used in Figures 4 and 5 of the paper. The notebook also includes an interactive slider for exploring the effect of varying $\alpha$.





## Running the code

The Python scripts contain the functions used to calculate the *VoI*. The Jupyter notebooks demonstrate their application and reproduce the results.

To reproduce the results, open the relevant notebook and run the cells in order. The notebooks include example plots for the parameter values used in the paper. Interactive widgets can be used in a compatible Jupyter environment, but do not run directly on GitHub.


## Requirements
The code requires Python and the following packages:
```
numpy
scipy
pandas
matplotlib
jupyter
ipywidgets (for interactive plots)
```
## Citation

Keith, S., Tubaldi, E., Gkimprixis, A., Douglas, J. and Pytharouli, S. (2025). *Value of Information framework for natural hazard insurance*. *Reliability Engineering & System Safety*, 267, 111816. https://doi.org/10.1016/j.ress.2025.111816

