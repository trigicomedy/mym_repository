import math

def Simpson(f,a,b):
    h = (b-a)/2
    return h/3*(f(a)+4*f((a+b)/2)+f(b))

def func(x):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x

value = Simpson(func,0,1.0)
print ('result = ',value)
