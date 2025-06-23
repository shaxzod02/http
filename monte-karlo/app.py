import matplotlib.pyplot as plt
import numpy as np
import random as rn

N = 2000
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

xx = np.linspace(ax, bx, 100)
y1 = xx**2; y2 = xx/2 + 1
plt.plot(xx, y1, color = "black", linewidth = 3)
plt.plot(xx, y2, color = "black", linewidth = 3)
plt.ylim(ay, by)
plt.show()

S_toliq = (bx - ax) * (by - ay)
S_soha = S_toliq * n / N

print("Sohaning yuzi = ", S_soha)