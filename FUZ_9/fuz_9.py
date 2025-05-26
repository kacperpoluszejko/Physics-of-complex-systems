import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

# Parametry
N = 10000
m0 = 5
m = 4

# Tworzymy graf o N wierzchołkach
A = {i: [] for i in range(N)}  

# Pierwsze m0 wierzchołków jest połączone
for i in range(m0):
    for j in range(i + 1, m0):
        A[i].append(j)
        A[j].append(i)

# Dołączamy nowe wierzchołki
for new_node in range(m0, N):
    degrees = {i: len(A[i]) for i in range(new_node)}
    nodes = list(degrees.keys())
    weights = list(degrees.values())

    targets = []
    total_weight = sum(weights)

   # Losowanie "targetów", które będą dołączone
    while len(targets) < m:
        r = random.uniform(0, total_weight)
        cumulative = 0

        for node, weight in zip(nodes, weights):
            cumulative += weight
            if r < cumulative:
                if node not in targets:
                    targets.append(node)
                break 

    for target in targets:
        A[new_node].append(target)
        A[target].append(new_node)

gr = nx.Graph()
gr.add_nodes_from(range(N))
for i, v in A.items():
    for j in v:
        gr.add_edge(i, j)

# ZADANIE 1 (rysowanie grafu o N = 100 wierzchołkach)
# nx.draw(gr, node_size=50, with_labels=False)
# plt.title("Graf Barabásiego–Alberta (m₀=5, m=4, N=100)")
# plt.show()

#ZADANIE 2 - rozkład stopni
N = len(A)

rank_dist = np.zeros(N)

for i in range(N):
    rank = len(A[i])
    rank_dist[rank] += 1

rank_dist /= (N - 1)

rank_table = np.arange(0, N)
nonzero = rank_dist > 0

k_values = rank_table[nonzero]
P_k = rank_dist[nonzero]

log_k = np.log10(k_values)
log_Pk = np.log10(P_k)

slope, intercept = np.polyfit(log_k, log_Pk, 1)
alpha = -slope

print(f"Szacowane alfa = {alpha:.3f}")
plt.figure(figsize=(8,6))
plt.plot(k_values, P_k, 'o', label="Numerycznie")
plt.plot(k_values, 10**intercept * k_values**slope, 'r-', label="Dopasowanie")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("k (stopień wierzchołka)")
plt.ylabel("P(k)")
plt.title(f"P(k), alfa = {alpha:.3f}")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()
plt.savefig("zad2.png")
plt.show()

