from itertools import product

def calculate_energy(configuration, J):

    N = len(configuration)
    energy = 0
    for i in range(N):
        energy += configuration[i] * configuration[(i + 1) % N]  
    return -J * energy

def generate_all(N, J):
    configs = list(product([-1, 1], repeat=N))
    results = []
    for config in configs:
        energy = calculate_energy(config, J)
        results.append((config, energy))
    return results


for N in [5, 6]:
    for J in [1, -1]:  # 1: ferromagnetyk, -1: antyferromagnetyk
        label = f"N={N}, J={J}"
        print(f"\n{label}")
        results = generate_all(N, J)
        for config, energy in results:
            print(f"Konfiguracja: {config}, Energia: {energy}")
