__author__ = 'student'

import numpy as np
import sys

def fdAmerican(callput, S0, K, r, T, sigma, q, M, N, S_max):
    dS = S_max / float(M)
    dt = T / float(N)
    tol = 0.001
    i_values = np.arange(M+1)
    j_values = np.arange(N+1)
    grid = np.zeros(shape=(M+1, N+1))
    boundary_conds = np.linspace(0, S_max, M+1)

    if callput == 1:
            payoffs = np.maximum(boundary_conds[1:M]-K, 0)
    else:
            payoffs = np.maximum(K-boundary_conds[1:M], 0)

    past_values = payoffs
    boundary_values = K * np.exp(-(r-q) * dt * (N-j_values))

    alpha = 0.25*dt*((sigma**2)*(i_values**2) - (r-q)*i_values)
    beta = -dt*0.5*((sigma**2)*(i_values**2) + (r-q))
    gamma = 0.25*dt*((sigma**2)*(i_values**2) + (r-q)*i_values)
    M1 = -np.diag(alpha[2:M], -1) + np.diag(1-beta[1:M]) - np.diag(gamma[1:M-1], 1)
    M2 = np.diag(alpha[2:M], -1) + np.diag(1+beta[1:M]) + np.diag(gamma[1:M-1], 1)

    aux = np.zeros(M-1)
    new_values = np.zeros(M-1)

    for j in reversed(range(N)):
        aux[0] = alpha[1]*(boundary_values[j] + boundary_values[j+1])
        rhs = np.dot(M2, past_values) + aux
        old_values = np.copy(past_values)
        error = sys.float_info.max

        while tol < error:
            new_values[0] =  max(payoffs[0], old_values[0] + 1.0/(1-beta[1]) *
                    (rhs[0] - (1-beta[1])*old_values[0] + (gamma[1]*old_values[1])))

            for k in range(M-2)[1:]:
                new_values[k] = max(payoffs[k], old_values[k] + 1.0/(1-beta[k+1]) *
                        (rhs[k] + alpha[k+1]*new_values[k-1] - (1-beta[k+1])*old_values[k] +
                         gamma[k+1]*old_values[k+1]))

            new_values[-1] = max(payoffs[-1], old_values[-1] + 1.0/(1-beta[-2]) *
                    (rhs[-1] + alpha[-2]*new_values[-2] - (1-beta[-2])*old_values[-1]))

            error = np.linalg.norm(new_values - old_values)
            old_values = np.copy(new_values)

        past_values = np.copy(new_values)

    values = np.concatenate(([boundary_values[0]], new_values, [0]))

    return np.interp(S0, boundary_conds, values)

if __name__ == "__main__":
    optionprice = fdAmerican(-1, 50, 50, 0.1, 5./12., 0.4, 0.1, 100, 1000, 100)
    print optionprice
