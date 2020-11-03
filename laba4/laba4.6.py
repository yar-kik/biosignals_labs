"""6. Сформувати випадковий сигнал тривалістю 10 с для частоти дисктеризації 1000 Гц. Побудувати за допомогою функції
plot графік сигналу та його амплітудного спектру, зробити висновки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

sample_rate = 1000
duration = 10

frequency1 = 10
frequency2 = 100
time = np.linspace(0, duration, duration * sample_rate)
frequency = np.linspace(0, sample_rate, duration * sample_rate)

x = np.random.rand(len(time))
# x = np.random.random(len(time))
y = 2 * np.abs(fft(x) / len(x))


fig, axes = plt.subplots(2, constrained_layout=True)
fig.set_size_inches(8, 6)
axes[0].plot(time, x, linewidth=.7)
axes[1].stem(frequency[1:], y[1:])
axes[1].set_xlim(0, sample_rate / 2)
axes[0].set_xlabel('Час, с')
axes[1].set_xlabel('Частота, Гц')
# ax.set_ylabel("Амплітуда, В")
# ax[0].set_title(f"Частота {f[i]} Гц")
axes[1].set_title("Спектр")
plt.show()