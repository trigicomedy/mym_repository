import math 
import numpy as np

def lagrange_interpolation(points, x):
    n = len(points)

    y = 0

    for i in range(n):
        term = points[i, 1]
        for j in range(n):
            if ( j != i ):
                term = term * ( x - points[j,0] ) / ( points[i,0] - points[j,0] )
        y = y + term
    return y

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
    y_interp = lagrange_interpolation(points, x_interp)
    print( "x = ", x_interp, ", Interpolated y  = ", y_interp )