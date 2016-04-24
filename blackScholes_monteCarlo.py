__author__ = 'student'

from numpy import exp, sqrt, maximum, mean, std, prod
import scipy.stats as st
import numpy as np

def BSMonteCarlo(S0, K, T, r, sigma, checkpoints, samples=None):

    M = checkpoints[-1]

    if samples is None:
        samples = []
        for i in range(M):
            samples.append(np.random.rand())

    if len(samples) < M:
        raise IndexError("Number of samples is less than last entry in 'checkpoints'")

    z = st.distributions.norm.ppf(samples)
    price_samples = S0 * exp((r-0.5*sigma**2)*T + sigma*sqrt(T)*z)
    vals = exp(-r*T) * maximum(0, price_samples-K)
    val = mean(vals)

    _mean = []
    _stddev = []
    _stderr = []

    for j in range(len(checkpoints)):
        _mean.append(mean(vals[0:checkpoints[j]]))
        _stddev.append(std(vals[0:checkpoints[j]]))
        _stderr.append(std(vals[0:checkpoints[j]])/sqrt(checkpoints[j]))

    return dict([('TV', val), ('Means', _mean), ('StdDevs', _stddev), ('StdErrs', _stderr)])

def BSMonteCarlo_P3(S0, K, T, r, sigma, checkpoints, samples=None):
    
    M = checkpoints[-1]
    
    if samples is None:
        samples = []
        for i in range(M):
            samples.append(np.random.rand())

    if len(samples) < M:
        raise IndexError("Number of samples is less than last entry in 'checkpoints'")
    
    vals = exp(-r*T) * maximum(0, S0-K)
    val = mean(vals)
    
    _mean = []
    _stddev = []
    _stderr = []
    
    for j in range(len(checkpoints)):
        _mean.append(mean(vals[0:checkpoints[j]]))
        _stddev.append(std(vals[0:checkpoints[j]]))
        _stderr.append(std(vals[0:checkpoints[j]])/sqrt(checkpoints[j]))
    
    return dict([('TV', val), ('Means', _mean), ('StdDevs', _stddev), ('StdErrs', _stderr)])

if __name__ == "__main__":
    K = 110; S0 = 100; r = 0.05; sigma = 0.4; T = 2.5;
    chkpnts = [100, 250, 500, 750, 1000]
    try:
        dic = BSMonteCarlo(S0, K, T, r, sigma, chkpnts)
        print dic
    except IndexError as e:
        print(e.args)