import numpy as np
import matplotlib.pyplot as plt

X, Y = np.loadtxt("fuz7_1.txt", delimiter=" ", unpack=True, usecols=(0, 1))
X2, Y2 = np.loadtxt("fuz7_2.txt", delimiter=" ", unpack=True, usecols=(0, 1))

plt.plot(X, Y, "black", marker = "s", markersize = 5)
plt.plot(X2, Y2, "red", marker = "x", markersize = 5)
plt.show()