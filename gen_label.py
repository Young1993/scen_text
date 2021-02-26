import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-1, 1, 0.01)
def func(x):
    return 1.0 / (1 + math.exp(-1*x))
y = np.vectorize(func)

plt.title("DB")
plt.plot(x, y(x))

plt.show()
