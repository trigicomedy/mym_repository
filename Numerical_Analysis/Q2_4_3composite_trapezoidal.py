import math
def CompositeTrapeZoidal(a,b,n):
    h = (b-a)/n
    T = 0
    for i in range(n):
        T +=  TrapeZoidal(func,a+i*h,a+(i+1)*h)
    return T

def TrapeZoidal(f,a,b):
    return 0.5*(b-a)*(f(a)+f(b))

def func(x):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
value = CompositeTrapeZoidal(0,1.0,10)
print ('result = ',value)
