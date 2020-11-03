import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt

sample_rate = 256
T = 10
t = np.arange(0, T + 1/sample_rate, 1/sample_rate)
duration = 0.3
center = 4
start_idx = int((center-duration/2)*sample_rate)
end_idx = int((center+duration/2)*sample_rate)
y = np.zeros_like(t)
y[start_idx:end_idx] = 1

plt.plot(t, y, linewidth=2)
plt.title('Графік прямокутного імпульсу', fontsize=14)
plt.xlabel('Час, t', fontsize=10)
plt.ylabel('Амплітуда, А', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
