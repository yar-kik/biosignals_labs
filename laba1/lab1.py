import numpy as np
import matplotlib.pyplot as plt

k = 2
b = -3
x = np.arange(15)
y = k * x + b
plt.plot(x, y, linewidth=3)
plt.title('Графік лінійної функції', fontsize=14)
plt.xlabel('Вісь х', fontsize=12)
plt.ylabel('Вісь у', fontsize=12)
plt.minorticks_on()
plt.tick_params(which='major', length=10, width=2, labelsize=12)
plt.tick_params(which='minor', length=5, width=1)
plt.scatter(x, y, s=30, c='red')
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
