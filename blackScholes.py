__author__ = 'student'
from scipy.stats import norm
from math import *

def bsformula( callput, S0, K, r, T, sigma, q=0.):
    """
    :param callput: Indicates if the option is a Call or Put option
    :param S0: Stock price
    :param K: Strike price
    :param r: Risk-free rate
    :param T: Time to expiration
    :param sigma: Volatility
    :param q: Dividend rate
    :return: Value of the option, its Delta, its Vega
    """
    d1=(log(float(S0)/K))+((r-q)+sigma*sigma/2.)*T/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    if callput==1:
        optionValue=S0*exp(-q*T)*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
        delta=norm.cdf(d1)
    elif callput==-1:
        optionValue=K*exp(-r*T)*norm.cdf(-d2)-S0*exp(-q*T)*norm.cdf(-d1)
        delta=-norm.cdf(-d1)

    vega=S0*sqrt(T)*norm.pdf(d1)
    return optionValue,delta,vega

if __name__ == "__main__":
    coptionValue,cdelta,cvega = bsformula(1,100,100,0.05,1,0.04)
    poptionValue,pdelta,pvega = bsformula(-1,100,100,0.05,1,0.04)

    print "Call option value is:", coptionValue
    print "Call delta is:", cdelta
    print "Call vega is:", cvega

    print "Put option value is:", poptionValue
    print "Put delta is:", pdelta
    print "Put vega is:", pvega


