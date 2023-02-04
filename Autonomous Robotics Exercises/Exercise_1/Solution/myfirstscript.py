import numpy as np
import matplotlib.pyplot as plt

#EXERCISE 1
def f(x):
    return np.cos(x)*np.exp(x)

#EXERCISE 2
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=f(x)
plt.plot(x,y,color="red",linewidth="2")

plt.title(" Exercise 2",color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("myFirstPlot.png",format="png")
plt.show()

