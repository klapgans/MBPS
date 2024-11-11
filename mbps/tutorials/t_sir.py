# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   -- add your team names here --

Tutorial for the disease model (SIR)
"""
# TODO: Create the script to simulate the SIR model,
# and analyse parameter beta.
from matplotlib import pyplot as plt
import numpy as np
from mbps.models.sir import SIR


tsim = np.linspace(0,365,366)   # [d]

dt = 7
susceptible= 0.99
infected= 0.01
recovered= 0.0
beta= 0.5
gamma= 0.02

model = SIR(tsim, dt,
            x0 = {"susceptible": susceptible,
            "infected": infected,
            "recovered": recovered},
            p = {"beta": beta,
            "gamma": gamma})

tspan = (tsim[0],tsim[-1])
y = model.run(tspan)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(y['t'], y['susceptible'], label='Susceptible')
plt.plot(y['t'], y['infected'], label='Infected')
plt.plot(y['t'], y['recovered'], label='Recovered')
plt.xlabel('Time [days]')
plt.ylabel('Population Fraction')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid(True)
plt.savefig("sir_model.pdf")