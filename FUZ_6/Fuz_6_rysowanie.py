import numpy as np
import matplotlib.pyplot as plt



X1, Y1 = np.loadtxt("fuz6_1.txt", delimiter=" ", unpack=True, usecols=(0, 1)) # T=1
X2, Y2 = np.loadtxt("fuz6_2.txt", delimiter=" ", unpack=True, usecols=(0, 1)) # T=2
X3, Y3 = np.loadtxt("fuz6_3.txt", delimiter=" ", unpack=True, usecols=(0, 1)) # T=2.5
X4, Y4 = np.loadtxt("fuz6_7.txt", delimiter=" ", unpack=True, usecols=(0, 1)) # T=4

spins1 = np.loadtxt("fuz6_4.txt", dtype = int) # T=1
spins2 = np.loadtxt("fuz6_5.txt", dtype = int) # T=2
spins3 = np.loadtxt("fuz6_6.txt", dtype = int) # T=2.5
spins4 = np.loadtxt("fuz6_8.txt", dtype = int) # T=4

T, mag, mag2 = np.loadtxt("fuz6_zad4.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2)) 

# T_a = np.arange(0.25, 4, 0.25)  
# m_a = (1 - (1 / np.sinh(2 / T))**4)**(1/8)

plt.plot(T, mag, "o")
plt.xlabel("T")
plt.ylabel("m")
plt.savefig("m(T).jpg")
plt.show()

plt.plot(T, mag2, "o")
plt.xlabel("T")
plt.ylabel("chi")
plt.savefig("chi(T).jpg")
plt.show()


plt.imshow(spins1, cmap='inferno', vmin=-1, vmax=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$T=1.0, L=32, t=10^5, m(0)=1$")
plt.colorbar()
plt.savefig("Spins_T=1.jpg")
plt.show()

plt.plot(X1, Y1)
plt.savefig("Mag_T=1.jpg")
plt.show()

plt.imshow(spins2, cmap='inferno', vmin=-1, vmax=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$T=2.0, L=32, t=10^5, m(0)=1$")
plt.colorbar()
plt.savefig("Spins_T=2.jpg")
plt.show()

plt.plot(X2, Y2)
plt.savefig("Mag_T=2.jpg")
plt.show()

plt.imshow(spins3, cmap='inferno', vmin=-1, vmax=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$T=2.5, L=32, t=10^5, m(0)=1$")
plt.colorbar()
plt.savefig("Spins_T=2.5.jpg")
plt.show()

plt.plot(X3, Y3)
plt.savefig("Mag_T=2.5.jpg")
plt.show()


plt.imshow(spins4, cmap='inferno', vmin=-1, vmax=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$T=4.0, L=32, t=10^5, m(0)=1$")
plt.colorbar()
plt.savefig("Spins_T=4.jpg")
plt.show()

plt.plot(X4, Y4)
plt.savefig("Mag_T=4.jpg")
plt.show()

