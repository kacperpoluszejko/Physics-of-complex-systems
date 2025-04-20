import numpy as np
import matplotlib.pyplot as plt

with open("fuz2_2.txt", "r") as f:
    data = f.read().strip().split('\n\n')


steps = []
for step_data in data:
    lines = step_data.split("\n")  
    grid = np.array([list(map(float, line.split())) for line in lines])
    steps.append(grid)


for i,step in enumerate(steps):
    x = step[:, 0]
    y = step[:, 1]
    plt.plot(x,y,color = 'black',marker = '.' ,markersize = 2, linewidth = 0.5)
    plt.xlabel("n")
    plt.ylabel("x")
    filename = f'fuz2_2rysowanie({i + 1}).png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.pause(1)
    plt.clf() 
plt.show()

