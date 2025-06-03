import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

# Parametry
N = 100
m = 1  
m0 = 1

G = nx.barabasi_albert_graph(N, m)

def dfs(u, visited, adj):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, visited, adj)

def is_connected(G):
    visited = [False] * len(G.nodes)
    adj = {node: list(G.neighbors(node)) for node in G.nodes}
    dfs(0, visited, adj)
    return all(visited)


plt.figure(figsize=(6, 6))
nx.draw(G, node_size=50, with_labels=False)
plt.show()

adj = {node: list(G.neighbors(node)) for node in G.nodes}
N = len(adj)

rank_dist = np.zeros(N)

for i in range(N):
    rank = len(adj[i])
    rank_dist[rank] += 1

rank_dist /= (N - 1)

rank_table = np.arange(0, N)
nonzero = rank_dist > 0
rank_table = rank_table[nonzero]
rank_dist = rank_dist[nonzero]

print(rank_dist)
plt.plot(rank_table, rank_dist, 'o')
plt.xlabel("Stopień wierzchołka")
plt.ylabel("P(k)")
plt.grid()
plt.show()


print("Spójny przed usunięciem krawędzi:", is_connected(G))

edge = random.choice(list(G.edges))
G.remove_edge(*edge)
print(f"Usunięto krawędź: {edge}")


print("Spójny po usunięciu krawędzi:", is_connected(G))
nx.draw(G, node_size=50, with_labels=False)
plt.show()