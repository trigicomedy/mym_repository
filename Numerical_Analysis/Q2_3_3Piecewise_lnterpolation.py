import math 
import numpy as np

def Piecewise_lnterpolation(points, x):
    n = len(points)
    y = 0
    for i in range(n-1):
        if ((x>points[i,0]) & (x<points[i+1,0])):
            return points[i,1]+(x-points[i,0])/(points[i+1,0]-points[i,0])*(points[i+1,1]-points[i,1])


#def f(x):
#    return 1.0/x

# the following is problem dependent
#points = np.array([ [ 2.0,  f(2.0)  ],
#                    [ 2.75, f(2.75) ],
#                    [ 4.0,  f(4.0)  ] ])
if __name__=='__main__': 
    points = np.array([ [ -0.1,  0.995  ],
                        [ 0.3 ,  0.955  ],
                        [ 0.7 ,  0.765  ] ,
                        [ 1.1 ,  0.454  ] ]) 

    x_interp = 0.2
    y_interp = Piecewise_lnterpolation(points, x_interp)
    print( "x = ", x_interp, ", Interpolated y  = ", y_interp )