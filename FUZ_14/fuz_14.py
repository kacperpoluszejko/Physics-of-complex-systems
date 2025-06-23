import numpy as np

def to_vector(grid):
    return np.array(grid).flatten()

def calc_W(patterns):
    N = patterns[0].size
    W = np.zeros((N, N))
    for p in patterns:
        for i in range(N):
            for j in range(N):
                W[i][j] += p[i] * p[j]
    for i in range(N):
        W[i][i] = 0
    return W

def recover(W, x_init, max_steps=100):
    x = x_init.copy()
    for _ in range(max_steps):  
        x_new = np.sign(W @ x)
        if np.array_equal(x, x_new):
            break  
        x = x_new
    return x

def print_pattern(vec, size=5):
    for i in range(size):
        row = vec[i*size:(i+1)*size]
        print(list(int(v) for v in row))

T = to_vector([
    [-1, -1, -1, -1, -1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1]
])
H = to_vector([
    [-1, 1, 1, 1, -1],
    [-1, 1,-1, 1, -1],
    [-1,-1,-1,-1, -1],
    [-1, 1,-1, 1, -1],
    [-1, 1,-1, 1, -1]
]) 
A = to_vector([
    [ 1, 1,-1, 1, 1],
    [ 1,-1, 1,-1, 1],
    [ 1,-1, 1,-1, 1],
    [-1,-1,-1,-1,-1],
    [-1, 1, 1, 1,-1]
]) 

W = calc_W([T, H, A])

T_2 = T.copy()
T_2[3] *= -1  
T_rec = recover(W, T_2)


print("Odzyskany wzorzec T:")
print_pattern(T_rec)