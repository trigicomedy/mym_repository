import math 
import numpy as np
def func1( x ):
    return x**3-x-1 #原函数
def func_derivatives( x ):
    return 3*x**2-1#导数
def NewtonsNonlinear(funcl,func2,a,tol):
    k=0
    b = a -funcl(a )/func2(a) 
    b = np.around(b,4)
    while abs( b - a)>tol :
        print('bb',b)
        k+=1
        a = b
        b = a- funcl(a )/func2(a)
        b = np.around(b,4)
        
    print('迭代次数=',k)
    return b
if __name__=='__main__': 
    value = NewtonsNonlinear(func1,func_derivatives,1.5,0.000000001) 
    print ("solution =",value)