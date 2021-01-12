import math
import numpy as np
import Q2_6_1power_iteration
A=np.matrix([[-1,-1,0.000],[-1,0,2],[1,1,3]])
Q,R=np.linalg.qr(A)
U=Q
for i in range(20):
    A2=R*Q
    Q,R=np.linalg.qr(A2)
    U=U*Q
A3=R*Q
#print(Q,'\n',R,'\n')
print("eigenvector")
print(U)
print('eigenvalue')
print(A3)
#m,eigenvector=pow(A,0.1,3)
#print(m,'\n',eigenvector,'\n')
