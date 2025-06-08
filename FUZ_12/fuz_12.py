import random
from collections import Counter
import numpy as np

def zadanie_1(graph, start_node, epsilon=1e-6):
    graph_size = len(graph)
    visits = np.zeros(graph_size)
    current = start_node
    steps = 0

    prev_prob = np.zeros(graph_size)

    while True:
        visits[current] += 1
        steps += 1
        neighbors = graph[current]
        current = random.choice(neighbors)

        total = np.sum(visits)
        current_prob = np.array([visits[i] / total for i in range(graph_size)])

        if (steps%1000 == 0):
            diff = np.sum(np.abs(current_prob - prev_prob))
            if diff < epsilon:
                print(steps)
                return current_prob, steps

        prev_prob = current_prob

    print(f"Nie osiągnięto zbieżności po {max_steps} krokach.")
    total = sum(visits.values())
    final_prob = np.array([visits[i] / total for i in range(len(graph))])
    return final_prob, steps


A = np.array([[0, 1, 1, 1],
                 [1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 1, 0]])

A2 = {}
for i in range(A.shape[0]):
    neighbors = []
    for j in range(A.shape[1]):
        if A[i][j] == 1:
            neighbors.append(j)
    A2[i] = neighbors


probability, steps = zadanie_1(A2, 0)
print(probability)
