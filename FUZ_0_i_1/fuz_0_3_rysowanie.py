import matplotlib.pyplot as plt 
import numpy as np

data = np.loadtxt("fuz0_3.txt") 

# x = np.linspace(0, 10, 11)
# y = np.linspace(0, 10, 11)

x = np.arange(0, 11, 1)
y = np.arange(0, 11, 1)

X, Y = np.meshgrid(x,y)


# plt.pcolor(X,Y,data)
plt.imshow(data, cmap="grey")
plt.show()
