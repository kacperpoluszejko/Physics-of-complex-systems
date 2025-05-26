import networkx as nx
import random
import matplotlib.pyplot as plt

# Parametry
N = 100
m0 = 5
m = 4

# Krok 1: Stwórz początkowy pełny graf
A = {i: [] for i in range(N)}  # słownik sąsiedztwa

# Tworzymy pełne połączenia między pierwszymi m0 wierzchołkami
for i in range(m0):
    for j in range(i + 1, m0):
        A[i].append(j)
        A[j].append(i)

# Krok 2: Dodaj nowe wierzchołki z przyłączaniem preferencyjnym
for new_node in range(m0, N):
    # Lista istniejących wierzchołków i ich stopni
    degrees = {i: len(A[i]) for i in range(new_node)}
    nodes = list(degrees.keys())
    weights = list(degrees.values())

    targets = []
    total_weight = sum(weights)

    while len(targets) < m:
        r = random.uniform(0, total_weight)  # losujemy liczbę z zakresu [0, suma wag)
        cumulative = 0

        for node, weight in zip(nodes, weights):
            cumulative += weight
            if r < cumulative:
                if node not in targets:
                    targets.append(node)
                break  # wybraliśmy jeden wierzchołek, wychodzimy z pętli for

    # Dodaj połączenia do słownika sąsiedztwa
    for target in targets:
        A[new_node].append(target)
        A[target].append(new_node)

# Krok 3: Stwórz graf z Twojego fragmentu
gr = nx.Graph()
gr.add_nodes_from(range(N))
for i, v in A.items():
    for j in v:
        gr.add_edge(i, j)

# Rysowanie
nx.draw(gr, node_size=50, with_labels=False)
plt.title("Graf Barabásiego–Alberta (m₀=5, m=4, N=100)")
plt.show()
