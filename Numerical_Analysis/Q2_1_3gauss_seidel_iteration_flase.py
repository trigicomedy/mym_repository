import numpy as np
import math 
def gauss_seidel_iteration(matrixA,b,Nmax):
    x=np.zeros((len(matrixA[0,:]),1))
    matrixL=matrixA.copy()
    matrixD=matrixA.copy()
    matrixU=matrixA.copy()
    for i in range(len(matrixA[0,:])):
        for j in range(len(matrixA[0,:])):
            if i==j:#对角线lu都是0
                matrixL[i,j]=0
                matrixU[i,j]=0
            else:#非对角线D都是0
                matrixD[i,j]=0
            if i>j:
                matrixU[i,j]=0
            if i<j:
                matrixL[i,j]=0
    matrixD_inv=np.linalg.inv(matrixD)
    for i in range(Nmax):
        matrixLX=generate_LX(matrixL,generate_x1(matrixA,x,b))
        x=np.dot(matrixD_inv,(b-np.dot(matrixU,x)-matrixLX))
        #print(x)
        #print(matrixU)
    print(x)
    return x
def generate_x1(matrixA,x,b):
    a11=matrixA[0,0]
    matrixA1=matrixA[0,:].copy()
    matrixA1[0]=0
    return (b[0,0]-np.dot(matrixA1,x)[0])/a11
def generate_LX(matrixL,x1):
    x=np.zeros((len(matrixL[0,:]),1))
    x[0,0]=x1
    for i in range(len(matrixL[0,:])):
        if i==0:
            continue
        x[i,0]=np.dot(matrixL[i,:],x)[0]
    x[0,0]=0
    return x


if __name__=='__main__': #仅在直接运行这块代码时执行以下的代码，如果被调用则不会运行
    matrixA = np.array([[4,-2,1.0],[-2,17,1],[1,1,9]])
    b = np.array([[-1],[33.0],[10]])
    gauss_seidel_iteration(matrixA,b,10)


