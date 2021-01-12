import math
import numpy as np
import Q2_6_1power_iteration
A=np.matrix([[2,-1,3],[4,2,5],[1,2,0]])
Q,R=np.linalg.lu(A)
print(Q,R)
#m,eigenvector=pow(A,0.1,3)
#print(m,'\n',eigenvector,'\n')
