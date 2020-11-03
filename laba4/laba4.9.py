"""9. Для довільного сигналу виконати пряме, а потім обернене перетворення Фурьє, порівняти початковий сигнал та
відновлений сигнал. Знайти середньоквадратичну похибку відновлення (функція std). Зробити висновки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.io import loadmat

eeg_healthy = loadmat('../data/EEG_healthy/eeg_healthy_9.mat')
x = eeg_healthy['sig'][0]
sample_rate = 256
duration = len(x) / sample_rate

time = np.linspace(0, duration, len(x))
frequency = np.linspace(0, sample_rate, len(x))
y = fft(x)
iy = ifft(y)
amplitude_y = 2 * np.abs(y / len(x))
print(np.std(np.abs(x-iy)))

fig, axes = plt.subplots(3, constrained_layout=True)
fig.set_size_inches(8, 6)
axes[0].plot(time, x)
axes[1].stem(frequency, amplitude_y)
axes[2].plot(time, iy.real)
axes[1].set_xlim(0, sample_rate / 2)
axes[0].set_xlabel('Час, с')
axes[1].set_xlabel('Частота, Гц')
# ax.set_ylabel("Амплітуда, В")
# ax[0].set_title(f"Частота {f[i]} Гц")
axes[1].set_title("Спектр")
plt.show()
