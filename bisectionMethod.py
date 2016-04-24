__author__ = 'student'

import numpy as np
import math

def bisect(target, targetfunction, start=None, bounds=None, tols=[0.01,0.01], maxiter=100):
    """
    :param target: The target of the function
    :param targetfunction: The function to solve
    :param start: The starting value to find bounds
    :param bounds: The bounds to check for a solution
    :param tols: The precision of the solution
    :param maxiter: Maximum number of iterations
    :return: The x-axis value of the root, number of iterations used,
            array with the series of x-values
    """
    if bounds!=None:
        a=bounds[0]
        b=bounds[1]
        if (np.sign(targetfunction(a)) == np.sign(targetfunction(b))):
            raise ValueError("Bounds do not contain a solution")

    else:
        i=1
        for i in range (1,1000):
            a=start-(tols[0]*math.pow(2,i))
            b=start+(tols[0]*math.pow(2,i))
            if (np.sign(targetfunction(a)) != np.sign(targetfunction(b))):
                break
        if (np.sign(targetfunction(a)) == np.sign(targetfunction(b))):
            raise ValueError("Bounds do not contain a solution")



    n=1
    root_arr=[]
    while n<=maxiter:
        c=(a+b)*0.5
        root_arr.append(c)
        if len(root_arr)>=maxiter:
            raise ValueError("Maximum iteration count is reached")
        if targetfunction(c)==target or abs(a-b)*0.5<tols[1]:
             return c,n, root_arr

        n+=1
        if targetfunction(c)<target:
            a=c
        else:
            b=c

    return c,n,root_arr


if __name__ == "__main__":
    y = lambda x: x**3 + 2*x**2 - 5
    try:
        #root, iterations, array = bisect(0,y,bounds=[-5,5])
        root, iterations, array = bisect(0,y,start=10)
        print "Root is:", root
        print "Iterations:", iterations
        print "Final element of array:", array[len(array)-1]
        print "Number of calls made to target function:", len(array)
    except ValueError as e:
        print(e.args)



