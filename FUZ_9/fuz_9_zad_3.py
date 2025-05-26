import networkx as nx
import matplotlib.pyplot as plt
import random

# Parametry
N = 100
m = 1  

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
plt.title("Graf BA (N=100, m=1)")
plt.show()

print("Spójny przed usunięciem krawędzi:", is_connected(G))

edge = random.choice(list(G.edges))
G.remove_edge(*edge)
print(f"Usunięto krawędź: {edge}")


print("Spójny po usunięciu krawędzi:", is_connected(G))
nx.draw(G, node_size=50, with_labels=False)
plt.show()