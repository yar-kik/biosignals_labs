import numpy as np
import matplotlib.pyplot as plt

sample_rate = 256
t = np.arange(0, 10 + 1 / sample_rate, 1 / sample_rate)
y = np.zeros_like(t)
interval = np.random.rand(10)*4
duration = .8
start = 0
end = start + duration
i = 0
while end < t[-1] + duration:
    y[int(start * sample_rate):int(end * sample_rate)] = 1
    start = end + interval[i]
    end = start + duration
    i += 1

plt.plot(t, y, linewidth=2)
plt.title('Графік прямокутних імпульсів з випадковим інтервалом', fontsize=14)
plt.xlabel('Час, t', fontsize=10)
plt.ylabel('Амплітуда, А', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()