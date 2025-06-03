import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

N, X1, X2, X3, X4, X5= np.loadtxt("fuz11.txt", delimiter=" ", unpack=True, usecols=(0, 1, 2, 3, 4, 5))

plt.plot(N, X1)
plt.plot(N, X2)
plt.plot(N, X3)
plt.plot(N, X4)
plt.plot(N, X5)
plt.xlabel("N")
plt.ylabel("d")
plt.savefig("Zad1_1.png")
plt.show()

#ZADANIE 1_2
N = 20
d_values = np.loadtxt("fuz11_zad1_1.txt")
d_values = np.round(d_values).astype(int)

d_range_full = np.arange(-N, N + 1)
bins_full = np.append(d_range_full - 0.5, d_range_full[-1] + 0.5) 
hist_counts, _ = np.histogram(d_values, bins=bins_full)
hist_norm = hist_counts / np.sum(hist_counts)
even_mask = (d_range_full % 2 == 0)
d_range_even = d_range_full[even_mask]
hist_norm_even = hist_norm[even_mask]

d_range_even = np.arange(-N, N + 1, 2)
P_N = comb(N, (d_range_even + N) // 2) * (0.5) ** N

plt.figure(figsize=(8, 6))
plt.plot(d_range_even, hist_norm_even, 'o', markersize = 12, label='Symulacja')
plt.plot(d_range_even, P_N, 's', label='Rozkład teoretyczny')
plt.xlabel('$d$')
plt.ylabel('$P_N(d)$')
plt.legend()
plt.savefig("Zad_1_2.png")
plt.show()