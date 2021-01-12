import math

def f(t,y):
    return -100*(y-t**2)+2*t

def Runge_Kutta_2order(xspan,y0,h):
    t = xspan[0]
    y=y0
    while( 1 ):
        k1 = f(t,y)
        k2 = f(t+h/2,y+k1/2*h)
        y = y + h*k2
        t+=h
        if(t>xspan[1]):break
    return y
if __name__=='__main__':
    y2=1
    y1=0
    h=0.1
    while(abs(y2-y1)>0.01):
        y1=Runge_Kutta_2order([0,1.0],1.0,h)
        y2=Runge_Kutta_2order([0,1.0],1.0,h/2)
        h/=2
    print('result=',y2,'\n','Calculated step=',h)

