__author__ = 'student'

from scipy.stats import norm
from math import *
from Bisect import bisect
from BS import bsformula
import numpy as np

def newton(callput, S0, K, r, T , q, price, sigma, tolerance, it=100 ):
     """
    :param callput: Indicates if the option is a Call or Put option
    :param S0: Stock price
    :param K: Strike price
    :param r: Risk-free rate
    :param T: Time to expiration
    :param q: Dividend rate
    :param price: Price of option
    :param sigma: Initial Volatility
    :param tolerance: The precision of the solution
    :param it: Maximum number of iterations
    :return: Implied volatility
    """
     i=0
     vega_init=0
     while i<it:
            bsret=bsformula(callput, S0, K, r, T, sigma, q)
            optionValue=bsret[0]
            vega=bsret[2]

            if (vega==0):
                return sigma
            vega_init=vega
            sigma_est=float(sigma)-(float(optionValue)-float(price))/float(vega)
            if (abs(sigma_est-sigma)<tolerance):
                return sigma_est

            sigma=sigma_est
            i+=1
     return float('NaN')


def bsimpvol(callput, S0, K, r, T, price, q=0., priceTolerance=0.01, method='bisect' ):
    """
    :param callput: Indicates if the option is a Call or Put option
    :param S0: Stock price
    :param K: Strike price
    :param r: Risk-free rate
    :param T: Time to expiration
    :param price: Price of option
    :param q: Dividend rate
    :param priceTolerance: The precision of the solution
    :param method: Specifies if Bisection method or Newton's method is to be used
    :return: Implied Volatility
    """
    sigma=0.5
    def targetfunction(x):
        return bsformula(callput, S0, K, r, T, x, q)[0]

    if (isnan(S0) or isnan(K) or isnan(r) or isnan(T) or isnan(price)):
        return float('NaN')
    if ((callput==1 and price < (S0-K)) or (callput==-1 and price < (K-S0))):
        return float('NaN')

    if method=='newton':
        sigma_est = newton(callput, S0, K, r, T, q, price, sigma, priceTolerance)
    if method=='bisect':
        sigma_est=(bisect(price,targetfunction, start=0.5, tols= [priceTolerance,priceTolerance]))[0]

    return sigma_est
if __name__ == "__main__":

    #sig=bsimpvol(1,231.64,210,0.1396512,0.0547945,25.8)
    sig=bsimpvol(-1,231.64,210,0.1396512,0.0547945,2.13)
    print "Implied volatility is:", sig