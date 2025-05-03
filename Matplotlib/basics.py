import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)

# print(x)
# print(y)
# print(z)

#Plotting the data

#Sine wave
# plt.plot(x,y)
# plt.show()

#Cosine wave
# plt.plot(x,z)
# plt.xlabel("Angle")   #Naming x and y coordinates 
# plt.ylabel("Cosine value")
# plt.title("Cosine wave") #Naming the plot
# plt.show()

#Plotting a parabola
a=np.linspace(-5,5,20)
b=a**2
# plt.plot(a,b)
# plt.show()

# plt.plot(a,b,'b* ') #Plotting with +symbol (b=blue)
# plt.show()

#Multiple lines in a single plot
c=np.linspace(-5,5,50)
# plt.plot(x,np.sin(x),'g-')
# plt.plot(x,np.cos(x),'r-- ')
# plt.show()

#Bar plot
# fig=plt.figure()
# ax=fig.add_axes([0.1,0.1,0.8,0.8]) #mentioning the area of the plot (origin,width,height)
# languages=['English','French','Spanish','Latin','German']
# people=[100,50,150,40,70]
# ax.bar(languages,people)
# plt.xlabel('Languages')
# plt.ylabel('Number of people')
# plt.show()

#Pie chart
# fig=plt.figure()
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# languages=['English','French','Spanish','Latin','German']
# people=[100,50,150,40,70]
# ax.pie(people,labels=languages,autopct='%1.1f%%')
# plt.show()

#Scatter plot
# x=np.linspace(0,10,30)
# y=np.sin(x)
# z=np.cos(x)

# fig=plt.figure()
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# ax.scatter(x,y,color='g')
# ax.scatter(x,z,color='b')
# plt.show()

#3d Scatter plot
fig=plt.figure()
ax=plt.axes(projection='3d')
z=20*np.random.random(100)
x=np.sin(z)
y=np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()