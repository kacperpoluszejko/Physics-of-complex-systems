import numpy as np
import matplotlib.pyplot as plt
import random


def count_sick_neighbours(table, x, y):
    sick = 0
    for i in [-1, 0 ,1]:
        for j in [-1, 0, 1]:
            nx = (x+i+N)%N
            ny = (y+j+N)%N
            if (table[nx][ny]==1):
                sick += 1
    return sick


alpha = [0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
print(alpha)
N = 60
b = 0.2
T=201

# S2 = []
# I2 = []
R2 = []

for a in alpha:

    table = np.zeros((N,N))
    p = int(N/2)
    table[p][p] = 1
    # S = []
    # I = []
    R = []

    for t in range(T):
        s = 0
        inf = 0
        r = 0
        table_copy = np.zeros((N,N)) #backup table

        for x in range(N):
            for y in range(N):

                if(table[x][y] == 0):
                    s += 1
                    for i in range(count_sick_neighbours(table, x, y)):
                        U1 = random.random()
                        if(U1 < a):    # chance that he will get sick
                            table_copy[x][y] = 1
                        
                
                if(table[x][y] == 1):
                    inf += 1
                    U2 = random.random() #chance that he will get better
                    if(U2 < b):
                        table_copy[x][y] = -1
                    else:
                        table_copy[x][y] = 1
                
                if(table[x][y] == -1):
                    r += 1
                    table_copy[x][y] = -1

        # if (t == 0 or t==1 or t==2 or t==5 or t==10 or t==50 or t==100):
        #     print(f"Wartość s to {s}, a inf to {inf}.")
        #     plt.imshow(table, cmap='inferno', vmin=-1, vmax=1)
        #     cbar = plt.colorbar()
        #     cbar.set_ticks([-1, 0, 1])  # Ustawienie wartości w legendzie
        #     cbar.set_label("Stan komórki")  # Tytuł legendy
        #     cbar.ax.set_yticklabels(['Odporny', 'Zdrowy', 'Chory'])
        #     plt.title(f"t = {t}, alpha = {a}")
        #     plt.savefig(f"fuz_3_t{t}_a{a}.jpg")
        #     plt.clf()
        table = table_copy

        # S.append(s)    
        # I.append(inf)
        R.append(r)

    # S2.append(S)    
    # I2.append(I)
    R2.append(R)

# plt.figure(figsize=(10, 6))
# for i, y in enumerate(S2):
#     j = round(i*0.1 + 0.1,2)
#     plt.plot(y, label=f'alpha = {j}')
# plt.legend()
# plt.title("S(t)")
# plt.savefig("Zad2_S.jpg")
# plt.show()

plt.figure(figsize=(10, 6))
for i, y in enumerate(R2):
    j = alpha[i]
    plt.plot(y, label=f'alpha = {j}')
plt.legend()
plt.title("R(t)")
plt.savefig("Zad3_R.jpg")
plt.show()


# plt.figure(figsize=(10, 6))
# for i, y in enumerate(I2):
#     j = round(i*0.1 + 0.1,2)
#     plt.plot(y, label=f'alpha = {j}')
# plt.legend()
# plt.title("I(t)")
# plt.savefig("Zad2_I.jpg")
# plt.show()


                    


                

