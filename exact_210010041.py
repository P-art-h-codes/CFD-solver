import numpy as np

H = 2
L = 1

# N is the no. of iterations because infinite iteration is not possible  
def T(x,y,N):
    T=0
    for n in range(1,N+1):
        ## the term has been broken into two parts for better readability
        value_1 = ( ( 1 - (-1)**n )/(n*np.pi) )
        value_2 = (np.sinh( ( (n*np.pi)/L)*(H-y) )*(np.sin( (n*np.pi*x)/L) ) )/(np.sinh( (n*np.pi*H)/L) )
        value = (250*2)*value_1*value_2
        T += value
    
    return T
