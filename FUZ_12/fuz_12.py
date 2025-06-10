import random
import numpy as np

def zadanie_1(graph, start_node = 0, epsilon=1e-6, max_steps = 10000000):
    graph_size = len(graph)
    visits = np.zeros(graph_size)
    current = start_node
    steps = 0

    prev_prob = np.zeros(graph_size)

    while steps<max_steps: #aby nie było nieskończonej pętli
        visits[current] += 1
        steps += 1
        neighbors = graph[current]
        if neighbors == []:
            current = random.randint(0, graph_size - 1)
        else:
            current = random.choice(neighbors)

        total = np.sum(visits)
        current_prob = np.array([visits[i] / total for i in range(graph_size)])

        if (steps%100000 == 0):
            diff = np.sum(np.abs(current_prob - prev_prob))
            if diff < epsilon:
                print(steps)
                return current_prob

        prev_prob = current_prob

def zadanie_2(graph, start_node = 0, epsilon=1e-6, max_steps = 10000000):
    graph_size = len(graph)
    visits = np.zeros(graph_size)
    current = start_node
    steps = 0

    prev_prob = np.zeros(graph_size)

    while steps<max_steps:
        visits[current] += 1
        steps += 1
        neighbors = graph[current]

        if graph[current]: 
            if random.random() < 0.85:
                current = random.choice(neighbors)
            else:
                current = random.randint(0, graph_size - 1)
        else:
            current = random.randint(0, graph_size - 1)
            
        total = np.sum(visits)
        current_prob = np.array([visits[i] / total for i in range(graph_size)])

        if (steps%100000 == 0):
            diff = np.sum(np.abs(current_prob - prev_prob))
            if diff < epsilon:
                print(steps)
                return current_prob

        prev_prob = current_prob


def zadanie_3(graph, epsilon=1e-6, max_steps = 1000000):
    N = len(graph)
    A = np.zeros((N,N))
    for i in range(N):
        neighbors = graph[i]
        if len(neighbors) == 0:
            for j in range(N):
                A[i][j] = 1/N
        for j in neighbors:
            A[i][j] = 1 / len(neighbors) 
    v = np.ones(N) / N
    diff = 1
    steps = 0
    while diff>(N*epsilon):
        v_new = A.T @ v  
        diff= np.sum(np.abs(v_new - v)) 
        v = v_new
        steps +=1
        if(steps>max_steps):
            break

    return v_new


def zadanie_4(graph, epsilon=1e-6, p = 0.15, max_steps = 1000000):
    N = len(graph)
    A = np.zeros((N,N))
    for i in range(N):
        neighbors = graph[i]
        if len(neighbors) == 0:
            for j in range(N):
                A[i][j] = 1/N
        for j in neighbors:
            A[i][j] = 1 / len(neighbors) 
    v = np.ones(N) / N
    diff = 1
    B = np.ones((N,N))/N
    M = (1-p)*A + p*B
    steps = 0
    while diff>(N*epsilon):
        v_new = M.T @ v  
        diff= np.sum(np.abs(v_new - v)) 
        v = v_new
        if(steps>max_steps):
            break

    return v_new            



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

B = np.array([[0, 1, 0, 0],
              [1, 0, 0, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]])

B2 = {}
for i in range(B.shape[0]):
    neighbors = []
    for j in range(B.shape[1]):
        if B[i][j] == 1:
            neighbors.append(j)
    B2[i] = neighbors



C = np.array([[0, 1, 0, 0],
              [0, 0, 0, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]])

C2 = {}
for i in range(C.shape[0]):
    neighbors = []
    for j in range(C.shape[1]):
        if C[i][j] == 1:
            neighbors.append(j)
    C2[i] = neighbors

probability = zadanie_1(A2)
print("Graf 1, Zadanie 1:")
print(probability)

probability = zadanie_2(A2)
print("Graf 1, Zadanie 2:")
print(probability)

probability = zadanie_3(A2)
print("Graf 1, Zadanie 3:")
print(probability)

probability = zadanie_4(A2)
print("Graf 1, Zadanie 4:")
print(probability)


probability = zadanie_1(B2)
print("Graf 2, Zadanie 1:")
print(probability)

probability = zadanie_2(B2)
print("Graf 2, Zadanie 2:")
print(probability)

probability = zadanie_3(B2)
print("Graf 2, Zadanie 3:")
print(probability)

probability = zadanie_4(B2)
print("Graf 2, Zadanie 4:")
print(probability)



probability = zadanie_1(C2)
print("Graf 3, Zadanie 1:")
print(probability)

probability = zadanie_2(C2)
print("Graf 3, Zadanie 2:")
print(probability)

probability = zadanie_3(C2)
print("Graf 3, Zadanie 3:")
print(probability)

probability = zadanie_4(C2)
print("Graf 3, Zadanie 4:")
print(probability)