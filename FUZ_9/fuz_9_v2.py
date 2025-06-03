import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

# Parametry
N = 100
m0 = 5
m = 4

A = {i: [] for i in range(N)}

for i in range(m0):
    for j in range(i+1, m0):
        A[i].append(j)
        A[j].append(i)

for new_node in range(m0, N):
    degrees = {i: len(A[i]) for i in range(new_node)}
    nodes = list(degrees.keys())
    weights = list(degrees.values())

    targets = []
    total_weight = sum(weights)

# targety to wierzchołki które będą dołączone
    while(len(targets) < m):
        U = random.uniform(0, total_weight)
        suma = 0
        for node, weight in zip(nodes, weights):
            suma += weight
            if(U<suma):
                if node not in targets:
                    targets.append(node)
                break
    
    for target in targets:
        A[target].append(new_node)
        A[new_node].append(target)


gr = nx.Graph()
gr.add_nodes_from(range(N))
for i, v in A.items():
    for j in v:
        gr.add_edge(i, j)

#Zadanie 1
nx.draw(gr, node_size=50, with_labels=False)
plt.savefig("Zad1.png")
plt.show()

#Zadanie 2
N = len(A)

rank_dist = np.zeros(N)

for i in range(N):
    rank = len(A[i])
    rank_dist[rank] += 1

rank_dist /= (N - 1)

rank_table = np.arange(0, N)
nonzero = rank_dist > 0
rank_table = rank_table[nonzero]
rank_dist = rank_dist[nonzero]

log_rank_table = np.log10(rank_table)
log_rank_dist = np.log10(rank_dist)

slope, intercept = np.polyfit(log_rank_table, log_rank_dist, 1)
alpha = -slope

print(f"Szacowane alfa = {alpha:.3f}")
plt.plot(log_rank_table, log_rank_dist, 'o')
plt.plot(log_rank_table, slope*log_rank_table + intercept)
plt.xlabel("k (stopień wierzchołka)")
plt.ylabel("P(k)")
plt.show()
