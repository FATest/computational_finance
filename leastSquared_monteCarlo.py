__author__ = 'DushyanthK'
#
# Valuation of American Options
# with Least-Squares Monte Carlo #
import math

import numpy as np
from numpy.polynomial import laguerre
from scipy.stats import norm
from math import *
import matplotlib.pyplot as plt

np.random.seed(150000)

# Model Parameters
S0=36. #initialstocklevel
K=40. #strikeprice
T=1.0 #time-to-maturity
r=0.06 #shortrate
sigma=0.2 #volatility
q=0.0

d1 = (log(float(S0)/K))+((r-q)+sigma*sigma/2.)*T/(sigma*sqrt(T))
d2 = d1-sigma*sqrt(T)
Vbsm = K*exp(-r*T)*norm.cdf(-d2)-S0*exp(-q*T)*norm.cdf(-d1)

error = []
for m in range(1, 10):
    # Simulation Parameters
    I = 25000
    M = 50
    dt=T/M
    df = exp(-r * dt)

    # Stock Price Paths
    S = S0 * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt
        + sigma * math.sqrt(dt) * np.random.standard_normal((M + 1, I)), axis=0))
    S[0] = S0
    # Inner Values
    h = np.maximum(K - S, 0)
    # Present Value Vector (Initialization)
    V = h[-1]
    
    # American Option Valuation by Backwards Induction
    for t in xrange(M - 1, 0, -1):
        rg= laguerre.lagfit(S[t], V * df, m)
        C = laguerre.lagval(S[t], rg)# continuation values V = np.where(h[t] > C, h[t], V * df)

    # exercise decision
    V0 = df*np.sum(V)/I #LSMestimator
    error.append(abs(V0 - Vbsm))

print error

plt.xlabel('Order of Polynomial for LS regression')
plt.ylabel('Errors')
plt.plot(range(1, 10), error)
plt.show()