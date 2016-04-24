__author__ = 'student'

from numpy import exp, sqrt, maximum
import scipy.stats as st
import numpy as np

def mcvanilla(callput, S, K, sigma, r, q, T, checkpoints, samples):

    M = checkpoints[-1]

    if len(samples) < M:
        raise IndexError("Number of samples is less than last entry in 'checkpoints'")

    zp = st.distributions.norm.ppf(samples)
    za = np.concatenate((zp, -zp))
    price_samples = S * exp(((r-q)-0.5*sigma**2)*T + sigma*sqrt(T)*za)

    if callput == 1:
        vals = exp(-(r-q)*T) * maximum(0, price_samples-K)
    elif callput == -1:
        vals = exp(-(r-q)*T) * maximum(0, K-price_samples)
    val = []
    for i in range(len(checkpoints)):
        val.append(vals[checkpoints[i]])
    return val

if __name__ == "__main__":
    K = 110; S = 100; r = 0.05; sigma = 0.4; T = 2.5; q = 0.0; callput = 1
    chkpnts = []
    samples = []
    for i in range(4, 20):
        chkpnts.append(pow(2, i))
    for j in range(chkpnts[-1]):
        samples.append(np.random.rand())
    try:
        price = mcvanilla(callput, S, K, sigma, r, q, T, chkpnts, samples)
        print price
    except IndexError as e:
        print(e.args)
