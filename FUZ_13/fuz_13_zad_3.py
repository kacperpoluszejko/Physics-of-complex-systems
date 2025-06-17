import numpy as np
from numba import njit
from itertools import product
from itertools import combinations

@njit
def calculate_energy(config, J):
    N = len(config)
    energy = 0.0
    for i in range(N):
        energy -= J[i] * config[i] * config[(i + 1) % N]
    return energy

@njit
def is_stable(config, J):
    N = len(config)
    base_energy = calculate_energy(config, J)
    for i in range(N):
        flipped1 = config.copy()
        flipped1[i] *= -1
        new_energy = calculate_energy(flipped1, J)
        if new_energy < base_energy:
            return False
        for j in range(i + 1, N):
            flipped2 = config.copy()
            flipped2[i] *= -1
            flipped2[j] *= -1
            new_energy = calculate_energy(flipped2, J)
            if new_energy < base_energy:
                return False
    return True

def generate_all_configs(N):
    return np.array(list(product([-1, 1], repeat=N)))

@njit
def count_stable_configs(configs, J):
    count = 0
    for i in range(len(configs)):
        if is_stable(configs[i], J):
            count += 1
    return count

def run_simulation(N, trials=100):
    configs = generate_all_configs(N)
    stable_counts = []
    for _ in range(trials):
        J = np.random.normal(0.0, 1.0, size=N)
        count = count_stable_configs(configs, J)
        stable_counts.append(count)
    avg_stable = np.mean(stable_counts)
    expected = 2 ** (N / 5)
    return avg_stable, expected

for N in [9, 12, 15]:
    avg, expected = run_simulation(N, trials=100)
    print(f"N = {N}")
    print(f"  Średnia liczba stabilnych stanów: {avg}")
    print(f"  Wartość teoretyczna (2^(N/5))    : {expected}\n")




