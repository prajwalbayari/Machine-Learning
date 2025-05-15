import numpy as np

#Creating matrix using numpy
matrix1=np.array([[2,3],[6,7]])
print(f"Matrix 1:\n{matrix1}")
print(f"Shape of the matrix: {matrix1.shape}") #Shape of matrix

matrix2=np.array([[10,35,45],[50,60,80],[20,15,90]])
print(f"\nMatrix 2:\n{matrix2}")

#Creating matrix with random values

random_matrix=np.random.rand(3,3)
print(f"\nRandom matrix with float values:\n{random_matrix}")#Float

random_matrix_int=np.random.randint(100,size=(3,3)) #Integer
print(f"\nRandom matrix with int values:\n{random_matrix_int}")

#Matrix with all ones

matrix3=np.ones((10,10),dtype=int)
print(f"\nMatrix with only ones:\n{matrix3}")

#Null matrix
matrix4=np.zeros((4,4),dtype=int)
print(f"\nMatrix with only zeros:\n{matrix4}")

#Identity matrix:
identity=np.eye(3,3)
print(f"\nIdentity matrix:\n{identity}")

#Transpose
a=np.random.randint(100,size=(4,5))
print(f"\nMatrix:\n{a}")
print(f"\nTranspose of the matrix :\n{np.transpose(a)}")

#Matrix addition and subtraction
A=np.random.randint(100,size=(4,4))
B=np.random.randint(100,size=(4,4))
print(f"\nMatrix A:\n{A}\nMatrix B:\n{B}\nA+B:\n{np.add(A,B)}\nA-B:\n{np.subtract(A,B)}") #A+B and A-B also works

#Multilplying the matrix with a scalar
print(f"\nA:\n{A}\nA*2=\n{A*2}")

#Multiplying 2 matrices
print(f"A*B=\n{np.multiply(A,B)}") #A*B also works