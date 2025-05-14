import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

#Plotting a vector
plt.quiver(0,0,4,5,scale_units='xy',angles='xy',scale=1,color='b')
plt.quiver(0,0,-3,-2,scale_units='xy',angles='xy',scale=1,color='y')
plt.quiver(0,0,3,-2,scale_units='xy',angles='xy',scale=1,color='r')
plt.quiver(0,0,-3,4,scale_units='xy',angles='xy',scale=1,color='g')
plt.xlim(-8,8)
plt.ylim(-8,8)
# plt.show()

#Addition of 2 vectors

vector_1=np.asarray([0,0,2,3])
vector_2=np.asarray([0,0,3,-2])
sum=vector_1+vector_2
print(f"1st vector = {vector_1},2nd vector = {vector_2}\nSum = {sum}")

#Subtraction of 2 vectors

vector_3=np.asarray([0,0,2,3])
vector_4=np.asarray([0,0,3,-2])
dif=vector_3-vector_4
print(f"\n1st vector = {vector_3},2nd vector = {vector_4}\nDifference = {dif}")

#Multiplying a vector by a scalar
print(f"\nVector={vector_1}\nVector*2 ={vector_1*2}")
print(f"\nVector={vector_2}\nVector*(-0.5) ={vector_2*(-0.5)}")


# Dot product of 2 vectors

a=np.array([2,3])
b=np.array([4,4])
print(f"\nVector1={a} Vector2={b}\nDot Product={np.dot(a,b)}")

#Cross product of 2 vectors
c=np.array([1,2,3])
d=np.array([4,5,6])
print(f"\nVector1={c} Vector2={d}\nCross Product={np.cross(c,d)}")

#Projection of vec1 on vec2

vec1=np.array([2,5])
vec2=np.array([8,-6])
mag=np.sqrt(np.sum(vec2**2)) #Magnitude of vector

proj=(np.dot(vec1,vec2)/mag**2)*vec2
print(f"\nvec1={vec1} vec2={vec2}\nProjection of vec1 on vec2 is {proj}")