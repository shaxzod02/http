import matplotlib.pyplot as plt
import numpy as np
import random as rn

N = 500
n = 0
ax = - 2; bx = 2; ay = 0; by = 2
for i in range(0, N):
    x = rn.uniform(ax, bx)
    y = rn.uniform(ay, by)
    if y >= x**2 and y <= x/2 + 1:
        plt.scatter(x, y, color='blue')
        n = n + 1
    else:
        plt.scatter(x, y, color='red')