import numpy as np
import matplotlib.pyplot as plt

dist = np.random.randint(10, size=10)

plt.hist(dist,[0,4,6,8,10])
plt.show()