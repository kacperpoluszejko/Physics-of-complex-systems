import numpy as np
import matplotlib.pyplot as plt


with open("fuz1.txt", "r") as f:
    data = f.read().strip().split("\n\n")  # Oddziel kroki 


steps = []
for step_data in data:
    lines = step_data.split("\n")  
    grid = np.array([list(map(int, line.split())) for line in lines])
    print(grid)
    steps.append(grid)

time = np.array([0,1,2,5,10,50,100])
for i, grid in enumerate(steps):
    plt.imshow(grid, cmap="gray_r")  # Czarny = 1, Biały = 0
    plt.title(f"Step {time[i]}")
    plt.savefig(f"V3_Step_{time[i]}")
    plt.pause(1.5)  # Pauza między krokami
    plt.clf() # Wyczyść przed kolejnym krokiem

plt.show()