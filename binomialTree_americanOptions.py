__author__ = 'student'

import math
import numpy as np

def binomialAmerican(S0, Ks, r, T, sigma, q, callputs, M):
    dt = T/M
    df = math.exp(-(r-q)*dt)
    u = math.exp(sigma * math.sqrt(dt))
    d = 1./u
    qu = (math.exp((r-q)*dt) - d)/(u-d)
    qd = 1-qu

    STs = [np.array([S0])]

    for i in range(M):
        prev_branches = STs[-1]
        st = np.concatenate((prev_branches*u, [prev_branches[-1]*d]))
        STs.append(st)

    payoffs = []
    for i in range(len(Ks)):
        payoffs_temp = np.maximum(0, (STs[M]-Ks[i]) if callputs[i]==1 else (Ks[i]-STs[M]))
        payoffs.append(payoffs_temp)



    fin_payoffs = []
    early_ex_payoffs = []
    for i in range(len(Ks)):
        for j in reversed(range(M)):
            payoffs[i] = (payoffs[i][:-1] * qu + payoffs[i][1:] * qd) * df
            early_ex_payoffs_temp = (STs[j] - Ks[i]) if callputs[i] == 1 else (Ks[i] - STs[j])
        early_ex_payoffs.append(early_ex_payoffs_temp)

        fin_payoffs.append(np.maximum(payoffs[i], early_ex_payoffs[i]))

    return fin_payoffs

if __name__ == "__main__":
    S0 = 40
    Ks = [35, 40, 45]
    r = 0.05
    T = 1.2
    sigma = 0.4
    q = 0.01
    callputs = [1, -1, -1]
    M = 10
    payoffs = binomialAmerican(S0, Ks, r, T, sigma, q, callputs, M)
    print payoffs
