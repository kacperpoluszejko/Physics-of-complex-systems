import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def kuramoto_rhs(t, theta, omega, K, N):
    return omega + (K / N) * np.sum(np.sin(theta - theta[:, None]), axis=1)

# Parametry ogólne
N = 50
K_values = np.arange(0.25, 5.25, 0.5)
Tmax = 100
dt = 0.5
t_eval = np.arange(0, Tmax, dt)

np.random.seed(42)
omega = np.random.normal(0, 0.5, N)
theta0 = np.random.uniform(0, 2*np.pi, N)

#ZADANIE 1
for K in K_values:
    sol = solve_ivp(kuramoto_rhs, [0, Tmax], theta0, t_eval=t_eval, args=(omega, K, N),method='RK45')
    theta_mod = np.mod(sol.y, 2*np.pi)
    z_t = np.mean(np.exp(1j * sol.y), axis=0)  
    r_t = np.abs(z_t)                          
    #psi_t = np.angle(z_t)    - faza    

    # Wykres theta(t)
    # plt.figure(figsize=(10, 4))
    # for i in range(N):
    #     plt.plot(sol.t, theta_mod[i], linewidth=0.7)
    # plt.title(f'N = {N}, K = {K:.2f}')
    # plt.xlabel('t')
    # plt.ylabel('θ mod $2π$')
    # plt.show()

    plt.plot(sol.t, r_t, label=f"K = {K:.2f}")
plt.xlabel("t")
plt.ylabel("r")
plt.title("Parametr porządku r(t) dla różnych K")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#ZADANIE 2
N_table = np.array([10, 20, 50])

for N in N_table:
    np.random.seed(0)
    omega = np.random.normal(0, 0.5, N)
    theta0 = np.random.uniform(0, 2*np.pi, N)
    r_table = []
    for K in K_values:
        sol = solve_ivp(kuramoto_rhs, [0, Tmax], theta0, t_eval=t_eval, args=(omega, K, N), method='RK45')

        z_t = np.mean(np.exp(1j * sol.y), axis=0)  
        r_t = np.abs(z_t)
        r_table.append(np.mean(r_t[-10:]))
    plt.plot(K_values, r_table, label = "N = {N}")
plt.xlabel("K")
plt.ylabel("r")
plt.title("r(K)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()