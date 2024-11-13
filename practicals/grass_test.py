# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   -- Jeroen Cox jeroen.cox@wur.nl --

Evaluation of the grass growth model
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mbps.models.grass import Grass


# -- Define the required variables
# Simulation time
tsim = np.linspace(0.0, 365.0, 365) # [d]
dt = 1 # [d]
# Initial conditions
# TODO: Define sensible values for the initial conditions
x0 = {'Ws':1E-4,'Wg':1E-4} # [kgC m-2]
# Model parameters (as provided by Mohtar et al. 1997 p.1492-1493)
# TODO: Define values for the model parameters
p = {'a':45,          # [m2 kgC-1] structural specific leaf area
     'alpha':2E-8,      # [kgCO2 J-1] leaf photosynthetic efficiency
     'beta':0.025,
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


# Disturbances (assumed constant for this test)
# 2-column arrays: Column 1 for time. Column 2 for the constant value.
# PAR [J m-2 d-1], environment temperature [°C], and
# water availability index [-]
with open('data/practical_data/weather_2001.csv') as f:
     df = pd.read_csv(f, comment='#', header=None, names=['STN', 'YYYYMMDD', 'TG', 'SQ', 'Q'])
     I0 = np.array(df['Q'].values)
     T = np.array(df['TG'].values)


# TODO: Fill in sensible constant values for T and I0.
d = {'I0':np.array([tsim, np.full((tsim.size,), 9E6)]).T,
     'T':np.array([tsim, np.full((tsim.size,), 18)]).T,
     'I0_ref':np.array([tsim, I0]), # [J m-2 d-1]
     'T_ref':np.array([tsim, T]),   # [°C]
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
t_grass = y_grass['t']
WsDM = np.array(y_grass['Ws'])*0.4
WgDM = np.array(y_grass['Wg'])*0.4

# -- Plot
# TODO: Make a plot for WsDM & WgDM vs. t
plt.figure(figsize=(10, 6))
plt.plot(t_grass, WsDM, label='storage (WsDM)')
plt.plot(t_grass, WgDM, label='structure WgDM)')
plt.xlabel('Time [days]')
plt.ylabel('Biomass [kgDM m-2]')
plt.title('Grass Growth Over Time')
plt.legend()
plt.savefig(f"data/practical_data/grass_growth_{datetime.datetime.now()}.png")