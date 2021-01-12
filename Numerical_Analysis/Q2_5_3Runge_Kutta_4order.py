import math
import numpy as np
def f(t,y):
    return y-2*t/y
def Runge_Kutta_4order(xspan,y0,h):
    t = xspan[0]
    y=y0
    while( 1 ):
        k1 = h*f(t,y)
        k2 = h*f(t+h/2,y+k1/2)
        k3 = h*f(t+h/2,y+k2/2)
        k4 = h*f(t+h,y+k3)
        y = y + (k1+2*k2+2*k3+k4)/6
        y=np.around(y,4)
        print(y)
        t = t + h
        if(t>xspan[1]):break
    return y
if __name__=='__main__':
    y1=0
    Runge_Kutta_4order([0,1],1,0.2)
    h=0.2
