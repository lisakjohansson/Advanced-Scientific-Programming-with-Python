# Project description

**Background**

The raw data for this project consists of phase-contrast images acquired through time-lapse microscopy using an inverted microscope. 
Cells are grown in a microfluidic chip containing narrow growth channels, which enables continuous tracking of individual cells and 
their lineages over time.

The cells are exposed to the antibiotic amikacin (8 ug/mL), which corresponds to the EUCAST clinical breakpoint for both E. coli 
and P. aeruginosa. The goal is to characterize the phenotypic response of individual cells to antibiotic treatment at single-cell 
resolution.

An existing MATLAB-based image analysis pipeline has already been used to segment cells, track lineages and estimate single-cell 
growth rates. Growth rates were calculated by fitting an exponential model over sliding windows of 10 minutes. Additionally, preliminary 
Python scripts are available for computing relative growth rates and visualizing individual experiments.

**Project goals**

The main objective of this project is to analyze a few datasets across species and resistance phenotypes. Specifically:

- Combine datasets from E. coli and P. aeruginosa, including both resistant and susceptible isolates
- Plot single-cell growth rate trajectories over time in a time-evolution plot
- Apply PCA to the combined dataset to identify dominant patterns in the growth dynamics
- Investigate whether PCA (or some other method) can help define a threshold that separates resistant and susceptible
  phenotypes based on their growth behavior under antibiotic exposure

