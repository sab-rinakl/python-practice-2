import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
for i in range(0, 200):
    x.append(np.random.randint(0, 201))
    y.append(np.random.randint(0, 201))

plt.scatter(x, y, color='r', marker='.')
plt.xlabel('Random integer', color='b')
plt.ylabel('Random integer', color='b')
plt.title('Scatter of random integers', color='g')
plt.axis([0, 200, 0, 200])
plt.show()

