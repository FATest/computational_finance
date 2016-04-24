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
q = 0

d1 = (log(float(S0)/K))+((r-q)+sigma*sigma/2.)*T/(sigma*sqrt(T))
d2 = d1-sigma*sqrt(T)
Vbsm = K*exp(-r*T)*norm.cdf(-d2)-S0*exp(-q*T)*norm.cdf(-d1)

#m=5
error = []

# Simulation Parameters
I = 25000
M = 50
dt = T/M
df = math.exp(-r * dt)

# Stock Price Paths
S = S0 * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt
    + sigma * math.sqrt(dt) * np.random.standard_normal((M + 1, I)), axis=0))
S[0] = S0
# Inner Values
h = np.maximum(K - S, 0)
# Present Value Vector (Initialization)
V = h[-1]

for m in range(1, 7):
    L = np.array([[0] * I] * (m+1))
    #American Option
    for t in xrange(M-1, 0, -1):
        L[0] = np.ones(I)
        L[1] = (np.ones(I) - S[t]) * L[0]
        for k in range(1, m):
            L[k+1] = ((2 * k + 1 - S[t]) * L[k] - k * L[k-1])/(k+1)
        A = np.matrix([[0.0] * (m+1)] * (m+1))
        b = np.array([0.0] * (m+1))
        for i in range(m+1):
            for j in range(m+1):
                A[i, j] = np.dot(L[i], L[j])
            b[i] = np.dot(L[i], V * df)#
        LF = np.linalg.cholesky(A)
        y = np.linalg.solve(LF, b)
        rg = np.linalg.solve(LF.T, y)
        c = 0
        for i in range(0, m+1):
            c += rg[i] * L[i]
        V = np.where(h[t] > c, h[t], V * dt)#

    # exercise decision
    V0 = df*np.sum(V)/I #LSMestimator

    error.append(abs(V0 - Vbsm))

print error

plt.xlabel('Order of Polynomial for LS regression')
plt.ylabel('Errors')
plt.plot(range(1, 7), error)
plt.show()
