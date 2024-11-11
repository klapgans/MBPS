# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   -- Fill in your team names --

Tutorial: Grass growth model analysis.
3. Temperature index
"""
# TODO: Import the required packages 
import numpy as np
import matplotlib.pyplot as plt


# TODO: Define the values for the TI parameters
def simple_variables(Tmax, Tmin, Topt, T):
    """
    For simplicity, define the variables for the temperature index.
    Tmax: Maximum temperature [°C]
    Tmin: Minimum temperature [°C]
    Topt: Optimum temperature [°C]
    T: Temperature [°C]
    """
    DTmax = Tmax - T
    DTmin = T - Tmin
    DTa = Tmax - Topt
    DTb = Topt - Tmin
    return DTmax, DTmin, DTa, DTb

def fcn_Ti_simplified(DTmax, DTmin, DTa, DTb, z) -> np.ndarray:
    return ( (DTmax/DTa) * ((DTmin/DTb)**(DTb/DTa)) )**z


# TODO: Define a sensible array for values of T
T = np.linspace(0, 42, 100)

DTMax, DTmin, DTa, DTb = simple_variables(np.max(T), np.min(T), 20, T)
Ti = fcn_Ti_simplified(DTMax, DTmin, DTa, DTb, 1.33)

# TODO: (Optional) Define support variables DTmin, DTmax, DTa, DTb
# Temperature index: TI = ( (DTmax/DTa) * (DTmin/DTb)**(DTb/DTa) )**z


# TODO: Define TI


# TODO: Make a plot for TI vs T
plt.style.use('ggplot')
plt.figure(1)
plt.plot(T, Ti, label='Temperature Index')
plt.xlabel('Temperature [°C]')
plt.ylabel('Temperature Index')
plt.title('Temperature Index vs. Temperature')
plt.legend()
plt.savefig("data/temperature_index.pdf")
