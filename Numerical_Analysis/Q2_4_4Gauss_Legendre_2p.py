import math
import numpy as np
def Gauss_Legendre_2p(f,a,b):
    return 0.5*(f(-1/np.sqrt(3))+f(1/np.sqrt(3)))

def func(x):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
if __name__=='__main__': 
    value = Gauss_Legendre_2p(func,0,1.0)
    print ('result = ',value)