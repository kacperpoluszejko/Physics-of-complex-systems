from itertools import product

def calculate_energy(configuration, J):
    N = len(configuration)
    energy = 0
    for i in range(N):
        energy += configuration[i] * configuration[(i + 1) % N]  
    return energy
    

def generate_all(N, J):
    configs = list(product([-1, 1], repeat=N))
    results = []
    for configuration in configs:
        energy = calculate_energy(configuration, J)
        results.append((configuration, energy))
    return results

for N in [5, 6]:
    for J in [1, -1]: 
        label = f"N={N}, J={J}"
        print(f"\n{label}")
        results = generate_all(N, J)
        results_sorted = sorted(results, key=lambda x: x[1], reverse=True)
        for config, energy in results_sorted:
            print(f"Konfiguracja: {config}, Energia: {energy}")
