"""6. Сформувати випадковий сигнал тривалістю 10 с для частоти дисктеризації 1000 Гц. Побудувати за допомогою функції
plot графік сигналу та його амплітудного спектру, зробити висновки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

sample_rate = 1000
duration = 10
time = np.linspace(0, duration, duration * sample_rate)
frequency = np.linspace(0, sample_rate, duration * sample_rate)

x = np.random.rand(len(time))
y = 2 * np.abs(fft(x) / len(x))
x_label = ['Час, с', 'Частота, Гц']
title = ['Графік випадкового сигналу', 'Амплітудний спектр сигналу']

fig, ax = plt.subplots(2, constrained_layout=True)
fig.set_size_inches(12, 6)
ax[0].plot(time, x, linewidth=.7)
ax[1].stem(frequency[1:], y[1:])
ax[1].set_xlim(0, sample_rate / 2)
for i in range(2):
    ax[i].set_xlabel(x_label[i])
    ax[i].set_title(title[i])
    ax[i].set_ylabel("Амплітуда")
    ax[i].minorticks_on()
    ax[i].grid(which='major', linewidth=1.2)
    ax[i].grid(which='minor', linewidth=.5)
plt.show()