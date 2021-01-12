import numpy as np
import math 

def pow(matrixA,ep,Nmax):
    num_of_row=matrixA.shape[0]
    eigenvector=np.ones((num_of_row,1))
    #print(matrixA,'tdask')
    m1=0.0
    for k in range(Nmax):
        v   = np.matmul(matrixA,eigenvector)
        #print(v)
        pos = np.unravel_index(np.argmax(np.abs(v)),v.shape)#argmax返回最大值的索引，矩阵也可以


        m   = v[pos[0]]#m获取最大值

#        if m==0:
#            m=0.00001
#        else:
        eigenvector   = v/m
        if (abs((m-m1)/m)<ep):
            print("迭代次数",k)
            break
        m1=m
        print("eigenvector")
        print(eigenvector)
        print('eigenvalue')
        print(m)
        k+=1
    return m,eigenvector
        #pos = np.unravel_index(np.argmax(a),a.shape)

if __name__=='__main__': #仅在直接运行这块代码时执行以下的代码，如果被调用则不会运行
    #matrixA=np.matrix([[2,4,6],[3,9,15],[4,16,36]])
    matrixA=np.matrix([[-1,-1,0.000],[-1,0,2],[1,1,3]])
    m,eigenvector=pow(matrixA,0.00000001,3)
    print("eigenvector")
    print(eigenvector)
    print('eigenvalue')
    print(m)
