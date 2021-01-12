import numpy as np

def Newton_Interpolation(points, x):
    n = len(points)

    N = points[:,1]

    for i in range(n):
        for j in range(n-1,i,-1):
            N[j] = (N[j] - N[j-1]) / ( points[j,0] - points[j-1-i,0] )
            
    y = points[0,1]#第一个y
    for i in range(1,n):
        for j in range(i):
            N[i] = N[i] * ( x - points[j,0] )
        y = y + N[i]
            
    return y


points = np.array([ [ -0.1,  0.995  ],
                    [ 0.3 ,  0.955  ],
                    [ 0.7 ,  0.765  ] ,
                    [ 1.1 ,  0.454  ] ])

x_interp = 0.2                                   
y_interp = Newton_Interpolation(points, x_interp)
print( "x = ", x_interp, ", Interpolated y  = ", y_interp )