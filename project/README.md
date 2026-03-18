# Project description

**Background**

The raw data for this project consists of phase-contrast images acquired through time-lapse microscopy using an inverted microscope. 
Cells are grown in a microfluidic chip containing narrow growth channels, which enables tracking of individual cells and 
their lineages over time.

The cells are exposed to the antibiotic amikacin (8 ug/mL), which corresponds to the EUCAST clinical breakpoint for both E. coli 
and P. aeruginosa. The goal is to characterize the phenotypic response of individual cells to antibiotic treatment at single-cell 
resolution.

An existing MATLAB-based image analysis pipeline has already been used to segment cells, track lineages and estimate growth rates. Growth rates were calculated by fitting an exponential model over sliding windows of 10 minutes. Additionally, preliminary 
Python scripts are available for computing relative growth rates and visualizing individual experiments.

**Project goals**

The main objective of this project is to build upon and improve existing Python code for analyzing single-cell growth data and to apply it to a small set of datasets across species and resistance phenotypes. Specifically:

- Organize existing Python scripts into a more structured and reusable analysis workflow
- Combine datasets from E. coli and P. aeruginosa, including both resistant and susceptible isolates
- Implement functions for visualizing single-cell growth rate trajectories over time
- Apply PCA to identify dominant patterns in the growth dynamics
- Explore whether these patterns can distinguish resistant and susceptible cells, and investigate how early in the time series such separation becomes possible, using a simple classifier as a proof-of-concept

