import numpy as np
import matplotlib.pyplot as plt

with open("fuz2_3.txt", "r") as f:
    data = f.read().strip().split('\n\n')


steps = []
for step_data in data:
    lines = step_data.split("\n")  
    grid = np.array([list(map(float, line.split())) for line in lines])
    steps.append(grid)

r_table = np.linspace(1,4,601)


for i,r in enumerate(r_table):
    # print(r)
    x = steps[i][:, 1] 
    plt.scatter([r] * len(x), x,edgecolors = "none", s=0.1, color='black')

plt.xlabel("r")
plt.ylabel("x")
plt.savefig("fuz2_3rysowanie.jpg", dpi = 1000)
plt.show()


# for step in steps:
#     x = step[:, 0]
#     y = step[:, 1]
#     plt.plot(x,y,color = 'black',marker = '.' ,markersize = 1)
#     # plt.pause(1.5) 
#     # plt.clf() 
# plt.show()





# print(x)

# plt.ylim(0, 1)
# plt.show()