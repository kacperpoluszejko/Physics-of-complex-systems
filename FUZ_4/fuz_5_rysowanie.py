import numpy as np
import matplotlib.pyplot as plt



X1, Y1, Z1 = np.loadtxt("fuz5.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X2, Y2, Z2 = np.loadtxt("fuz6.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X3, Y3, Z3 = np.loadtxt("fuz7.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X4, Y4, Z4 = np.loadtxt("fuz8.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))

X5, Y5, Z5 = np.loadtxt("fuz1.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X6, Y6, Z6 = np.loadtxt("fuz2.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X7, Y7, Z7 = np.loadtxt("fuz3.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))
X8, Y8, Z8 = np.loadtxt("fuz4.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))

# Definiujemy zakres wartości 1/T
T = np.linspace(0.5, 4, 50)  # Unikamy dzielenia przez zero
y = -np.tanh(T)

T2 = np.linspace(0.5, 4, 50)  # Unikamy dzielenia przez zero
y2 = T2*T2/(np.cosh(T2)*np.cosh(T2))


X1, Y1, Z1 = np.loadtxt("fuz_zad3.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2))

C = (Z1 - Y1*Y1)*X1*X1/1000

# plt.plot(T, y, 'x', label = "Analitycznie")
# plt.plot(X1, Y1, label = "Numerycznie")
# plt.legend()
# plt.xlabel("1/T")
# plt.ylabel('<E(t)>')
# plt.savefig("Zad3_srednia.jpg")
# plt.show()
# plt.title("Energia 1/T = 4")
# plt.savefig('Energia_T_4.jpg')
# plt.show()

plt.plot(T2, y2, 'x')
plt.plot(X1, C)
plt.legend()
plt.xlabel("1/T")
plt.ylabel('Wariancja')
plt.savefig("Zad3_wariancja.jpg")
plt.show()

# Z = np.ones(len(X1))
# Z1 = -Z*np.tanh(0.5)
# Z2 = -Z*np.tanh(1.5)
# Z3 = -Z*np.tanh(2.5)
# Z4 = -Z*np.tanh(4)

# plt.plot(X1, Y1, linewidth = 0.5)
# plt.plot(X5, Y5, linewidth = 0.5)
# plt.plot(X5, Z1)
# plt.xlabel("t")
# plt.ylabel("E(t)")
# plt.title("E(t) 1/T = 0.5")
# plt.savefig("Energia_beta_0.5.jpg")
# plt.show()

# plt.plot(X2, Y2, linewidth = 0.5)
# plt.plot(X6, Y6, linewidth = 0.5)
# plt.plot(X6, Z2)
# plt.xlabel("t")
# plt.ylabel("E(t)")
# plt.title("E(t) 1/T = 1.5")
# plt.savefig("Energia_beta_1.5.jpg")
# plt.show()

# plt.plot(X3, Y3, linewidth = 0.5)
# plt.plot(X7, Y7, linewidth = 0.5)
# plt.plot(X7, Z3)
# plt.xlabel("t")
# plt.ylabel("E(t)")
# plt.title("E(t) 1/T = 2.5")
# plt.savefig("Energia_beta_2.5.jpg")
# plt.show()

# plt.plot(X4, Y4, linewidth = 0.5)
# plt.plot(X8, Y8, linewidth = 0.5)
# plt.plot(X8, Z4)
# plt.xlabel("t")
# plt.ylabel("E(t)")
# plt.title("E(t) 1/T = 4,0")
# plt.savefig("Energia_beta_4.jpg")
# plt.show()
