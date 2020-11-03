import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

sample_rate = 256
t = np.arange(0, 10 + 1 / sample_rate, 1 / sample_rate)
y = np.zeros_like(t)
for i in range(0, len(t), 500):
    y[i:] = square(2 * np.pi * t[i:] * .5, duty=np.random.random())


# np.save('data_file.npy', (t, y))
# t, y = np.load('data_file.npy')
plt.plot(t, y, linewidth=2)
plt.title('Графік прямокутних імпульсів з випадковим інтервалом', fontsize=14)
plt.xlabel('Час, t', fontsize=10)
plt.ylabel('Амплітуда, А', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
