__author__ = 'student'

from numpy import exp, sqrt, maximum, mean, std, prod, sum
import scipy.stats as st
import numpy as np
from numpy import shape, reshape

def MCStockPrices( S0, sigma, r, t, samples, integrator):

    if integrator is 'standard':
        z=st.distributions.norm.ppf(samples)
        standard_s=[]
        standard_St_prices=[]
        
        for i in range(len(samples)):
            if i == 0:
                d_t = t[i]
            else:
                d_t = t[i]-t[i-1]
            
            standard_S = S0*exp((r-0.5*sigma**2)*d_t + sigma*sqrt(d_t)*z[i,:])
            standard_St_prices.append(standard_S)
            S0=standard_S
        
        return standard_St_prices
        


    if integrator is 'euler':
        z=st.distributions.norm.ppf(samples)
        euler_s=[]
        euler_St_prices=[]

        for i in range(len(samples)):
            if i == 0:
                d_t = t[i]
            else:
                d_t = t[i]-t[i-1]

            euler_S = (S0+S0*(r)*d_t + S0*sigma*sqrt(d_t)*z[i,:])
            euler_St_prices.append(euler_S)
            S0=euler_S

        return euler_St_prices

    if integrator is 'milstein':

        z=st.distributions.norm.ppf(samples)
        delStochCoeffdelAsset = sigma
        milstein_s=[]
        milstein_St_prices=[]

        for i in range(len(samples)):
            if i == 0:
                d_t = t[i]
            else:
                d_t = t[i]-t[i-1]

            milstein_S = S0 + S0*(r)*d_t+ S0*sigma*sqrt(d_t)*z[i,:] + S0* 0.5*sigma*delStochCoeffdelAsset*(z[i,:]**2*d_t-d_t)
            milstein_St_prices.append(milstein_S)
            S0=milstein_S

        return milstein_St_prices


if __name__ == "__main__":
    S0 = 100; sigma = 0.4; r = 0.05;
    t = [0.5, 0.75, 1.0, 1.5, 2.0, 2.5]
    M = 10
    samples = np.random.rand(len(t), M)
    stk_prices = MCStockPrices(S0, sigma, r, t, samples, 'standard')
    print np.shape(stk_prices)
    print np.ndim(stk_prices)
    print stk_prices

