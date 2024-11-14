# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   -- add your team names here --

Sensitivity analysis of the grass growth model
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mbps.models.grass_sol import Grass

plt.style.use('ggplot')

# TODO: Define the required variables for the grass module

# -- Define the required variables
# Simulation time
tsim = np.linspace(0.0, 365.0, 365) # [d]
dt = 1 # [d]
# Initial conditions
# TODO: Define sensible values for the initial conditions
x0 = {'Ws':1E-4,'Wg':1E-4} # [kgC m-2]
# Model parameter values (as provided by Mohtar et al. 1997 p.1492-1493)
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
'''NOTE: If you have not evaluated and adjusted your own implementation of
the model, adjust to a=55[m2 kgC-1], and alpha=1E-8[kgCO2 J-1]'''

# Disturbances
# PAR [J m-2 d-1], environment temperature [°C], and
# water availability index [-]
t_ini = "20010101"
t_end = "20011231"
data_weather = pd.read_csv(
     'data/practical_data/weather_2001.csv', # .. to move up one directory from current directory
     comment='#', # ignore comment lines
     header=None, # no header in the CSV file
     names=['STN', 'YYYYMMDD', 'TG', 'SQ', 'Q'], # manually specify column names
     usecols=['YYYYMMDD', 'TG', 'SQ', 'Q'], # columns to use
     index_col=0, # column with row names from used columns, 0-indexed
     )
# Retrieve relevant arrays from pandas dataframe
T = data_weather.loc[t_ini:t_end,'TG'].values    # [0.1 °C] Env. temperature
I_gl = data_weather.loc[t_ini:t_end,'Q'].values # [J cm-2 d-1] Global irradiance 
# Aply the necessary conversions of units
T = T*0.1    # [???] to [???] Env. temperature
I0 = I_gl*10000   # [???] to [???] Global irradiance to PAR
# Dictionary of disturbances (2D arrays, with col 1 for time, and col 2 for d)
d = {'T':np.array([tsim, T]).T,
     'I0':np.array([tsim, I0]).T,   
     'WAI':np.array([tsim, np.full((tsim.size,),1.0)]).T
     }
'''NOTE: If you have not evaluated and adjusted your own implementation of
the model, retrieve wethare data for 2017 from the file etmgeg_260.csv'''


# Controlled inputs
u = {'f_Gr':0, 'f_Hr':0}            # [kgDM m-2 d-1]

# Initialize grass module
grass = Grass(tsim, dt, x0, p)

# Normalized sensitivities
ns = grass.ns(x0, p, d=d, u=u, y_keys=('Wg',))

# Calculate mean NS through time
# TODO: use the ns DataFrame to calculate mean NS per parameter
mean_wg_a = ns["Wg"]["a"].mean()
mean_wg_alpha = ns["Wg"]["alpha"].mean()




# -- Plots
# TODO: Make the necessary plots (example provided below)
plt.figure(1)
plt.plot(grass.t, ns['Wg','a','-'], label='a -', linestyle='--')
plt.plot(grass.t, ns['Wg','a','+'], label='a +')
plt.legend()
plt.xlabel(r'$time\ [d]$')
plt.ylabel('normalized sensitivity [-]')
plt.show()