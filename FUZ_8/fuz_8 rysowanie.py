import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych
X = np.loadtxt("fuz8_zad3.txt", delimiter=" ", unpack=True, usecols=(0))
unique_values, counts = np.unique(X, return_counts=True)
probabilities = counts / counts.sum()



unique_values = unique_values[:-250]
probabilities = probabilities[:-250]

log_s = np.log10(unique_values)
log_Ps = np.log10(probabilities)

fit = np.polyfit(log_s, log_Ps, 1)
slope, intercept = fit
tau = -slope  

from scipy.stats import linregress
result = linregress(log_s, log_Ps)
tau_error = result.stderr

print(f"tau = {tau:.4f} ± {tau_error:.4f}")

# Wykres
plt.loglog(unique_values, probabilities, ".", label="Dane")
plt.loglog(unique_values, 10**(intercept) * unique_values**slope, label=f"Dopasowanie: τ = {tau:.4f}± {tau_error:.4f}")
plt.xlabel("s")
plt.ylabel("P(s)")
plt.title("Rozkład P(s) i dopasowanie ")
plt.legend()
plt.savefig("Zad3.png")
plt.show()
