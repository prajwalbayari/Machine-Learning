import numpy as np #Nearly 10 time faster than list

#Numpy arrays
# np_array=np.array([1,2,3,4,5]) #They are not separated by comma
# print(type(np_array))
# print(np_array.shape) #Gives dimensions of the array

#2D array
# np_array=np.array([(1,2,3,4),(1,2,3,4)])
# print(np_array)
# print(np_array.shape)

#2D array with different datatype
# np_array=np.array([(1,2,3,4),(1,2,3,4)],dtype=float)
# print(np_array)

# Initial placeholders 
# x=np.zeros((2,2)) #Array of zeros
# print(x)

#Creating array of particular value
# z=np.full((4,4),4)
# print(z)

#creating an identity matrix
# print(np.eye(4))

#create numpy array with random values within a specific range
# print(np.random.randint(1,10000,(3,4)))

#Array of evenly spaced values specifying the number of values required
# print(np.linspace(0,100,11))

#Array of evenly spaced values specifying the step
# print(np.arange(10,100,5))

#Convert a list to a numpy array
# l=[1,2,3,4,5]
# arr=np.asarray(l)
# print(arr,type(arr))

#Anlalyzing a numpy array
# c=np.random.randint(10,90,(5,5))
# print(c)
# print(c.shape) #Array dimensions
# print(c.ndim) #number of dimensions
# print(c.size) #number of elements
# print(c.dtype) #datatype of elements

#Mathematical operations
# a=np.random.randint(1,10,(5,5))
# b=np.random.randint(1,10,(5,5))
# print(a) 
# print(b)
# print(b+a) #same as np.add(b,a)
# print(a-b) #same as np.subtract(b,a)
# print(a*b) #same as np.multiply(b,a)
# print(a/b) #same as np.divide(b,a)

#Array manipulations
# arr=np.random.randint(0,10,(2,3))
# print(arr.shape,"\n",arr)
# print(np.transpose(arr).shape,"\n",np.transpose(arr)) #Transpose of array same as array.T(arr)

#Reshaping an array
a=np.random.randint(0,10,(2,3))
print(a)
print(a.reshape(1,6))