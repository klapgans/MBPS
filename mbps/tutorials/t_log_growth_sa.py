# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
"""

import numpy as np
import matplotlib.pyplot as plt

from mbps.models.log_growth import LogisticGrowth

plt.style.use('ggplot')

# Simulation time array
tsim = np.linspace(0, 10, 100+1)    # [d]
tspan = (tsim[0], tsim[-1])         # [d]

# Initialize and run reference object
dt = 0.1                        # [d] time-step size
x0 = {'m':1.0}                  # [gDM m-2] initial conditions
p_ref = {'r':1.2,'K':100.0}     # [d-1], [gDM m-2] model parameters (ref. values)
lg = LogisticGrowth(tsim,dt,x0,p_ref)   # Initialize object
y = lg.run(tspan)                       # Run object

y_ref_mean = np.mean(y['m'])    # [gDM m-2] average of m through time
# One-at-a-time parameter changes, simulation, S, and NS
# dm/dr-
p_rmin = p_ref.copy()                           # define p with r-
p_rmin['r'] = 0.95*p_ref['r']                   # update value of r-
lg_rmin = LogisticGrowth(tsim, dt, x0, p_rmin)  # initialize object
y_rmin = lg_rmin.run(tspan)                     # run object
S_rmin = (y_rmin['m']-y['m'])/(p_rmin['r']-p_ref['r'])  # sensitivity
NS_rmin = S_rmin*p_ref['r']/y_ref_mean          # normalized sensitivity

# dm/dr+
p_rpls = p_ref.copy()                           # define p with r+
p_rpls['r'] = 1.05*p_ref['r']                   # update value of r+
lg_rpls = LogisticGrowth(tsim, dt, x0, p_rpls)  # initialize object
y_rpls = lg_rpls.run(tspan)                     # run object
S_rpls = (y_rpls['m']-y['m'])/(p_rpls['r']-p_ref['r'])  # sensitivity
NS_rpls = S_rpls*p_ref['r']/y_ref_mean          # normalized sensitivity

# dm/dK-
p_Kmin = p_ref.copy()                           # define p with K-
p_Kmin['K'] = 0.95*p_ref['K']                   # update value of K-
lg_Kmin = LogisticGrowth(tsim, dt, x0, p_Kmin)  # initialize object
y_Kmin = lg_Kmin.run(tspan)                     # run object
S_Kmin = (y_Kmin['m']-y['m'])/(p_Kmin['K']-p_ref['K'])  # sensitivity
NS_Kmin = S_Kmin*p_ref['K']/y_ref_mean          # normalized sensitivity

# dm/dK+
p_Kpls = p_ref.copy()                           # define p with K+
p_Kpls['K'] = 1.05*p_ref['K']                   # update value of K+
lg_Kpls = LogisticGrowth(tsim, dt, x0, p_Kpls)  # initialize object
y_Kpls = lg_Kpls.run(tspan)                     # run object
S_Kpls = (y_Kpls['m']-y['m'])/(p_Kpls['K']-p_ref['K'])  # sensitivity
NS_Kpls = S_Kpls*p_ref['K']/y_ref_mean           # normalized sensitivity


# Plot results
# m with changes in r
plt.figure(1)
plt.plot(y['t'], y['m'], label='Reference')
plt.plot(y_rmin['t'], y_rmin['m'], label='r - 5%')
plt.plot(y_rpls['t'], y_rpls['m'], label='r + 5%')

plt.xlabel('Time [days]')
plt.ylabel('Biomass [gDM m-2]')
plt.title('Biomass vs. Time (changing r ± 5%)')
plt.legend()
plt.grid(True)
plt.savefig("data/biomass_vs_time_r.png")

# m with changes in K
plt.figure(2)
plt.plot(y['t'], y['m'], label='Reference')
plt.plot(y_Kmin['t'], y_Kmin['m'], label='K - 5%')
plt.plot(y_Kpls['t'], y_Kpls['m'], label='K + 5%')
plt.xlabel('Time [days]')
plt.ylabel('Biomass [gDM m-2]')
plt.title('Biomass vs. Time (changing K ± 5%)')
plt.legend()
plt.grid(True)
plt.savefig("data/biomass_vs_time_K.png")

# S on r
plt.figure(3)
plt.plot(y['t'], S_rmin, label='S (r - 5%)')
plt.plot(y['t'], S_rpls, label='S (r + 5%)')
plt.plot(y['t'], NS_rmin, label='NS (r - 5%)')
plt.plot(y['t'], NS_rpls, label='NS (r + 5%)')
plt.xlabel('Time [days]')
plt.ylabel('Sensitivity')
plt.title('Sensitivity vs. Time (changing r ± 5%)')
plt.legend()
plt.grid(True)
plt.savefig("data/sensitivity_vs_time_r.png")

# S on K
plt.figure(4)
plt.plot(y['t'], S_Kmin, label='S (K - 5%)')
plt.plot(y['t'], S_Kpls, label='S (K + 5%)')
plt.xlabel('Time [days]')
plt.ylabel('Sensitivity')
plt.title('Sensitivity vs. Time (changing K ± 5%)')
plt.legend()
plt.grid(True)
plt.savefig("data/sensitivity_vs_time_K.png")


# NS on r and K
plt.figure(5)
plt.plot(y['t'], NS_rmin, label='NS (r - 5%)')
plt.plot(y['t'], NS_rpls, label='NS (r + 5%)')
plt.plot(y['t'], NS_Kmin, label='NS (K - 5%)')
plt.plot(y['t'], NS_Kpls, label='NS (K + 5%)')
plt.xlabel('Time [days]')
plt.ylabel('Normalized Sensitivity')
plt.title('Normalized Sensitivity vs. Time (changing r and K ± 5%)')
plt.legend()
plt.grid(True)
plt.savefig("data/normalized_sensitivity_vs_time.png")

plt.show()