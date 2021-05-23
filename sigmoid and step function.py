import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def stepfunction(x):
    return np.array(x > 0, dtype=np.int)



x = np.arange(-5.0, 5.0, 0.1)

y0 = stepfunction(x)

y = sigmoid(x)

plt.plot(x, y)
plt.plot(x, y0, linestyle = "--")
plt.ylim(-0.1, 1.1)
plt.show()