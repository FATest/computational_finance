__author__ = 'student'

from numpy import exp, sqrt, maximum, mean, std, prod
import scipy.stats as st
import numpy as np
from BSMonteCarlo import BSMonteCarlo_P3
from MCStockPrices import MCStockPrices

def MSOptionPrices(S0, K, T, r, sigma, t, checkpoints, samples, integrator):

    if t[-1] < T:
        t.append(T)
    stk_prices = MCStockPrices(S0, sigma, r, t, samples, integrator)
    stk_prices_T = np.array(stk_prices)
    stk_dic = BSMonteCarlo_P3(stk_prices_T[-1,:], K, T, r, sigma, chkpnts)
    return stk_dic

if __name__ == "__main__":
    S0 = 100; K = 110;  T = 2.5; r = 0.05; sigma = 0.4;
    t = [0.5, 0.75, 1.0, 1.5, 2.0, 2.5]
    chkpnts = [100, 250, 500, 750, 1000]
    M = 1000
    samples = np.random.rand(len(t), M)
    try:
        dic = MSOptionPrices(S0, K, T, r, sigma, t, chkpnts, samples, 'standard')
        print dic
    except IndexError as e:
        print(e.args)