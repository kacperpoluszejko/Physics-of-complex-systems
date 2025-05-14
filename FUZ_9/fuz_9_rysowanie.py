import numpy as np
import matplotlib.pyplot as plt
import math

X, Y = np.loadtxt("fuz9_1.txt", delimiter=" ", unpack=True, usecols=(0, 1))

N = 100
alfa1 = 4
alfa2 = 10
av_k = alfa1*(N-1)/N #Jeśli chcemy rysować wartość teoratyczną dla innej alfy zmienić to tutaj
X2 = []
Y2 = np.zeros(25)
for i in range(25):
    X2.append(i)
    Y2[i] = np.exp(-av_k)*pow(av_k, X2[i])/math.factorial(X2[i])


plt.plot(X, Y, "black", marker = "s", markersize = 3, label = "Numerical")
plt.plot(X2, Y2, "red", marker = "s", markersize = 3, label = "Theoretical")

plt.xlabel("Stopień")
plt.ylabel("P(stopień)")
plt.title(r"$\alpha = 4$")
plt.legend()
plt.savefig("Zad_3_1.png")
