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
    matrixDL_inv=np.linalg.inv(matrixD+ matrixL)
    for i in range(Nmax):
        x= -1*np.dot(np.dot(matrixDL_inv,matrixU),x)+np.dot(matrixDL_inv,b)
    print(x)
    return x
if __name__=='__main__': #仅在直接运行这块代码时执行以下的代码，如果被调用则不会运行
    matrixA = np.array([[4,-2,1.0],[-2,17,1],[1,1,9]])
    b = np.array([[-1],[33.0],[10]])
    gauss_seidel_iteration(matrixA,b,10)


