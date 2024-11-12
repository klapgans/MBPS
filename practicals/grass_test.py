# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   -- Jeroen Cox jeroen.cox@wur.nl --

Evaluation of the grass growth model
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mbps.models.grass import Grass

# -- Define the required variables
# Simulation time
tsim = np.linspace(0.0, 365.0, 365+1) # [d]
dt = 1 # [d]
# Initial conditions
# TODO: Define sensible values for the initial conditions
x0 = {'Ws':1,'Wg':1} # [kgC m-2]
# Model parameters (as provided by Mohtar et al. 1997 p.1492-1493)
# TODO: Define values for the model parameters
p = {'a':40.0,          # [m2 kgC-1] structural specific leaf area
     'alpha':2E-9,      # [kgCO2 J-1] leaf photosynthetic efficiency
     'beta': 0.05,
     'k':0.5,           # [-] extinction coefficient of canopy
     'm':0.1,           # [-] leaf transmission coefficient
     'M':0.02,          # [d-1] maintenance respiration coefficient
     'mu_m':0.5,        # [d-1] upperbound of Ws compared to Wg
     'P0':0.432,          # [kgCO2 m-2 d-1] max photosynthesis parameter
     'phi':0.9,         # [-] photoshynthetic fraction for growth
     'Tmax':42.0,       # [°C] maximum temperature for growth
     'Tmin':0.0,        # [°C] minimum temperature for growth
     'Topt':20.0,       # [°C] optimum temperature for growth"
     'Y':0.75,           # [-] structure fraction from storage
     'z':1.33            # [-] bell function power
     }
# Parameters adjusted manually to obtain growth
# TODO: If needed, adjust the values for 2 or 3 parameters to obtain growth
# p[???] = ???
# p[???] = ???

# Disturbances (assumed constant for this test)
# 2-column arrays: Column 1 for time. Column 2 for the constant value.
# PAR [J m-2 d-1], environment temperature [°C], and
# water availability index [-]
with open('data/practical_data/weather_2001.csv') as f:
     df = pd.read_csv(f, comment='#', header=None, names=['STN', 'YYYYMMDD', 'TG', 'SQ', 'Q'])
     I0 = np.array(df['Q'].values)
     T = np.array(df['TG'].values)


# TODO: Fill in sensible constant values for T and I0.
d = {'I0_ref':np.array([tsim, np.full((tsim.size,), 8E7)]).T,
     'T_ref':np.array([tsim, np.full((tsim.size,), 20)]).T,
     'WAI':np.array([tsim, np.full((tsim.size,),1.0)]).T
     }

# Controlled inputs
u = {'f_Gr':0, 'f_Hr':0}            # [kgDM m-2 d-1]

# Initialize grass module
grass = Grass(tsim,dt,x0,p)

# Run simulation
tspan = (tsim[0],tsim[-1])
y_grass = grass.run(tspan,d,u)

# Retrieve simulation results
# assuming 0.4 kgC/kgDM (Mohtar et al. 1997, p. 1492)
# TODO: Retrieve the simulation results
t_grass = y_grass['t']
# WsDM = ???
# WgDM = ???

# -- Plot
# TODO: Make a plot for WsDM & WgDM vs. t
plt.figure(1)
# plt.plot(t_grass, WsDM, label='Storage weight')

