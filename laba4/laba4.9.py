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

t = np.linspace(0, duration, len(x))
f = np.linspace(0, sample_rate, len(x))
y = fft(x)
restored_x = ifft(y)

standard_deviation = np.std(np.abs(x - restored_x))
print("Середньоквадратична похибка відновлення: ", standard_deviation)

title = ['Початковий сигнал', "Відновлений сигнал"]
fig, ax = plt.subplots(2, constrained_layout=True)
fig.set_size_inches(12, 6)
ax[0].plot(t, x)
ax[1].plot(t, restored_x.real)
for j in range(2):
    ax[j].set_xlabel('Час, с')
    ax[j].set_title(title[j])
    ax[j].set_ylabel("Амплітуда")
    ax[j].minorticks_on()
    ax[j].grid(which='major', linewidth=1.2)
    ax[j].grid(which='minor', linewidth=.5)
plt.show()
