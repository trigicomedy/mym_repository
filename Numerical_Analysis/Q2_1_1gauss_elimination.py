import numpy as py
 
def set_matrix():
	matrix1 = py.array([[-2,4,8.0],[-4,18,-16],[-6,2,-20]])
	matrix2 = py.array([[5],[8],[7]])
	return matrix1,matrix2

def swap_row(matrix,rowi,rowj):
	temp = 0.0
	for columns in range(len(matrix[0,:])):#这里的[]是指坐标，0是第0行，冒号意为整个所有列都要，加上len就是列长度
		temp = matrix[rowi][columns]
		matrix[rowi][columns] = matrix[rowj][columns]
		matrix[rowj][columns] = temp
	return matrix
 
def times_k(matrix,rowi,rowj,k):
	for columns in range(len(matrix[0,:])):
		matrix[rowj][columns] = -k*matrix[rowi][columns] + matrix[rowj][columns]
	return matrix
 
def up_triangle(matrix):
	for columns in range(len(matrix[:,0])):
		for rows in range(columns,len(matrix[:,0])):
			if matrix[rows][columns] == 0:
				pass
			else:
				swap_row(matrix,columns,rows)
				break		
		for rows in range(columns + 1,len(matrix[:,0])):
			times_k(matrix,columns,rows,matrix[rows][columns]/matrix[columns][columns])
	print('上三角矩阵：')
	print(matrix)
 
def get_result(matrix):
	x = py.matrix(py.zeros(matrix.shape[0])) #生成一个存储结果的矩阵
	n = x.shape[1]-1  						 #（矩阵的大小-1），比如大小为4，n则为最后一个元素，n[0,3],存放最后一个x
	x[0,n] = matrix[n,n+1]/matrix[n,n]       # 先算x(n)：b(n)/a(nn)，即为最后一个x的值
	for i in range(n):  					 # 用回带求依次求出x的值
		n -= 1  
		x[0,n] = (matrix[n,matrix.shape[1]-1] - py.sum(py.multiply(x[0, n+1:], matrix[n,n+1:matrix.shape[1]-1])))/matrix[n,n]  
	print('x的值：')
	print(x.T) 
 
if __name__=='__main__': #仅在直接运行这块代码时执行以下的代码，如果被调用则不会运行
	print('增广矩阵：')	
	matrix3 = py.hstack(set_matrix())  #按列合并：vstack()   按行合并：hstack()
	print(matrix3)
	up_triangle(matrix3)
	get_result(matrix3)