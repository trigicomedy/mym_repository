import math 
import numpy as np
def func( x ):
    return x**3-x-1 #原函数
def Secant( func,x0,x1,tol): 
    k=0
    while(abs(x1-x0)>tol):
        k+=1
        x2=x1-func(x1)*(x1-x0)/(func(x1)-func(x0))
        x0=x1
        x1=x2
        x1 = np.around(x1,4)
        print(x1)
    print('迭代次数=',k)
    return x1
if __name__=='__main__': 
    value= Secant(func,1.0,2.0,10**(-4)) 
    print("solution =",value)