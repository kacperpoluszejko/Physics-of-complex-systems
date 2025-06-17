import numpy as np
from numba import njit
from itertools import product

@njit
def calculate_energy(config, J):
    N = len(config)
    energy = 0.0
    for i in range(N):
        energy -= J[i] * config[i] * config[(i + 1) % N]
    return energy


def generate_all_configs(N):
    return np.array(list(product([-1, 1], repeat=N)))

@njit
def is_stable(configuration, J):
    N = len(configuration)
    base_energy = calculate_energy(configuration, J)
    for i in range(N):
        flipped = configuration.copy()
        flipped[i] *= -1
        new_energy = calculate_energy(flipped, J)
        if new_energy < base_energy:
            return False
    return True

@njit
def count_stable_configs(configs, J):
    count = 0
    for config in configs:
        if (is_stable(config, J)):
            count += 1
    return count

def trials(N, trials = 100):
    configs = generate_all_configs(N)
    counts = []
    for i in range(trials):
        J = np.random.normal(0.0, 1.0, size=N)
        counts.append(count_stable_configs(configs, J))
    avg = np.mean(counts)
    return avg

for N in [9, 12, 15]:
    avg = trials(N)
    print(f"N = {N}")
    print(f"  Średnia liczba stabilnych stanów: {avg}")