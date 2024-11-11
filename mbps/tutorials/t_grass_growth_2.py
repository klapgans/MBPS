# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   --- Fill in your team names ---
Tutorial: Grass growth model analysis.
2. Irradiance trhoughout day
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# TODO: define a function fcn_I0
# with positional arguments tau, h and J
# that returns I0 [W m-2]
# Remember to apply any unit conversion in the function, or its arguments.
def fcn_I0(tau, h, J):
    """
    Calculate the irradiance I0 [W m-2] throughout the day.
    tau: time [hr]
    h: day length [hr]
    J: daily radiation [J cm-2]

    Returns
    -------
    I0: np.ndarray: irradiance [W m-2]
    """
    I0=(2*J)/h*np.sin((np.pi*tau)/h)**2
    return I0

# TODO: Define an array for 24 hr, with time step of 1 min.
# Use the function linspace.    
tau = np.linspace(0,24, 24*60)

# Reference values
# A nice and fresh liberation day at Wageningen (05/05/2022)
# TODO: Enjoy a Bevrijdingsfestival in Wageningen
h = 15.0    # [hr], (Time and Date AS, 2022)
J = 1517.0  # [J cm-2], (KNMI, 2022)

# TODO: calculate the area below the function curve 'fcn_I0'
# to determine the daily radiation R.
# Use the function 'quad'
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html
# Verify whether J = R.
R = quad(fcn_I0, 0, 15, args=(h, J))[0]

assert np.isclose(J, R), "The daily radiation is not equal to J"

# TODO: plot I0 vs tau for h = 8, 15, and 24 [hr]
plt.style.use('ggplot')
plt.figure(1)

# Plot I0 vs tau for h = 8, 15, and 24 [hr]
plt.plot(tau, fcn_I0(tau, 8, J), label='h = 8')
plt.plot(tau, fcn_I0(tau, 15, J), label='h = 15')
plt.plot(tau, fcn_I0(tau, 24, J), label='h = 24')
plt.xlabel('Time [hr]')
plt.ylabel('Irradiance [W m-2]')
plt.title('Irradiance throughout the day')
plt.legend()
plt.grid(True)
plt.savefig("data/irradiance_day.pdf")

### References
# [1] Time and Date AS (accesed Sep 2022),
# https://www.timeanddate.com/sun/netherlands/wageningen?month=5&year=2022

# [2] KNMI (accesed Sep 2022), Weather station De Bilt 260,
# https://www.knmi.nl/nederland-nu/klimatologie/daggegevens