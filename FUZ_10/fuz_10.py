import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def kuramoto_rhs(t, theta, omega, K, N):
    return omega + (K / N) * np.sum(np.sin(theta - theta[:, None]), axis=1)

#ZADANIE 1
# Parametry ogólne
N = 50
K_values = np.arange(0.25, 5.25, 0.5)
Tmax = 100
dt = 0.5
t_eval = np.arange(0, Tmax, dt)

np.random.seed(42)
omega = np.random.normal(0, 0.5, N)
theta0 = np.random.uniform(0, 2*np.pi, N)

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
#Parametry ogólne
N = 50
K_values = np.arange(0.25, 5.25, 0.5)
Tmax = 100
dt = 0.5
t_eval = np.arange(0, Tmax, dt)
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
    plt.plot(K_values, r_table, label = f"N = {N}")
plt.xlabel("K")
plt.ylabel("r")
plt.title("r(K)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#ZADANIE 3
N = 50
Tmax = 100
dt = 1
t_eval = np.arange(0, Tmax, dt)
K_values = [0.01, 0.8, 2.0]


np.random.seed(0)
omega = np.random.normal(0, 0.5, N)

theta_uniform_1 = np.random.uniform(0, 2 * np.pi, N // 2)
theta_uniform_2 = np.random.uniform(0, np.pi / 12, N // 2)
theta_0 = [np.concatenate([theta_uniform_1, theta_uniform_2])]

# Iteracja po wartościach K i konfiguracjach
for K in K_values:
    sol = solve_ivp(
        kuramoto_rhs,
        [0, Tmax], theta0,
        args=(omega, K, N),
        t_eval=t_eval,
        method='RK45'
    )

    r_t = np.abs(np.mean(np.exp(1j * sol.y), axis=0))
    plt.plot(sol.t, r_t, label=f"K={K}")

# Finalizacja wykresu
plt.xlabel("t")
plt.ylabel("r")
plt.title("Desynchronizacja – parametr porządku r(t)")
plt.ylim(0, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()