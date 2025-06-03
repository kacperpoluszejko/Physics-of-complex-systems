import numpy as np

def distance(N):
    distances = []
    repeats = N*10
    for i in range(repeats):
        x_pos, y_pos = 0.0, 0.0
        for j in range(N):
            theta = np.random.uniform(0, 2 * np.pi)
            x_pos += np.cos(theta)
            y_pos += np.sin(theta)
        distance = np.sqrt(x_pos**2 + y_pos**2)
        distances.append(distance)

    srednia = np.mean(distances)
    odch = np.std(distances)
    return srednia, odch

Ns = [10, 100, 200]

for N in Ns:
    mean_d, std_d = distance(N)
    expected_d = np.sqrt(N)
    print(f"N = {N}\t{mean_d:.4f} ± {std_d:.4f}\t expected = {expected_d:.4f}")
