import math

def TrapeZoidal(f,a,b):
    return 0.5*(b-a)*(f(a)+f(b))

def func(x):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
if __name__=='__main__': 
    value = TrapeZoidal(func,0,1.0)
    print ('result = ',value)


    
