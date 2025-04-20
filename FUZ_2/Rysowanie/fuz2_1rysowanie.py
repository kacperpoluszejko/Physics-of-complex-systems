import numpy as np
import matplotlib.pyplot as plt

with open("fuz2_1.txt", "r") as f:
    data = f.read().strip().split('\n\n')


steps = []
for step_data in data:
    lines = step_data.split("\n")  
    grid = np.array([list(map(float, line.split())) for line in lines])
    steps.append(grid)


for step in steps:
    x = step[:, 0]
    y = step[:, 1]
    plt.plot(x,y,color = 'black',marker = '.' ,markersize = 3, linewidth = 0.1)
    plt.xlabel("n")
    plt.ylabel("x")
    # plt.pause(1.5) 
    # plt.clf() 
plt.savefig("fuz2_1_rysowanie.jpg")
plt.show()

