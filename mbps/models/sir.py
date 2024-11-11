#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
@authors:   Your team names

Class for disease SIR model
"""
import numpy as np

from mbps.classes.module import Module
from mbps.functions.integration import fcn_euler_forward
from scipy.integrate import solve_ivp

class SIR(Module):
    """ Module for disease spread
    
    Parameters
    ----------
    Add here the parameters required to initialize your object
    
    Returns
    -------
    Add here the model outputs returned by your object
    
    """
    # Initialize object. Inherit methods from object Module
    # TODO: fill in the required code
    def __init__(self,tsim,dt,x0,p):
        Module.__init__(self,tsim,dt,x0,p)
    
    # Define system of differential equations of the model
    # TODO: fill in the required code.
    '''Explanation
    Notice that for the function diff, we use _t and _y0.
    This underscore (_) notation is used to define internal variables,
    which are only used inside the function.
    It is useful here to represent the fact that _t and _y0 are changing
    iteratively, every time step during the numerical integration
    (in this case, called by 'fcn_euler_forward')
    '''
    def diff(self, _t, _y0):
        # State variables
        s, i, r = _y0[0], _y0[1], _y0[2]
        # Parameters
        beta, gamma = self.p['beta'], self.p['gamma']
        # Differential equations
        ds_dt = -beta * s * i
        di_dt = beta * s * i - gamma * i
        dr_dt = gamma * i
        return np.array([ds_dt, di_dt, dr_dt])

    def output(self, tspan):
        # Retrieve object properties
        diff = self.diff
        y0 = [self.x0['susceptible'], self.x0['infected'], self.x0['recovered']]

        # Numerical integration using solve_ivp from scipy
        t_eval = np.linspace(tspan[0], tspan[1], int((tspan[1]-tspan[0])/self.dt)+1)
        sol = solve_ivp(diff, tspan, y0, method='RK45', t_eval=t_eval)

        # Retrieve results from numerical integration output
        t = sol.t
        s, i, r = sol.y[0], sol.y[1], sol.y[2]
        return {'t': t, 'susceptible': s, 'infected': i, 'recovered': r}

