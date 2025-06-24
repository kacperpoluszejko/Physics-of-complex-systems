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

def is_correct(tab1, tab2):
    if np.array_equal(tab1, tab2):
        print("Wzorzec poprawnie odtworzony \n")
    else:
        print("Wzorzec niepoprawnie odtworzony \n")

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

E = to_vector([
    [-1,-1,-1,-1,-1],
    [-1, 1, 1, 1, 1],
    [-1,-1,-1,-1, 1],
    [-1, 1, 1, 1, 1],
    [-1,-1,-1,-1,-1]
]) 


T2 = to_vector([
    [-1, -1, -1,  1, -1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [-1,  1,  1,  1,  1],
    [ 1,  1, -1,  1,  1]
])
H2 = to_vector([
    [-1, 1, 1, 1, -1],
    [-1, 1, 1, 1, -1],
    [-1, 1,-1,-1,  1],
    [-1, 1, 1, 1,  1],
    [-1, 1, 1, 1, -1]
]) 
A2 = to_vector([
    [ 1, 1, 1, 1, 1],
    [ 1,-1, 1,-1, 1],
    [ 1,-1, 1,-1, 1],
    [ 1, 1, 1, 1, 1],
    [-1, 1, 1, 1,-1]
]) 

W = calc_W([T, H, A, E])
T_rec = recover(W, T2)
H_rec = recover(W, H2)
A_rec = recover(W, A2)


print("Odzyskany wzorzec T:")
print_pattern(T_rec)
is_correct(T, T_rec)

print("Odzyskany wzorzec H:")
print_pattern(H_rec)
is_correct(H, H_rec)

print("Odzyskany wzorzec A:")
print_pattern(A_rec)
is_correct(A, A_rec)